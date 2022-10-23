# Generated by Django 4.1.2 on 2022-10-22 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_rename_artise_artiste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='sond_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='musicapp.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
        ),
    ]
