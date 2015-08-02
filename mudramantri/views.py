from django.shortcuts import render
from forms import *
from models import *
from django.shortcuts import  get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import hashlib, datetime, random
from django.utils import timezone
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


# index called for registration as well

def index(request):
    registered = False
    if request.method == 'POST':
        form = RegForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            user = User()
            user.email = email
            user.username = email
            user.first_name = firstname
            user.last_name = lastname
            user.is_active = False
            user.set_password(password)
            user.save()

            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt + email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            # Get user by username

            user = User.objects.get(email=email)

            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
                                      key_expires=key_expires, phone=phone)
            new_profile.save()

            # Initiate progress tracker
            up = userprogressitr(user=user)
            cp = userprogresscomp(user=user)
            up.save()
            cp.save()
            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \
            48 hours http://127.0.0.1:8000/confirm/%s" % (email, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                      [email], fail_silently=False)
            return render(request, 'mudramantri/index.html', {'registered': True})
        else:
            return render(request, 'mudramantri/index.html', {'form': form})
    else:
        form = RegForm()
        return render(request, 'mudramantri/index.html', {'form': form})


def register_confirm(request, activation_key):
    # check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/index')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    # check if the activation key has expired, if it has then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        form = RegForm()
        return render(request, 'mudramantri/index.html', {'form': form, 'expire': True})
    # if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    LogForm = LoginForm()
    return render(request, 'mudramantri/page-login.html', {'form': LogForm, 'verify': True})


def loginUser(request):
    if request.user.is_authenticated():
        form = RegForm()
        return render(request, 'mudramantri/index.html', {'form': form, 'login': True})
    if request.method == 'POST':
        formLogin = LoginForm(data=request.POST)
        if formLogin.is_valid():
            username = formLogin.cleaned_data['username']
            password = formLogin.cleaned_data['password']
            remember = formLogin.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if remember:
                        settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                    else:
                        settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    next = request.GET.get('next', None)
                    if next is not None:
                        return redirect(next)
                    else:
                        return render(request, 'mudramantri/index.html', {'Login': True})
                else:
                    return render(request, 'mudramantri/page-login.html', {'form': formLogin, 'Inactive': True})
            else:
                return render(request, 'mudramantri/page-login.html', {'form': formLogin, 'Invalid': True})
        else:
            return render(request, 'mudramantri/page-login.html', {'form': formLogin})
    else:
        next = request.GET.get('next', None)
        formLogin = LoginForm()
        return render(request, 'mudramantri/page-login.html', {'form': formLogin, 'next': next})


def logoutUser(request):
    logout(request)
    form = RegForm()
    return render(request, 'mudramantri/index.html', {'form': form})


@login_required(login_url='/login/')
def itrDashboard(request):
    user = request.user
    return render(request, 'mudramantri/page-itr-dashboard.html', {})


@login_required(login_url='/login/')
def itrFile(request):
    if request.method == 'POST':
        finyear = request.POST.get('finYear', None)
        noOfForms = (request.POST.get('noOfForms', None))
        if noOfForms is not None:
            noOfForms = int(noOfForms)
            request.session['noOfForms'] = noOfForms
        index = 0
        for key, file in request.FILES.items():
            user = request.user
            username = user.username
            filename = file.name
            x = request.FILES[key]
            y = x.field_name
            itrfile, createdfile = ItrFile.objects.get_or_create(user=user)
            itrfilemeta, createdmeta = ItrFileMeta.objects.get_or_create(itrfile=itrfile, FinYear=finyear)
            totalCost = request.POST.get('cost')
            request.session['totalCost'] = totalCost
            if createdmeta:
                itrfilemeta.totalamount = totalCost
                itrfilemeta.save()
            if 'form16_' in y:
                if index <= (noOfForms - 1):
                    pwd = 'password_' + str(index)
                    index += 1
                forms = ItrForm16.objects.create(ItrMeta=itrfilemeta, finyear=finyear, form16=file,
                                                 password=request.POST.get(pwd, None))
                forms.save()
            if 'panCardUpload' in y:
                itrfilemeta.Pan = file
                itrfilemeta.PanStatus = True
                itrfilemeta.save()
            if 'otherIncome' in y:
                itrfilemeta.OtherIncome = file
                itrfilemeta.OtherIncomeStatus = True
                itrfilemeta.save()
            if 'deductionUpload' in y:
                itrfilemeta.Deduction = file
                itrfilemeta.DeductionStatus = True
                itrfilemeta.save()
            up = userprogressitr.objects.get(user=request.user)
            up.step = '2'
            up.save()
            request.session['message'] = 'Form 16 uploaded. Now, enter bank details'
            request.session['header'] = 'Upload Successful'
        return redirect('/itr/BankDetails')
    else:
        up = userprogressitr.objects.get(user=request.user)
        up.firstvisit = False
        up.step = '1'
        up.save()
        message = request.session['message']
        header = request.session['header']
        return render(request, 'mudramantri/page-file-itr.html', {'message': message, 'header': header})


