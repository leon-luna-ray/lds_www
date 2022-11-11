# from django.db import models
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
    CharBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    BooleanBlock,
    TextBlock,
)


class FreeTextBlock(StructBlock):
    """
    Simple free-form text block
    """
    content = RichTextBlock(
        required=True,
        features=[
            'h3', 'h4', 'h5', 'bold', 'underline',
            'italic', 'ol', 'ul', 'hr', 'lead-in',
            'link', 'button-link', 'link-list',
            'document-link', 'image', 'embed'])

    class Meta:
        template = '_blocks/free_text_blk.html'


class LinkBlock(StructBlock):
    """
    Link with text title
    """
    link = PageChooserBlock(required=True)
    title = CharBlock(required=False)


class LinkWithTextBlock(LinkBlock):
    """
    Link with text title amd description
    """
    text = RichTextBlock(required=False, features=['bold', 'italic', ])


class ImageWithTextBlock(StructBlock):
    """
    Image and text
    """
    title = CharBlock(required=False)
    text = TextBlock()
    image = ImageChooserBlock(required=False)


class LinkWithImageBlock(LinkWithTextBlock):
    """
    Link with text title, description and image
    """
    image = ImageChooserBlock(required=False)


class LinkCardBlock(StreamBlock):
    """
    Stream block providing all page builder components for main body
    """
    link_card = LinkWithImageBlock(min_num=2)

    class Meta:
        template = '_blocks/link_card_blk.html'


class ImageWithTextToutBlock(StructBlock):
    title = CharBlock()
    text = TextBlock()
    image = ImageChooserBlock(required=False)
    reverse = BooleanBlock(required=False)

    class Meta:
        template = '_blocks/image_text_tout.html'


class ThreeColumnToutBlock(StructBlock):
    """
    Full width three column tout
    """
    intro = TextBlock(required=False)
    columns = StreamBlock(
        [
            ('column', ImageWithTextBlock()),
        ],
        block_counts={
            'column': {'min_num': 3, 'max_num': 3},
        },
    )

    class Meta:
        template = "_blocks/three_column_tout.html"


class BodySectionBlock(StreamBlock):
    """
    Stream block providing all page builder components for main body
    """
    free_text = FreeTextBlock()
    image_text_tout = ImageWithTextToutBlock()
    link_card_block = LinkCardBlock()
    three_column_tout = ThreeColumnToutBlock()

    class Meta:
        template = '_blocks/body_section_blk.html'
