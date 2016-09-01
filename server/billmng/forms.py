from django import forms
from models import Bill

class BillForm(forms.ModelForm):

    class Meta:
        model = Bill
        fields = '__all__'
        exclude = ['identifier','user', 'bill_date']