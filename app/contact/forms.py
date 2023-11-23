from django import forms 
from .models import Appealing
from django.utils.translation import gettext_lazy as _

class AppealingForm(forms.ModelForm):
    # email = forms.EmailField()
    #
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={ #contact html-deki atributlar
            'class' : 'form-control', #
            'placeholder' : _('Full Name'), #from django.utils.translation import gettext_lazy as _
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={ 
            'class' : 'form-control', #
            'placeholder' : _('Email'), 
        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={ #contact html-deki atributlar
            'class' : 'form-control', #
            'placeholder' : _('Subject'), #from django.utils.translation import gettext_lazy as _
        }
    )) 
    message = forms.CharField(widget=forms.TextInput(
        attrs={ #contact html-deki atributlar
            'class' : 'form-control', #
            'placeholder' : _('Message'), #from django.utils.translation import gettext_lazy as _
            'rows' : 6,
        }
    ))

    class Meta:
        model = Appealing
        fields = ['full_name', 'email', 'subject', 'message']     