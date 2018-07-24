from django.contrib import admin

import application.models as models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'magazine', 'science', 'authors', 'grade')
    list_filter = ('magazine', 'science',)


class MagazineAdmin(admin.ModelAdmin):
    list_display = ('number', 'mouth', 'year',)
    list_filter = ('year',)

class SpecialMagazineAdmin(admin.ModelAdmin):
    list_display = ('number', 'mouth', 'year',)
    list_filter = ('year',)

class ScienceAdmin(admin.ModelAdmin):
    list_display = ('name','ordering')


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Magazine, MagazineAdmin)
#admin.site.register(models.SpecialMagazine, SpecialMagazineAdmin)
admin.site.register(models.Science, ScienceAdmin)
admin.site.register(models.Feedback)
