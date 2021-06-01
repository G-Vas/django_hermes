from django.contrib import admin
from django.contrib.gis import forms
from mptt.admin import MPTTModelAdmin
from .models import Post, Category, ProductFeatures, Photos, CallRequests
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    tagline = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


# Register your models here.
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Post, form=PostAdminForm)
admin.site.register(ProductFeatures)
admin.site.register(Photos)
admin.site.register(CallRequests)
