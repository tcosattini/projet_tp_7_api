# Generated by Django 4.1.3 on 2022-12-02 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TClient',
            fields=[
                ('codcli', models.AutoField(primary_key=True, serialize=False)),
                ('genrecli', models.CharField(blank=True, max_length=8, null=True)),
                ('nomcli', models.CharField(max_length=40)),
                ('prenomcli', models.CharField(blank=True, max_length=30, null=True)),
                ('adresse1cli', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse2cli', models.CharField(blank=True, max_length=50, null=True)),
                ('adresse3cli', models.CharField(blank=True, max_length=255, null=True)),
                ('cpcli', models.CharField(blank=True, max_length=5, null=True)),
                ('villecli', models.CharField(blank=True, max_length=50, null=True)),
                ('telcli', models.CharField(blank=True, max_length=10, null=True)),
                ('emailcli', models.TextField(blank=True, null=True)),
                ('portcli', models.CharField(blank=True, max_length=10, null=True)),
                ('newsletter', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TCommunes',
            fields=[
                ('id_commune', models.AutoField(primary_key=True, serialize=False)),
                ('dep', models.PositiveIntegerField(blank=True, db_column='DEP', null=True)),
                ('cp', models.CharField(blank=True, db_column='CP', max_length=5, null=True)),
                ('communes', models.CharField(blank=True, db_column='COMMUNES', max_length=50, null=True)),
            ],
            options={
                'db_table': 't_communes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TConditionnement',
            fields=[
                ('idcondit', models.AutoField(primary_key=True, serialize=False)),
                ('libcondit', models.CharField(blank=True, max_length=50, null=True)),
                ('poidscondit', models.IntegerField(blank=True, null=True)),
                ('prixcond', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('ordreimp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_conditionnement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TDept',
            fields=[
                ('code_dept', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nom_dept', models.CharField(blank=True, max_length=50, null=True)),
                ('ordre_aff_dept', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TDtlcode',
            fields=[
                ('codcde', models.IntegerField(blank=True, null=True)),
                ('qte', models.IntegerField(blank=True, null=True)),
                ('colis', models.IntegerField(blank=True, db_column='Colis', null=True)),
                ('commentaire', models.CharField(blank=True, db_column='Commentaire', max_length=100, null=True)),
                ('id_dtl_commande', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 't_dtlcode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TEnseigne',
            fields=[
                ('id_enseigne', models.AutoField(primary_key=True, serialize=False)),
                ('lb_enseigne', models.CharField(blank=True, max_length=50, null=True)),
                ('ville_enseigne', models.CharField(blank=True, max_length=50, null=True)),
                ('dept_enseigne', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_enseigne',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TEntcde',
            fields=[
                ('codcde', models.AutoField(primary_key=True, serialize=False)),
                ('datcde', models.DateTimeField(blank=True, null=True)),
                ('timbrecli', models.FloatField(blank=True, null=True)),
                ('timbrecde', models.FloatField(blank=True, null=True)),
                ('nbcolis', models.PositiveIntegerField(blank=True, db_column='Nbcolis', null=True)),
                ('cheqcli', models.FloatField(blank=True, null=True)),
                ('idcondit', models.IntegerField(blank=True, null=True)),
                ('cdecomt', models.TextField(blank=True, db_column='cdeComt', null=True)),
                ('barchive', models.IntegerField(blank=True, null=True)),
                ('bstock', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_entcde',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TObjet',
            fields=[
                ('codobj', models.AutoField(primary_key=True, serialize=False)),
                ('libobj', models.CharField(blank=True, max_length=50, null=True)),
                ('tailleobj', models.CharField(blank=True, db_column='Tailleobj', max_length=50, null=True)),
                ('puobj', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('poidsobj', models.DecimalField(blank=True, db_column='Poidsobj', decimal_places=4, max_digits=19, null=True)),
                ('indispobj', models.IntegerField(blank=True, null=True)),
                ('o_imp', models.IntegerField(blank=True, null=True)),
                ('o_aff', models.IntegerField(blank=True, null=True)),
                ('o_cartp', models.IntegerField(blank=True, null=True)),
                ('idcondit', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('o_ordre_aff', models.IntegerField(blank=True, null=True)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 't_objet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPoids',
            fields=[
                ('valmin', models.FloatField(primary_key=True, serialize=False)),
                ('valtimbre', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_poids',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TPoidsv',
            fields=[
                ('valmin', models.FloatField(primary_key=True, serialize=False)),
                ('valtimbre', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_poidsv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRelCond',
            fields=[
                ('idrelcond', models.AutoField(primary_key=True, serialize=False)),
                ('qteobjdeb', models.IntegerField(blank=True, null=True)),
                ('qteobjfin', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_rel_cond',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TRole',
            fields=[
                ('code_role', models.AutoField(primary_key=True, serialize=False)),
                ('lib_role', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 't_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TUtilisateur',
            fields=[
                ('code_utilisateur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_utilisateur', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom_utilisateur', models.CharField(blank=True, max_length=50, null=True)),
                ('couleur_fond_utilisateur', models.IntegerField(blank=True, null=True)),
                ('date_cde_utilisateur', models.DateTimeField(blank=True, null=True)),
                ('last_login', models.DateField(blank=True, null=True)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('is_superuser', models.IntegerField()),
            ],
            options={
                'db_table': 't_utilisateur',
                'managed': False,
            },
        ),
    ]
