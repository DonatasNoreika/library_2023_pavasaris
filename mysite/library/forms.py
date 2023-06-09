from django import forms
from .models import BookReview, Profile, BookInstance
from django.contrib.auth.models import User


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

class DateInput(forms.DateInput):
    input_type = 'date'

class InstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'due_back']
        widgets = {'due_back': DateInput()}
