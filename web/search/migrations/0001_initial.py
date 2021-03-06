# Generated by Django 2.2 on 2019-04-24 10:04

from django.db import migrations, models
import django.db.models.deletion
import libs.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Executable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_path', models.TextField()),
                ('path', models.TextField(unique=True)),
                ('strings', models.TextField()),
                ('meta', libs.field.JSONField(default=dict)),
                ('libraries', libs.field.JSONField(default=dict)),
                ('imports', libs.field.JSONField(default=dict)),
                ('exports', libs.field.JSONField(default=dict)),
                ('segments', libs.field.JSONField(default=dict)),
                ('entries', libs.field.JSONField(default=dict)),
                ('created', models.DateField()),
                ('modified', models.DateField()),
                ('added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MachO',
            fields=[
                ('executable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='search.Executable')),
                ('classdump', models.TextField()),
                ('classes', libs.field.JSONField(default=dict)),
                ('rpaths', libs.field.JSONField(default=dict)),
                ('ent', libs.field.JSONField(default={})),
                ('ent_str', models.TextField()),
                ('ent_keys', libs.field.JSONField(default=[])),
                ('cs_flags', models.IntegerField(default=0)),
                ('cs_flags_str', models.TextField()),
                ('lv', models.BooleanField(default=False)),
                ('signed', models.BooleanField(default=False)),
                ('apple', models.BooleanField(default=False)),
                ('codesign', models.TextField()),
                ('info_plist', libs.field.JSONField(default=dict)),
                ('info_plist_str', models.TextField()),
            ],
            bases=('search.executable',),
        ),
        migrations.CreateModel(
            name='PE',
            fields=[
                ('executable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='search.Executable')),
                ('version', libs.field.JSONField(default=dict)),
            ],
            bases=('search.executable',),
        ),
    ]
