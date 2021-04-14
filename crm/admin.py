from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Класс для добавления комментария из соответствующей модели к карточке заказа
class Comment(admin.StackedInline):
    model = CommentCrm      # Обязательный параметр
    fields = ('cmmnt_dt', 'cmmnt_text')
    readonly_fields = ('cmmnt_dt',)
    extra = 0


# Класс для кастомизации crm-системы
class OrderAdm(admin.ModelAdmin):
    list_display = ('order_name', 'id', 'order_status', 'order_phone', 'order_dt')
    list_display_links = ('order_name', 'id')
    search_fields = ('order_name', 'id', 'order_phone', 'order_dt')
    list_filter = ('order_status',) # в кордеж с одним элементом в конце нужно поставить запятую
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    # Передача комментария
    inlines = [Comment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
