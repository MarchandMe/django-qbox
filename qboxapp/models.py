from django.db import models
from django.utils.timezone import now

STATUS = [
    (0, "Unanswered"),
    (1, "Answered"),
]

class Question(models.Model):
    #qid = models.SlugField(max_length=100, unique = True, default='', editable=False) #does not work for some reason currently
    question = models.TextField()
    answer = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    answered_on = models.DateTimeField(auto_now= True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        first_five_list=self.question.split()[:5] #first five words
        return " ".join(first_five_list)
