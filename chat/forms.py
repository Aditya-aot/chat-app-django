from django import forms
from django.forms import ModelForm
from .models import Full_chat


class ChatForm(ModelForm):
    content =  forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your topic "}))
    message  =   forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write your Message"}))
    # images = forms.ImageField()
    # null = True, blank = True

    class Meta:
        model = Full_chat
        fields = [
            'content' ,
            'message' ,

            # 'images' ,

        ]

    # fields = [
    #   'first_name' ,
    #   'last_name'


#
# ]

class RawCustomerForm(forms.Form):
    todo      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your first name"}))
    last_date = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "your last name"}))

