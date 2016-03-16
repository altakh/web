from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=250)
    text = forms.CharField(widget=forms.Textarea)
    def clean_title(self):
        title = self.cleaned_data['title']
	#if not is_ethic(title):
	    #raise forms.ValidationError(u'Not correct', code=12)
	return title
    def clean_text(self):
        text = self.cleaned_data['text']
	#if not is_ethic(text):
	    #raise forms.ValidationError(u'Not correct', code=12)
	return text
    def save(self):
	question = Question(**self.cleaned_data)
	question.save()
	return question
#21
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()
    def clean_question(self):
	question = self.cleaned_data['question']
	try:
           qs = Question.objects.get(id=question)
	except Question.DoesNotExist:
	     raise forms.ValidationError("not found question %d" %question)
	return qs
    def save(self):
	answer = Answer(**self.cleaned_data)
	answer.save()
	return answer
