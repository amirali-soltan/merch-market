from django import forms
from .models import Comment,Question,Answer

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'positive_points', 'negative_points' , 'suggest']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text'] 
