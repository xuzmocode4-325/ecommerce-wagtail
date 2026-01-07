# backend/blog/api.py
from ninja import Router
from typing import List
from .models import BlogPostPage, BlogIndexPage, Author
from .schemas import BlogPostPageSchema, BlogIndexPageSchema, AuthorSchema

router = Router(tags=["Blog"])


@router.get("/posts/", response=List[BlogPostPageSchema])
def list_blog_posts(request):
    """List all published blog posts"""
    return BlogPostPage.objects.live().order_by('-date')


@router.get("/posts/{slug}", response=BlogPostPageSchema)
def get_blog_post(request, slug: str):
    """Get a specific blog post by slug"""
    post = BlogPostPage.objects.live().filter(slug=slug).first()
    if not post:
        return 404, {"detail": "Blog post not found"}
    return post


@router.get("/index/", response=BlogIndexPageSchema)
def get_blog_index(request):
    """Get the blog index page"""
    index = BlogIndexPage.objects.live().first()
    if not index:
        return 404, {"detail": "Blog index not found"}
    return index


@router.get("/authors/", response=List[AuthorSchema])
def list_authors(request):
    """List all authors"""
    return Author.objects.all()