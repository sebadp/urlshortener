from django.db import models
import secrets
import requests
from bs4 import BeautifulSoup


class ShortenedURL(models.Model):
    short_code = models.CharField(max_length=8, unique=True)
    long_url = models.URLField()
    title = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Generate a unique short code for the URL
        while not self.short_code:
            code = secrets.token_urlsafe(6)[:8]
            if not ShortenedURL.objects.filter(short_code=code).exists():
                self.short_code = code

        # Crawl the website and retrieve its title
        response = requests.get(self.long_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            self.title = title_tag.string.strip()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} <- From : {self.long_url}"
