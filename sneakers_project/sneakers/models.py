from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.conf import settings

from cloudinary_storage.storage import MediaCloudinaryStorage


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Sneaker(models.Model):
    category = models.ForeignKey(
        Category, related_name="sneakers", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(
        upload_to="uploads/", blank=True, null=True, storage=MediaCloudinaryStorage()
    )
    thumbnail = models.ImageField(
        upload_to="uploads/", blank=True, null=True, storage=MediaCloudinaryStorage()
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image(self):
        if self.image:
            url = self.image.url
            if url.startswith("http"):
                return url
            return url
        return ""

    def get_thumbnail(self):
        if self.thumbnail:
            url = self.thumbnail.url
            if url.startswith("http"):
                return url
            return url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                url = self.thumbnail.url
                if url.startswith("http"):
                    return url
                return url
            else:
                return ""

    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
