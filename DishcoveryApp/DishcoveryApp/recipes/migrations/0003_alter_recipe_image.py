# Generated by Django 5.1.3 on 2024-12-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_remove_recipe_created_at_remove_recipe_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="recipe_images/"),
        ),
    ]
