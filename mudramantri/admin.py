from django.contrib import admin
from mudramantri.models import  UserProfile, ItrFile,ItrFileMeta,ItrForm16, newcompany, partner, payment,feedback, userprogressitr, userprogresscomp
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ItrFile)
admin.site.register(ItrFileMeta)
admin.site.register(ItrForm16)
admin.site.register(payment)
admin.site.register(partner)
admin.site.register(newcompany)
admin.site.register(feedback)
admin.site.register(userprogressitr)
admin.site.register(userprogresscomp)
