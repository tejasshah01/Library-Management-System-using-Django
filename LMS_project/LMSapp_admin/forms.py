from django import forms
from LMSapp_admin.models import issued_book




class user_login(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    Remember_me=forms.BooleanField(label='Remember me')

class Customer_issue_book(forms.ModelForm):
    price=forms.DecimalField(max_digits=10,decimal_places=2)
    borrow_date=forms.DateTimeField(widget=forms.SelectDateWidget)
    class Meta:
        model=issued_book
        fields=['name','book','price','borrow_date','return_date']
        widgets={'book':forms.Select,
                 'return_date':forms.SelectDateWidget}