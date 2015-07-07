__author__ = 'shesharma'
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS, FieldError
from mudramantri.models import UserProfile
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings

class RegForm(forms.Form):
    email = forms.EmailField(error_messages={'required': 'Please enter your Email ID'})
    password=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    phone= forms.CharField(label="Mobile Number",max_length=10)
    email.widget.attrs['class']='form-control'
    email.widget.attrs['required']=True
    phone.widget.attrs['class']='form-control'
    phone.widget.attrs['required']=True
    password.widget.attrs['class']='form-control'
    password.widget.attrs['required']=True
    password2.widget.attrs['class']='form-control'
    password2.widget.attrs['required']=True

    def clean(self):
        cleaned_data = super(RegForm,self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError({'email':'Incorrect Email ID.(Hint: abc@domain.com)'})
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            print 'test!'
        else:
            raise forms.ValidationError({'email':'Email already registered. Please login or use another email.'})
        if password!=password2:
            raise ValidationError({'password2':'Passwords do not match. Enter again.'})
        if len(password)<8:
            raise ValidationError({'password':'Password should be at least 8 character long'})
        return self.cleaned_data

    def invalid_code(self):
        expire = True
        if expire:
            raise ValidationError('Activation link expired! Please register again.')



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=True)
    username.widget.attrs['required']=True
    password.widget.attrs['required']=True
    username.widget.attrs['class']='form-control'
    password.widget.attrs['class']='form-control'
    def clean(self):
        """clean method for remember_me """
        cleaned_data = super(LoginForm,self).clean()
        remember_me = cleaned_data.get('remember_me')
        if not remember_me:
          settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
        else:
          settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        username = cleaned_data.get('username')
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Incorrect Email or Password.')
        return self.cleaned_data


