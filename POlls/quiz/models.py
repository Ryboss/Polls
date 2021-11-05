from django.db import models

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    question2 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=20)
    option5 = models.CharField(max_length=20)
    option6 = models.CharField(max_length=20)
    question3 = models.CharField(max_length=100)
    option7 = models.CharField(max_length=20)
    option8= models.CharField(max_length=20)
    option9 = models.CharField(max_length=20)
    question4 = models.CharField(max_length=100)
    option10 = models.CharField(max_length=20)
    option11 = models.CharField(max_length=20)
    option12 = models.CharField(max_length=20)
    question5 = models.CharField(max_length=100)
    option13 = models.CharField(max_length=20)
    option14 = models.CharField(max_length=20)
    option15 = models.CharField(max_length=20)


    def __str__(self):
        return self.question


class Question1(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    question2 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=20)
    option5 = models.CharField(max_length=20)
    option6 = models.CharField(max_length=20)
    question3 = models.CharField(max_length=100)
    option7 = models.CharField(max_length=20)
    option8 = models.CharField(max_length=20)
    option9 = models.CharField(max_length=20)
    question4 = models.CharField(max_length=100)
    option10 = models.CharField(max_length=20)
    option11 = models.CharField(max_length=20)
    option12 = models.CharField(max_length=20)
    question5 = models.CharField(max_length=100)
    option13 = models.CharField(max_length=20)
    option14 = models.CharField(max_length=20)
    option15 = models.CharField(max_length=20)

    def __str__(self):
        return self.title