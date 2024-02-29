from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth import get_user_model

# Create your models here.
from django.utils.text import slugify

User = get_user_model()


class CategoryPost(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="Categorie")
    cat_slug = models.SlugField(max_length=100, blank=True, editable=True)
    color = ColorField(default='#0D6EFD', unique=True)

    class Meta:
        verbose_name = "Catégorie"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.cat_slug:
            self.cat_slug = slugify(self.title)

        super().save(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    category = models.ManyToManyField(CategoryPost)
    published = models.BooleanField(default=False, verbose_name="Publié")
    image = models.ImageField(upload_to="images")
    content = models.TextField(blank=True, verbose_name='Contenu')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        return f"Par {self.author.first_name} {self.author.last_name}" if self.author else "auteur inconnu"

    # def get_absolute_url(self):
    #     return reverse('posts:home')
