from django.db import models

class Articles(models.Model):
    title = models.CharField('Номер вопроса:', max_length=25)
    date = models.DateTimeField('Время создания вопроса:')
    ques = models.CharField('Текст вопроса:', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
