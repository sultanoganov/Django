# Generated by Django 2.1.5 on 2019-03-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('courses_quantity', models.PositiveIntegerField()),
                ('student_description', models.TextField()),
                ('students_money', models.DecimalField(decimal_places=2, max_digits=6)),
                ('passport', models.CharField(max_length=50)),
                ('identity_number', models.CharField(max_length=20)),
            ],
        ),
    ]
