from django.contrib import admin

from .models import Question, Choice, Catagory

@admin.register(Catagory)
class TagAdmin(admin.ModelAdmin):
  	list_display = ('name', 'slug')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
  	#list_display = ('question_text', 'pub_date')
  	filter_horizontal = ('catagories', )

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
  	list_display = ('question', 'choice_text', 'votes')

