# Generated by Django 2.1.4 on 2018-12-13 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nefarious', '0012_remove_watchtvepisode_transmission_torrent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchTVSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_profile_custom', models.CharField(blank=True, choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-720p-1080p', 'hd-720p-1080p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd')], max_length=500)),
                ('tmdb_season_id', models.IntegerField(unique=True)),
                ('season_number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watch_tv_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nefarious.WatchTVShow')),
            ],
        ),
        migrations.AddField(
            model_name='watchtvepisode',
            name='watch_tv_season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nefarious.WatchTVSeason'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='watchtvseason',
            unique_together={('watch_tv_show', 'season_number')},
        ),
    ]