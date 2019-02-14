from django.contrib import admin

# Register your models here.
from blog_content.models import Category, ContentModle, Docket

admin.site.register(Category)
admin.site.register(ContentModle)
admin.site.register(Docket)
