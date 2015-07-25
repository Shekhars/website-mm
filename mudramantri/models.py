from django.db import models
from django.contrib.auth.models import User
from zinnia.models_bases import entry
import django.utils.timezone
# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['media', instance.ItrMeta.itrfile.user.username, filename])


def content_file_user(instance, filename):
    return '/'.join(['media', instance.itrfile.user.username, filename])


def content_filecomp_name(instance, filename):
    return '/'.join(['media', instance.comp.user.username, filename])


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    service_type = models.BooleanField(blank=True, default=False)
    phone = models.CharField(max_length=10)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    class Meta:
        verbose_name_plural = u'User profiles'


class ItrFile(models.Model):
    user = models.OneToOneField(User)
    AcNo = models.CharField(max_length=20, blank=True)
    IfscCode = models.CharField(max_length=20, blank=True)
    OtherInfo = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = u'ITR File Info'


class ItrFileMeta(models.Model):
    itrfile = models.ForeignKey(ItrFile)
    FinYear = models.CharField(max_length=7)
    totalamount = models.CharField(max_length=10, blank=True)
    Pan = models.FileField(upload_to=content_file_user, blank=True)
    PanStatus = models.BooleanField(default=False)
    OtherIncome = models.FileField(upload_to=content_file_user, blank=True)
    OtherIncomeStatus = models.BooleanField(default=False)
    Deduction = models.FileField(upload_to=content_file_user, blank=True)
    DeductionStatus = models.BooleanField(default=False)


class ItrForm16(models.Model):
    ItrMeta = models.ForeignKey(ItrFileMeta)
    finyear = models.CharField(max_length=7, blank=True)
    form16 = models.FileField(blank=True, upload_to=content_file_name)
    password = models.CharField(blank=True, max_length=50)
    UploadedOn = models.DateTimeField(default=django.utils.timezone.datetime.now())
    ItrV = models.FileField(upload_to=content_file_name, blank=True)
    ItrvStatus = models.BooleanField(default=False)
    PaymentStatus = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = u'Form 16'


class newcompany(models.Model):
    user = models.ForeignKey(User)
    NoOfPartners = models.IntegerField(blank=True, default=2)
    AuthCapital = models.CharField(max_length=300)
    State = models.CharField(max_length=120)
    Cost = models.CharField(max_length=100)
    Progress = models.IntegerField(default=1)


class partner(models.Model):
    comp = models.ForeignKey(newcompany)
    PanCard = models.FileField(upload_to=content_filecomp_name)
    PanCardStatus = models.BooleanField(default=False)
    AddressProof = models.FileField(upload_to=content_filecomp_name)
    AddressProofStatus = models.BooleanField(default=False)
    Photo = models.FileField(upload_to=content_filecomp_name)
    PhotoStatus = models.BooleanField(default=False)


class payment(models.Model):
    comp = models.OneToOneField(newcompany)
    partpayment = models.BooleanField(default=False)
    partpaymentId = models.CharField(max_length=100, null=True)
    partpaymentdate = models.DateTimeField(blank=True)
    fullpayment = models.BooleanField(default=False)
    fullpaymentstatus = models.CharField(max_length=100, null=True)
    fullpaymentdate = models.DateTimeField(blank=True)


class feedback(models.Model):
    name = models.CharField(max_length=100)
    question = models.TextField(blank=True)
    step = models.CharField(max_length=10)


class userprogressitr(models.Model):
    user = models.OneToOneField(User)
    firstvisit = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)
    step = models.CharField(default='0', max_length=2)

class userprogresscomp(models.Model):
    user = models.OneToOneField(User)
    firstvisit = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)
    step = models.CharField(default='0', max_length=2)