@login_required(login_url='/login/')
def bankDetails(request):
    if request.method == 'POST':
        acno = request.POST.get('bankAccount')
        ifsc = request.POST.get('ifscCode')
        other = request.POST.get('otherInfo')
        user = request.user
        itrfile, createdfile = ItrFile.objects.get_or_create(user=user)
        itrfile.AcNo = acno
        itrfile.IfscCode = ifsc
        itrfile.OtherInfo = other
        itrfile.save()
        up = userprogressitr.objects.get(user=request.user)
        up.step = '3'
        up.save()
        request.session['message'] = 'Alright, bank details looks fine. We\'re at last step. '
        request.session['header'] = 'Got it!'
        return redirect('/itr/checkout')
    else:
        up = userprogressitr.objects.get(user=request.user)
        up.step = '2'
        up.firstvisit = False
        up.save()
        message = request.session['message']
        header = request.session['header']
        return render(request, 'mudramantri/page-itr-docs-cloud.html', {'message': message, 'header': header})


@login_required(login_url='/login/')
def checkout(request):
    noOfForms = request.session.get('noOfForms', None)
    total = request.session.get('totalCost', None)
    if request.method == 'POST':
        itrfile, created = ItrFile.objects.get_or_create(user=request.user)
        itrfilemeta, createdmeta = ItrFileMeta.objects.get_or_create(itrfile=itrfile)
        itrfilemeta.PaymentStatus = True
        itrfilemeta.save()
        cp = userprogressitr.objects.get(user=request.user)
        cp.complete = True
        cp.save()
        return render(request, 'mudramantri/page-itr-dashboard.html',
                      {'message': 'You\'re done! Leave the rest to us. Track your progress here',
                       'header': 'Complete!'})
    else:
        cp = userprogressitr.objects.get(user=request.user)
        cp.step = '3'
        cp.firstvisit = False
        cp.save()
        message = request.session['message']
        header = request.session['header']
        return render(request, 'mudramantri/page-itr-checkout.html',
                      {'total': total, 'noOfForms': noOfForms, 'message': message, 'header': header})


@login_required(login_url='/login/')
def download(request):
    if request.method == 'POST':
        finyear = request.POST.get('finyear')
        doctype = request.POST.get('doctype')
        dct = ''
        if doctype == 'My Documents':
            dot = 'md'
        if doctype == 'ITR-V Documents':
            dot = 'vd'
        if doctype == 'Show All Documents':
            dot = 'ad'
        itrfile = ItrFile.objects.filter(user=request.user)
        if itrfile.count() > 0:
            itrfilemeta = ItrFileMeta.objects.filter(itrfile=itrfile)
            if itrfilemeta.count() > 0:
                form16 = ItrForm16.objects.filter(ItrMeta=itrfilemeta)
                if form16.count() > 0:
                    return render(request, 'mudramantri/page-itr-downloads.html',
                                  {'form16': form16, 'itrfilemeta': itrfilemeta, 'finyear': finyear, 'dot': dot})
                else:
                    return render(request, 'mudramantri/page-itr-downloads.html',
                                  {'itrfilemeta': itrfilemeta, 'finyear': finyear, 'dot': dot})
            else:
                message = 'No files found'
                return render(request, 'mudramantri/page-itr-downloads.html',
                              {'message': message, 'finyear': finyear, 'dot': dot})
    return render(request, 'mudramantri/page-itr-downloads.html', {})


@login_required(login_url='/login/')
def dashboard(request):
    message = request.session['message']
    header = request.session['header']
    itrfile = ItrFile.objects.filter(user=request.user)
    if itrfile.count() > 0:
        itrfilemeta = ItrFileMeta.objects.filter(itrfile=itrfile)
        if itrfilemeta.count() > 0:
            form16 = ItrForm16.objects.filter(ItrMeta=itrfilemeta)
            if form16.count() > 0:
                return render(request, 'mudramantri/page-itr-dashboard.html',
                              {'form16': form16, 'itrfile': itrfilemeta, 'message': message, 'header': header})
            else:
                return render(request, 'mudramantri/page-itr-dashboard.html',
                              {'itrfile': itrfilemeta, 'message': message, 'header': header})
    return render(request, 'mudramantri/page-itr-dashboard.html', {'blank': True, 'message': message, 'header': header})


