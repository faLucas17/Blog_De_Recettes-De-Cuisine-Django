# Generated by Django 5.1.1 on 2024-11-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_alter_article_auteur"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="resume",
            field=models.CharField(max_length=2000),
        ),
    ]
