
from django.db import models
from django.contrib.auth import get_user_model
 
User = get_user_model()

class category1(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    category = models.ForeignKey(category1, on_delete=models.CASCADE, related_name='questions')
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    # ans = models.CharField(
    ans = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Quizhistory(models.Model):
    category = models.ForeignKey(category1, on_delete=models.CASCADE, related_name='quizhistory')
    given_datetime = models.DateTimeField(auto_now_add = True)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.category
    
 