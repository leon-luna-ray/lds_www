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


class ImageWithTextBlock(StructBlock):
    """
    Image and text
    """
    title = CharBlock(required=False)
    text = TextBlock()
    image = ImageChooserBlock(required=False)


class LinkBlock(StructBlock):
    """
    Link with text title
    """
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
        required=False,
    )
    title = CharBlock(required=False)


class LinkWithTextBlock(LinkBlock):
    """
    Link with text title amd description
    """
    text = RichTextBlock(required=False, features=['bold', 'italic', ])


class LinkWithImageBlock(LinkWithTextBlock):
    """
    Link with text title, description and image
    """
    image = ImageChooserBlock(required=False)


class LinkCardBlock(StructBlock):
    """
    Stream block providing all page builder components for main body
    """
    title = CharBlock()
    text = TextBlock(required=False)
    image = ImageChooserBlock()
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
    
    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        for block in value['link']:
                if block.block_type not in 'page_link':
                    context['link_url'] = block
                else:
                    context['link_url'] = block.value.url
        return context

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
    link_cards_block = LinkCardsBlock()
    three_column_tout = ThreeColumnToutBlock()

    class Meta:
        template = '_blocks/body_section_blk.html'
