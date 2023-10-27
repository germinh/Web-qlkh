from django import forms
from .models import SignupForm
class Formdangky(forms.ModelForm):  
    class Meta:  
        model = SignupForm
        fields = "__all__" 