# backend/blog/schemas.py
from ninja import ModelSchema
from typing import Optional
from .models import BlogIndexPage, BlogPostPage, Author


class AuthorSchema(ModelSchema):
    class Meta:
        model = Author
        fields = ['id', 'name', 'role', 'image']


class BlogPostPageSchema(ModelSchema):
    authors: Optional[list] = None
    tags: Optional[list] = None
    
    class Meta:
        model = BlogPostPage
        fields = ['id', 'title', 'slug', 'date', 'intro', 'body']


class BlogIndexPageSchema(ModelSchema):
    class Meta:
        model = BlogIndexPage
        fields = ['id', 'title', 'slug', 'description']