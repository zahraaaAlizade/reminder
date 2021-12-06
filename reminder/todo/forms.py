from .models import Category,Task
from django import forms
import datetime

class FriendForm(forms.ModelForm):
    ## change the widget of the date field.
    time = forms.DateField(
        label='What is your birth date?', 
        # change the range of the years from 1980 to currentYear - 5
        # widget=forms.SelectDateWidget( datetime.date.today())
    )
    
    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Task
        fields = ("__all__")