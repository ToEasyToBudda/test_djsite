# Generated by Django 3.1.7 on 2021-04-12 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210412_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmmnt_text', models.TextField(verbose_name='Текст комментария')),
                ('cmmnt_dt', models.DateTimeField(auto_now=True)),
                ('cmmnt_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментариев',
            },
        ),
    ]
