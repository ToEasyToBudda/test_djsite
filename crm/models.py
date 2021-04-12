from django.db import models


class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class CommentCrm(models.Model):
    cmmnt_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    cmmnt_text  = models.TextField(verbose_name='Текст комментария')
    cmmnt_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cmmnt_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
