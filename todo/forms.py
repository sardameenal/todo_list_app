from socket import fromshare
from django import forms

class TodoForm(forms.Form):
    """this form is to add the todo item

    Args:
        text: will represet the input in the add field in the form.
    """
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter todo', 'aria-label': 'todo', 'aria-describedby': 'add-btn'}
    ))