from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


# Model for product
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="media/", validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
