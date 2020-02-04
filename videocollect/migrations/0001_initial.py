# Generated by Django 2.2 on 2020-02-03 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('video', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoEntrenamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_entrenamiento', models.FileField(upload_to='')),
                ('signo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signo', to='videocollect.Signo')),
                ('fecha_hora_subida', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
