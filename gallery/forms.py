from django import forms
from .models import *


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('user',)