@login_required(login_url='/login/')
def companydashboard(request):
    if request.method == 'POST':
        nop = request.POST.get('noOfPartners')
        authcap = request.POST.get('authCapital')
        state = request.POST.get('stateName')
        cost = request.POST.get('cost')
        company, createdComp = newcompany.objects.get_or_create(user=request.user)
        company.NoOfPartners = nop
        company.AuthCapital = authcap
        company.Cost = cost
        company.State = state
        company.save()
        up = userprogresscomp.objects.get(user=request.user)
        up.step = '2'
        up.save()
        request.session['messagec'] = 'Give us the proofs needed for DIN/DSC and other formalities'
        request.session['headerc'] = 'Cost Calculated'
        return redirect('/company/docs')
    up = userprogresscomp.objects.get(user=request.user)
    up.firstvisit = False
    up.step = '1'
    up.save()
    message = request.session['messagec']
    header = request.session['headerc']
    return render(request, 'mudramantri/page-companyform-dashboard.html', {'message':message, 'header':header})


@login_required(login_url='/login')
def companydocs(request):
    if request.method == 'POST':
        comp = newcompany.objects.values_list('NoOfPartners', flat=True).filter(user=request.user)
        nop = comp[0]
        company = newcompany.objects.get(user=request.user)
        for key, file in request.FILES.items():
            x = request.FILES[key]
            y = x.field_name
            partn, createpar = partner.objects.get_or_create(comp=company)
            if 'pan' in y:
                partn.PanCard = file
                partn.PanCardStatus = True;
                partn.save()
            if 'afp' in y:
                partn.AddressProof = file
                partn.AddressProofStatus = True
                partn.save()
            if 'photo' in y:
                partn.Photo = file
                partn.PhotoStatus = True
                partn.save()
        up = userprogresscomp.objects.get(user=request.user)
        up.step = '3'
        up.save()
        request.session['messagec'] = 'Alright, We have recieved your docs too. We\'re at last step. '
        request.session['headerc'] = 'Got it!'
        return redirect('mudramantri/page-companyform-checkout.html')
    else:
        comp = newcompany.objects.values_list('NoOfPartners', flat=True).filter(user=request.user)
        if comp.count() > 0:
            nop = comp[0]
            up = userprogresscomp.objects.get(user=request.user)
            up.step = '2'
            up.firstvisit = False
            up.save()
            message = request.session['messagec']
            header = request.session['headerc']
            return render(request, 'mudramantri/page-companyform-docs.html', {'nop': nop, 'message':message, 'header':header})
        else:
            request.session['messagec'] = 'First fill these details about your company'
            request.session['headerc'] = 'Missing Details!'
            up = userprogresscomp.objects.get(user=request.user)
            up.step = '1'
            up.save()
            return redirect('/company/dashboard')


@login_required(login_url='/login/')
def companycheckout(request):
    if request.method == 'POST':
        comp = newcompany.objects.get(user=request.user)
        pay, created = payment.objects.get_or_create(newcompany = comp)
        pay.partpayment = True
        pay.save()
        cp = userprogresscomp.objects.get(user=request.user)
        cp.complete = True
        cp.save()
        request.session['messagec'] = 'Relax and let us take care of the rest. Track your progress here!'
        request.session['headerc'] = 'Payment accepted!'
        return redirect('/company/progress')
    cp = userprogresscomp.objects.get(user=request.user)
    cp.step = '3'
    cp.firstvisit = False
    cp.save()
    message = request.session['messagec']
    header = request.session['headerc']
    return render(request, 'mudramantri/page-companyform-checkout.html', {'message':message, 'header':header})


@login_required(login_url='/login/')
def companyprogress(request):
    if request.method == 'POST':
        message_ret = 'We will get back to you shortly. Meanwhile, try you can also speak to our customer care through live chat or call.'
        fb = feedback()
        fb.name = request.user.username
        fb.question = request.POST.get('question', None)
        fb.step = request.POST.get('step', None)
        fb.save()
        return render(request, 'mudramantri/page-companyform-progress.html', {'message_ret': message_ret})
    comp = newcompany.objects.values_list('Progress').filter(user=request.user)
    progress = comp[0]
    return render(request, 'mudramantri/page-companyform-progress.html', {'progress': progress})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        topic = request.POST.get('topic')
        message = request.POST.get('message')
        email_subject = 'Enquiry for: '+ topic + 'by ' + name
        email_body = message
        send_mail(email_subject, email_body, 'contact@bizkeeda.com',
                  [email], fail_silently=False)
        return render(request,'mudramantri/index.html')
    return render(request, 'mudramantri/page-contact-us.html', {})


