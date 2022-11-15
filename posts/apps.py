"""Posts application module."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Posts application configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    verbose_name = 'Posts'
