from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'date', 'ques']

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Номер вопроса"
            }),
            "date": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Дата"
            }),
            "ques": DateTimeInput(attrs={
                "class": "form-control",
                "placeholder": "Текст вопроса"
            }),
        }