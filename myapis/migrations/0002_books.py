# Generated by Django 3.2.5 on 2021-07-08 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapis.student')),
            ],
        ),
    ]
