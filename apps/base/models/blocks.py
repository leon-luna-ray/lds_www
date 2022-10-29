from wagtail.core.blocks import (
    RichTextBlock,
    StreamBlock,
    StructBlock,
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


class BodySectionBlock(StreamBlock):
    """
    Stream block providing all page builder components for main body
    """
    section = StreamBlock([
        ('free_text', FreeTextBlock())
    ],
        blank=True,
        null=True,
    )
    class Meta:
        template = '_blocks/body_section_blk.html'