@login_required(login_url='/login/')
def itrdecide(request):
    cp = userprogressitr.objects.get(user=request.user)
    request.session['first'] = ''
    request.session['return'] = ''
    request.session['finish'] = ''
    request.session['header'] = ''
    request.session['message'] = ''
    if cp.firstvisit:
        request.session['first'] = True
        request.session['message'] = 'Welcome!'
        request.session[
            'header'] = 'Let\'s start. If you\'re stuck, feel free to use live chat anytime(See chat box at bottom right of screen)'
        return HttpResponseRedirect('/itr/form16')
    if cp.complete:
        request.session['finish'] = True
        request.session['message'] = 'Success'
        request.session['header'] = 'Leave the rest to us! Meanwhile, you can check progress here.'
        return HttpResponseRedirect('/itr/dashboard')
    if cp.step == '1':
        request.session['return'] = True
        request.session['message'] = 'Welcome Back'
        request.session['header'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/itr/form16')
    if cp.step == '2':
        request.session['return'] = True
        request.session['message'] = 'Welcome Back'
        request.session['header'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/itr/BankDetails')
    if cp.step == '3':
        request.session['return'] = True
        request.session['message'] = 'Welcome Back'
        request.session['header'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/itr/checkout')


@login_required(login_url='/login/')
def compdecide(request):
    cp = userprogresscomp.objects.get(user=request.user)
    request.session['firstc'] = ''
    request.session['returnc'] = ''
    request.session['finishc'] = ''
    request.session['headerc'] = ''
    request.session['messagec'] = ''
    if cp.firstvisit:
        request.session['firstc'] = True
        request.session['messagec'] = 'Welcome!'
        request.session[
            'headerc'] = "Let's start. If you're stuck, feel free to use live chat anytime(See chat box at bottom right of screen)"
        return HttpResponseRedirect('/company/dashboard')
    if cp.complete:
        request.session['finishc'] = True
        request.session['messagec'] = 'Success'
        request.session['headerc'] = 'Leave the rest to us! Meanwhile, you can check progress here.'
        return HttpResponseRedirect('/company/progress')
    if cp.step == '1':
        request.session['returnc'] = True
        request.session['messagec'] = 'Welcome Back'
        request.session['headerc'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/company/dashboard')
    if cp.step == '2':
        request.session['returnc'] = True
        request.session['messagec'] = 'Welcome Back'
        request.session['headerc'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/company/docs')
    if cp.step == '3':
        request.session['returnc'] = True
        request.session['messagec'] = 'Welcome Back'
        request.session['headerc'] = 'Let\'s continue from where you left'
        return HttpResponseRedirect('/company/checkout')


def sociallogin(request):
    up, created = UserProfile.objects.get_or_create(user=request.user)
    itrp, created = userprogresscomp.objects.get_or_create(user=request.user)
    compp, created = userprogressitr.objects.get_or_create(user=request.user)
    email = request.user.email
    firstname = request.user.first_name
    lastname = request.user.last_name
    phone = up.phone
    if email in [None, ''] or firstname in [None, ''] or lastname in [None, ''] or phone in [None, '']:
        return redirect('extrainfo')
    else:
        return HttpResponseRedirect('/index')

def privacy(request):
    return render(request,'mudramantri/page-terms-privacy.html')

@login_required(login_url='/login/')
def extrainfo(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        phone = request.POST.get('phone',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        user = User.objects.get(username = request.user.username)
        user_email = user.email
        user_firstname = user.first_name
        user_lastname = user.last_name
        if user_email in [None, ''] and email is not None:
            user.email = email
        if user_firstname in [None,''] and firstname is not None:
            user.first_name = firstname
        if user_lastname in [None, ''] and lastname is not None:
            user.last_name = lastname
        user.save()
        if phone is not None:
            up = UserProfile.objects.get(user=user)
            up.phone = phone
            up.save()
        next = request.GET.get('next', None)
        if next is not None:
            return redirect(next)
        else:
            return HttpResponseRedirect('/index')
    return render(request,'mudramantri/page-welcome.html')


def require_email(request):
    if request.method == 'POST':
        email = request.POST.get('email',None)
        phone = request.POST.get('phone',None)
        firstname = request.POST.get('firstname',None)
        lastname = request.POST.get('lastname',None)
        user = User.objects.get(username = request.user.username)
        if user.email is None and email is not None:
            user.email = email
        if user.first_name is None and firstname is not None:
            user.first_name = firstname
        if user.last_name is None and lastname is not None:
            user.last_name = lastname
        user.save()
        if phone is not None:
            up, created = UserProfile.objects.get_or_create(user=request.user, key_expires = django.utils.timezone.datetime.now())
            up.phone = phone
            up.save()
        up = userprogressitr(user=user)
        cp = userprogresscomp(user=user)
        up.save()
        cp.save()
        backend = request.session['partial_pipeline']['backend']
        return redirect('social:complete', backend=backend)
    else:
        return render_to_response('mudramantri/page-welcome.html', {}, RequestContext(request))

