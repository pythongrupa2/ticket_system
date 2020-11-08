# Generated by Django 3.1.2 on 2020-11-07 17:18

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='User Name')),
                ('user_surname', models.CharField(max_length=50, verbose_name='User Surname')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=50, verbose_name='Type of Payment')),
                ('date_payment', models.DateField(verbose_name='Date of Payment')),
                ('date_payment_return', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=10, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_login', models.CharField(max_length=50, verbose_name='User Login')),
                ('user_email', models.CharField(max_length=100, verbose_name='User Email')),
                ('user_phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='price_ticket',
            field=models.DecimalField(decimal_places=10, max_digits=1000),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('1', 'Standard'), ('2', 'VIP')], max_length=10)),
                ('date_reservation', models.DateField(blank=True, null=True)),
                ('date_purchase', models.DateField()),
                ('date_ticket_return', models.DateField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.operator')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.payment')),
                ('user_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.user')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='user_payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.user'),
        ),
    ]
