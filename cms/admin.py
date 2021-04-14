from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):
    # Высвечивает параметры в главном меню
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    # Преобразует параметр в ссылку
    list_display_links = ('cms_title',)
    # Позволяет менять параметры в главном меню
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'cms_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, img):
        if img.cms_img:
            return mark_safe(f'<img src="{ img.cms_img.url }" width="80px"')
        else:
            return 'Нет картинки'

    get_img.short_description = 'Картинка'

admin.site.register(CmsSlider, CmsAdmin)