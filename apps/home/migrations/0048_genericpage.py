# Generated by Django 4.1.2 on 2022-11-14 17:56

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_employee_image'),
        ('wagtailcore', '0077_alter_revision_user'),
        ('home', '0047_alter_aboutpage_reverse_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('reverse_header', models.BooleanField(default=False)),
                ('content', wagtail.fields.StreamField([('sections', wagtail.blocks.StreamBlock([('free_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=['h3', 'h4', 'h5', 'bold', 'underline', 'italic', 'ol', 'ul', 'hr', 'lead-in', 'link', 'button-link', 'link-list', 'document-link', 'image', 'embed'], required=True))])), ('image_text_tout', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('reverse', wagtail.blocks.BooleanBlock(required=False))])), ('link_cards_block', wagtail.blocks.StructBlock([('link_cards', wagtail.blocks.StreamBlock([('card', wagtail.blocks.StructBlock([('link', wagtail.blocks.StreamBlock([('page_link', wagtail.blocks.PageChooserBlock(icon='home', required=False)), ('external_link', wagtail.blocks.URLBlock(icon='link', required=False))], max_num=1, required=True)), ('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], block_counts={'card': {'min_num': 2}}))])), ('three_column_tout', wagtail.blocks.StructBlock([('intro', wagtail.blocks.TextBlock(required=False)), ('columns', wagtail.blocks.StreamBlock([('column', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], block_counts={'column': {'max_num': 3, 'min_num': 3}}))]))]))], null=True, use_json_field=False)),
                ('header_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage')),
                ('preview_thumbnail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.accessibleimage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
