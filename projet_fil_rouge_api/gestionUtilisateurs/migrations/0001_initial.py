# Generated by Django 4.1.3 on 2022-11-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TRole",
            fields=[
                ("code_role", models.AutoField(primary_key=True, serialize=False)),
                ("lib_role", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "t_role",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TUtilisateur",
            fields=[
                (
                    "code_utilisateur",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "nom_utilisateur",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "prenom_utilisateur",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "couleur_fond_utilisateur",
                    models.IntegerField(blank=True, null=True),
                ),
                ("date_cde_utilisateur", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "t_utilisateur",
                "managed": False,
            },
        ),
    ]
