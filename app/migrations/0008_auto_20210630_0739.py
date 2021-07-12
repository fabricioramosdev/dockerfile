# Generated by Django 3.2 on 2021-06-30 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20210623_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpfusuario',
            name='cpf',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='app.cpf'),
        ),
        migrations.AlterField(
            model_name='cpfusuario',
            name='usuario',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]