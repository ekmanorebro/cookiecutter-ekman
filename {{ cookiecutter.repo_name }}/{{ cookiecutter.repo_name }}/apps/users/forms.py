from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreationForm(forms.UserCreationForm):
  
  class Meta(forms.UserCreationForm.Meta):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

    labels = {
      'username': 'Username:',
      'first_name': 'First name:',
      'last_name': 'Last name:',
      'email': 'Email:',  
    }