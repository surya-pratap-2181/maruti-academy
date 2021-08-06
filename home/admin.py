from django.contrib import admin
from home.models import Content, Glimpses, GlimpsesImage
# Register your models here.


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name',
                    'position', 'category', 'photo')
    search_fields = ('title', 'name')


class GlimpsesImageInline(admin.TabularInline):
    model = GlimpsesImage
    extra = 3


@admin.register(Glimpses)
class GlimpsesAdmin(admin.ModelAdmin):
    inlines = [GlimpsesImageInline, ]
    list_display = ('id', 'name',)


@admin.register(GlimpsesImage)
class GlimpsesImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'glimpses', 'image')
