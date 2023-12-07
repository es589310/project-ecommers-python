from django import forms 
from .models import Comment, ProductItem
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
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


class ProductItemForm(forms.ModelForm):
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
        model = ProductItem
        fields = ['product', 'size', 'color', 'quantity']    

