from django.contrib import admin

import sitesettings.models as models


class SettingsAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False



#admin.site.register(models.ActualArticles, SettingsAdmin)
admin.site.register(models.MainPage, SettingsAdmin)
admin.site.register(models.ReqPage, SettingsAdmin)
#admin.site.register(models.PaymentPage, SettingsAdmin)
#admin.site.register(models.SpecialPage, SettingsAdmin)

