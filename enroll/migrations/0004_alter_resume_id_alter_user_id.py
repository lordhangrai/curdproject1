# Generated by Django 4.1.4 on 2024-06-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_resume_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
