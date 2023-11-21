from django import forms 
from .models import Appealing

class AppealingForm(forms.ModelForm):
    # email = forms.EmailField()

    class Meta:
        model = Appealing
        fields = ['full_name', 'email', 'subject', 'message']     