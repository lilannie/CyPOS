from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class UserForm (ModelForm):
    first_name = forms.CharField(help_text="First Name:")
    last_name = forms.CharField(help_text="Last Name:")
    username = forms.CharField(help_text="Username:")
    email = forms.CharField(help_text="Email:")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Password:")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


# Modify user information form 
class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        fieldsets = [{
            'first_name':'First Name', 
            'last_name': 'Last Name', 
            'username': 'Username', 
            'email': 'Email',
            #'title': "Modify your user information here. Any information you would like to keep, do not modify."
        }]

# class UserEditPasswordForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['old_password', 'new_password', 'repeat_new_password']
#         fieldsets = [{
#             'old_password':'Old Password', 
#             'new_password': 'New Password', 
#             'repeat_new_password': 'Repeat New Password', 
#             #'title': "Modify your user information here. Any information you would like to keep, do not modify."
#         }]

class ChangePasswordForm(ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), required=True)
    new_password_again = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        fieldsets = [{
            'id': 'update-password',
            'legend': 'Change Password',
            'title': 'Your password should be at least 8 characters long.<br>' +
                     'Passwords must contain a lowercase letter, an uppercase letter, and a number or symbol.'
        }]

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        if cleaned_data.get('new_password') != cleaned_data.get('new_password_again'):
            raise forms.ValidationError("The passwords you inputted do not match.")