from django.contrib import admin

from .models import Category, Question, Option

# Register your models here.
class OptionInline(admin.TabularInline):
    model = Option

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
    OptionInline,
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass
