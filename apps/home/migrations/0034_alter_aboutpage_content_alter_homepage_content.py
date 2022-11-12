# Generated by Django 4.1.2 on 2022-11-11 19:42

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_aboutpage_content_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='content',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StreamBlock([('free_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=['h3', 'h4', 'h5', 'bold', 'underline', 'italic', 'ol', 'ul', 'hr', 'lead-in', 'link', 'button-link', 'link-list', 'document-link', 'image', 'embed'], required=True))])), ('image_text_tout', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('reverse', wagtail.blocks.BooleanBlock(required=False))])), ('link_card_block', wagtail.blocks.StreamBlock([('link_card', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], min_num=2))])), ('three_column_tout', wagtail.blocks.StructBlock([('intro', wagtail.blocks.TextBlock(required=False)), ('columns', wagtail.blocks.StreamBlock([('column', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], block_counts={'column': {'max_num': 3, 'min_num': 3}}))]))]))], null=True, use_json_field=None),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StreamBlock([('free_text', wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=['h3', 'h4', 'h5', 'bold', 'underline', 'italic', 'ol', 'ul', 'hr', 'lead-in', 'link', 'button-link', 'link-list', 'document-link', 'image', 'embed'], required=True))])), ('image_text_tout', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('reverse', wagtail.blocks.BooleanBlock(required=False))])), ('link_card_block', wagtail.blocks.StreamBlock([('link_card', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic'], required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], min_num=2))])), ('three_column_tout', wagtail.blocks.StructBlock([('intro', wagtail.blocks.TextBlock(required=False)), ('columns', wagtail.blocks.StreamBlock([('column', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], block_counts={'column': {'max_num': 3, 'min_num': 3}}))]))]))], null=True, use_json_field=None),
        ),
    ]
