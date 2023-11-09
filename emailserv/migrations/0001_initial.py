# Generated by Django 4.2.7 on 2023-11-09 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailDistribution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(verbose_name="Время рассылки")),
                (
                    "period",
                    models.CharField(
                        choices=[
                            ("1", "Раз в день"),
                            ("2", "Раз в неделю"),
                            ("3", "Раз в месяц"),
                        ],
                        default="1",
                        verbose_name="Период рассылки",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        default=1, verbose_name="Статус рассылки"
                    ),
                ),
                (
                    "emails",
                    models.ManyToManyField(
                        to="users.user", verbose_name="Пользователи"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Тема письма")),
                ("body", models.TextField(verbose_name="Содержание письма")),
            ],
            options={
                "verbose_name": "Письмо",
                "verbose_name_plural": "Письма",
            },
        ),
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(
                        default=None, verbose_name="Дата и время последней попытки"
                    ),
                ),
                (
                    "response",
                    models.BooleanField(
                        default=False, verbose_name="Ответ почтового сервера"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="emailserv.emaildistribution",
                        verbose_name="Статус рассылки",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="emaildistribution",
            name="message",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="emailserv.message",
                verbose_name="Сообщение",
            ),
        ),
    ]