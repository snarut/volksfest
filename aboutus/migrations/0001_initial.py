# Generated by Django 3.2.5 on 2021-08-03 07:48

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=300)),
                ('review_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AboutusPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_title', models.CharField(default='เกี่ยวกับเรา', max_length=100)),
                ('hero_text', wagtail.core.fields.RichTextField()),
                ('first_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_image', to='wagtailimages.image')),
                ('second_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_image', to='wagtailimages.image')),
                ('third_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='third_image', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
