# Generated by Django 4.1.13 on 2024-08-03 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "role_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("role_name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "role",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "subject_id",
                    models.CharField(max_length=7, primary_key=True, serialize=False),
                ),
                ("subject_name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "subject",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.CharField(max_length=254, unique=True)),
                ("fte_percentage", models.FloatField(blank=True, null=True)),
                ("honorific", models.CharField(blank=True, max_length=50, null=True)),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="admin_user_input.role",
                    ),
                ),
            ],
            options={
                "db_table": "UserProfile",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SubjectInstance",
            fields=[
                ("instance_id", models.AutoField(primary_key=True, serialize=False)),
                ("month", models.IntegerField(blank=True, null=True)),
                ("year", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("enrollments", models.IntegerField(blank=True, null=True)),
                (
                    "subject",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="admin_user_input.subject",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="admin_user_input.userprofile",
                    ),
                ),
            ],
            options={
                "db_table": "subject_instance",
                "managed": True,
            },
        ),
    ]
