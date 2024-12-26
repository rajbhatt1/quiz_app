from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import QuesModel

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 

class categoryform(ModelForm):
    class Meta:
        model= category1
        fields="__all__"

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"



class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        category_id = kwargs.pop('category_id')
        super().__init__(*args, **kwargs)

        # Get questions for the selected category
        questions = QuesModel.objects.filter(category_id=category_id)
        
        for question in questions:
            # Create a radio button field for each question
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[
                    (question.op1, question.op1),
                    (question.op2, question.op2),
                    (question.op3, question.op3),
                    (question.op4, question.op4),
                ],
                label=question.question,
                widget=forms.RadioSelect,
            )

    
