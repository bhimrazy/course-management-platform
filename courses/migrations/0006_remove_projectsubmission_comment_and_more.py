# Generated by Django 4.2.9 on 2024-01-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0005_project_time_spent_evaluation_field_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectsubmission",
            name="comment",
        ),
        migrations.AddField(
            model_name="project",
            name="problem_comments_field",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="projectsubmission",
            name="problem_comments",
            field=models.TextField(blank=True),
        ),
    ]