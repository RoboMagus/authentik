# Generated by Django 5.0.10 on 2025-01-13 18:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_flows", "0027_auto_20231028_1424"),
        ("authentik_stages_invitation", "0008_alter_invitation_expires"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name="invitation",
            index=models.Index(fields=["expires"], name="authentik_s_expires_96f4b8_idx"),
        ),
        migrations.AddIndex(
            model_name="invitation",
            index=models.Index(fields=["expiring"], name="authentik_s_expirin_4f8f35_idx"),
        ),
        migrations.AddIndex(
            model_name="invitation",
            index=models.Index(
                fields=["expiring", "expires"], name="authentik_s_expirin_4f8096_idx"
            ),
        ),
    ]
