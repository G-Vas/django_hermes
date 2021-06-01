# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumberField


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    tagline = models.TextField("Краткое описсание", max_length=400, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна', default=20.0)
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    slug = models.SlugField(max_length=200, default='', unique=True)
    # features = models.ManyToManyField('ProductFeatures', related_name='features', verbose_name='Характеристики')

    def __str__(self):
        return self.title


class Photos(models.Model):
    """Изображеия"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="seed_photos/")
    post = models.ForeignKey(Post, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображеия"


class ProductFeatures(models.Model):
    feature_name = models.CharField(verbose_name='Имя ключа для категории', max_length=50)
    value = models.CharField(max_length=255, verbose_name='Значение')
    post = models.ManyToManyField(Post, related_name="feature")

    def __str__(self):
        return f"имя характеристики {self.feature_name} Значение - {self.value}"


class CallRequests(models.Model):
    first_name = models.CharField(verbose_name="Ім'я клієна", max_length=50)
    last_name = models.CharField(verbose_name="Прізвище клієна", max_length=50)
    phone = models.CharField(verbose_name="Телефон", null=False, blank=False, max_length=12)
    question = models.TextField(verbose_name="Запитання", null=True, blank=True)

    def __str__(self):
        return f"Ім'я {self.first_name}/ Прізвище {self.last_name}/ номер {self.phone}"
