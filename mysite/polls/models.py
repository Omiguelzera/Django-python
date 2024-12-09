from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 200)
    vostes = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.question.id}:{self.choice_text}"