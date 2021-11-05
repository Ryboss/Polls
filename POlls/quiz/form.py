from django import forms
from .models import Question1

class Poll(forms.Form):
    poll1 = Question1.title
