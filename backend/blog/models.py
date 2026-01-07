from django import forms
from django.db import models
from datetime import date

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet

from wagtail_headless_preview.models import HeadlessPreviewMixin

from taggit.models import TaggedItemBase
from modelcluster.models import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager


class HomePage(HeadlessPreviewMixin, Page):
    """
    Home page model - add preview support.
    Assumes Vue route: "/"
    """
    intro = RichTextField(blank=True, features=['h2', 'bold', 'italic', 'link'])
    # Add other fields as needed

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        # Add other panels
    ]

    preview_url = "/"


class BlogIndexPage(HeadlessPreviewMixin, Page):
    """
    Blog listing index - already had mixin, updated preview_url.
    Assumes Vue route: "/blog/"
    """
    description = RichTextField(blank=True, features=['h2', 'bold', 'italic', 'link'])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    preview_url = "/blog/"


class BlogTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPostPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPostPage(HeadlessPreviewMixin, Page):
    """
    Blog post detail - already had mixin, updated preview_url.
    Assumes Vue route: "/blog/{slug}/"
    """
    date = models.DateField("Post date", default=date.today)
    intro = RichTextField(blank=True, features=['h2', 'bold', 'italic', 'link'])
    body = RichTextField(blank=True, features=['h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'image', 'embed'])
    authors = ParentalManyToManyField('blog.Author', blank=True)
    tags = ClusterTaggableManager(through=BlogTag, blank=True)

    content_panels = Page.content_panels + [
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('date'),
        FieldPanel('intro'),      
        FieldPanel('body'),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

    preview_url = "/blog/preview/"  # Preview route in Vue (with token param)


class BlogPageImageGallery(Orderable):
    page = ParentalKey(
        BlogPostPage, on_delete=models.CASCADE, related_name='gallery_images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return self.name
    

class TagIndexPage(HeadlessPreviewMixin, Page):
    """
    Tag listing page - ADDED mixin + preview_url.
    Assumes Vue route: "/tags/" or "/tags/{tag}/"
    """
    description = RichTextField(
        blank=True, 
        features=['h2', 'bold', 'italic', 'link']
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]

    preview_url = "/tags/"  # Adjust if tag-specific