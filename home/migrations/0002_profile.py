# Generated by Django 3.2.4 on 2021-06-15 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('PURL', models.URLField(max_length=300)),
                ('Website', models.URLField(max_length=300)),
                ('RollNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
