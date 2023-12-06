from django import forms 
from .models import Comment
from django.utils.translation import gettext_lazy as _

class CommnetForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(
        attrs={ #contact html-deki atributlar
            'class' : 'form-control', #
            'placeholder' : _('Your review..'), #from django.utils.translation import gettext_lazy as _
            'rows' : 5,
            'cols' : 30, 
            # buradaki bütün kodları frontdaki həmən hissə ilə eyniləşdiririk = detail.html ilə
        }
    ))

    class Meta:
        model = Comment
        fields = ['text']     