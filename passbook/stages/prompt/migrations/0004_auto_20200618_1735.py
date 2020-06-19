# Generated by Django 3.0.7 on 2020-06-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_stages_prompt", "0003_auto_20200615_1641"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt",
            name="type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("username", "Username"),
                    ("email", "Email"),
                    ("password", "Password"),
                    ("number", "Number"),
                    ("checkbox", "Checkbox"),
                    ("data", "Date"),
                    ("data-time", "Date Time"),
                    ("separator", "Separator"),
                    ("hidden", "Hidden"),
                    ("static", "Static"),
                ],
                max_length=100,
            ),
        ),
    ]
