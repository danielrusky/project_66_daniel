# Generated by Django 4.2.7 on 2023-11-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_message"),
        ("emailserv", "0002_emailserv_alter_logs_status_delete_emaildistribution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailserv",
            name="emails",
            field=models.ManyToManyField(to="users.user"),
        ),
    ]