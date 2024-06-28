# Generated by Django 5.0.6 on 2024-06-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_service_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='service',
            name='stylists',
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=1, verbose_name='Booking date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('B', 'Blowout'), ('WCS', 'Womens Cut & Style'), ('WMC', 'Womens Master Cut & Style'), ('MCW', 'Mens Wash & Scissor Cut'), ('LMC', 'Lengthy Master Color'), ('BMC', 'Buzz Master Color'), ('F', 'Fix Your Face'), ('FF', 'Face First')], default='B', max_length=3),
        ),
        migrations.AddField(
            model_name='appointment',
            name='stylists',
            field=models.CharField(choices=[('A', 'Annabelle'), ('C', 'Corey'), ('D', 'Devlin'), ('G', 'Giang'), ('S', 'Scott')], default='A', max_length=1),
        ),
    ]
