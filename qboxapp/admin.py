from django.contrib import admin
from .models import Question

#class QuestionAdmin(admin.ModelAdmin):
    #list_display = ('created_on', 'answered_on')
    #list_filter = ("status")
    #search_fields = ['Question', 'Answer']



admin.site.register(Question)#, QuestionAdmin)