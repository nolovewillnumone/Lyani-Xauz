from django.contrib import admin
from .models import Menu,Category,Reservation,MenuCategory,Subscriber


admin.site.register(Reservation)
admin.site.register(Category)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'order', 'is_access')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('category__name', 'order')

@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Показываем поле email в списке
    search_fields = ('email',)  # Добавляем возможность поиска по email


