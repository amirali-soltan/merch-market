from django.contrib import admin
from app_social.models import Comment, Image, Question, Answer

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
