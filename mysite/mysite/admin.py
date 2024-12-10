from django.contrib import admin


from polls.models import Choice, Question


class MyAdminSite(admin.AdminSite):
    site_header = 'Site Admin'


admin_site = MyAdminSite()
admin_site.register(Question)
admin_site.register(Choice)