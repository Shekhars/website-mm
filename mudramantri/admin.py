from django.contrib import admin
from mudramantri.models import *
from Blog.models import *
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
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
