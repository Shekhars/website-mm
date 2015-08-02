__author__ = 'Shekhar Sharma'

from social.pipeline.partial import partial
from django.shortcuts import render, redirect

@partial
def other_info(strategy, details, user=None, is_new=False, *args, **kwargs):
    if is_new or not details.get('email'):
        return redirect('require_email')
    else:
        return
