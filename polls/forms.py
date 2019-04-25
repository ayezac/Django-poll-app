
from django import forms



class PollForm(forms.Form):
    question = forms.CharField(label ='Your question',)
    choice_1= forms.CharField(label ='Your first choice')
    choice_2= forms.CharField(label ='Your second choice')
    choice_3= forms.CharField(label ='Your third choice')


            


