from django import forms
from django.forms import BaseInlineFormSet
from django.forms.widgets import RadioSelect
from django.contrib import admin
from mcq.models import MCQQuestion, Answer
from quiz.admin import QuizAdminForm, AnswerInline
from .models import Quiz,Question
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.widgets import FilteredSelectMultiple

class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)



class CustomInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

class myform(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'

    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all().select_subclasses(),
        required=False,
        label=_("Questions"),
        widget=FilteredSelectMultiple(
            verbose_name=_("Questions"),
            is_stacked=False))


    def __init__(self, *args, **kwargs):
        super(myform, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['questions'].initial = \
                self.instance.question_set.all().select_subclasses()

    def save(self, commit=True):
        quiz = super(myform, self).save(commit=False)
        quiz.save()
        quiz.question_set.set(self.cleaned_data['questions'])
        self.save_m2m()
        return quiz




class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class myTestForm(forms.ModelForm):
    list_display = ('content', 'category',)
    list_filter = ('category',)
    fields = ('content', 'category',
              'figure', 'quiz', 'explanation', 'answer_order')

    search_fields = ('content', 'explanation')
    filter_horizontal = ('quiz',)
    inlines = [AnswerInline]

    class Meta:
        model = Answer
        fields = '__all__'


