# Generated by Django 4.2 on 2023-04-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0006_alter_profile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='followed_by', to='dwitter.profile'),
        ),
    ]