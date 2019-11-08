# Generated by Django 2.2.4 on 2019-08-09 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepost_total_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 8, 9, 10, 24, 17, 549679))),
            ],
        ),
        migrations.AddField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='article.ArticleColumn'),
        ),
    ]
