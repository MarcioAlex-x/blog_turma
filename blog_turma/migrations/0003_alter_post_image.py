# Generated by Django 4.2.3 on 2023-07-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_turma", "0002_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.FileField(blank=True, null=True, upload_to="images/"),
        ),
    ]