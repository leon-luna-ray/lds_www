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
    URLBlock,
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


class TitleWithTextBlock(StructBlock):
    title = CharBlock(required=False)
    text = TextBlock()


class ImageWithTextBlock(TitleWithTextBlock):
    """
    Image and text
    """
    image = ImageChooserBlock()


class LinkCardBlock(StructBlock):
    link = StreamBlock(
        [
            ('page_link', PageChooserBlock(
                required=False,
                icon='home',
            )),
            ('external_link', URLBlock(
                required=False,
                icon='link',
            )),
        ],
        max_num=1,
        required=True,
    )
    title = CharBlock()
    text = TextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        template = '_blocks/link_card_blk.html'


class LinkCardsBlock(StructBlock):
    link_cards = StreamBlock(
        [
            ('card', LinkCardBlock())
        ],
        block_counts={
            'card': {'min_num': 2}
        }
    )

    class Meta:
        template = '_blocks/link_cards_blk.html'

class LinkListItemBlock(StructBlock):
    link = StreamBlock(
        [
            ('page_link', PageChooserBlock(
                required=False,
                icon='home',
            )),
            ('external_link', URLBlock(
                required=False,
                icon='link',
            )),
        ],
        max_num=1,
        required=True,
    )
    title = CharBlock()
    text = RichTextBlock(required=False)
    image = ImageChooserBlock()

    class Meta:
        template = '_blocks/list_list_item_blk.html'


class LinkListBlock(StructBlock):
    intro = RichTextBlock(required=False)
    list_items = StreamBlock(
        [
            ('item', LinkListItemBlock())
        ],
        block_counts={
            'item': {'min_num': 1}
        }
    )

    class Meta:
        template = '_blocks/link_list_blk.html'


class ImageWithTextToutBlock(StructBlock):
    title = CharBlock(required=False)
    subtitle = CharBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()
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


class ContactInfoBlock(StructBlock):
    intro = RichTextBlock()
    text_title = CharBlock()
    text = RichTextBlock()
    list_title = CharBlock()
    list = StreamBlock([
        ('item', TitleWithTextBlock())
    ],
        block_counts={
        'item': {'min_num': 7, 'max_num': 7}
    })
    
    class Meta:
        template = '_blocks/contact_info.html'


class CallToActionBlock(ImageWithTextBlock):
    link = StreamBlock(
        [
            ('page_link', PageChooserBlock(
                required=False,
                icon='home',
            )),
            ('external_link', URLBlock(
                required=False,
                icon='link',
            )),
        ],
        max_num=1,
        required=True,
    )
    reverse = BooleanBlock(required=False)

    class Meta:
        template = '_blocks/cta_blk.html'


class BodySectionBlock(StreamBlock):
    """
    Stream block providing all page builder components for main body
    """
    free_text = FreeTextBlock()
    image_text_tout = ImageWithTextToutBlock()
    link_cards_block = LinkCardsBlock()
    three_column_tout = ThreeColumnToutBlock()
    call_to_action = CallToActionBlock()
    contact_info = ContactInfoBlock()
    link_list = LinkListBlock()

    class Meta:
        template = '_blocks/body_section_blk.html'
