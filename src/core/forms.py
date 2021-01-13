from django import forms
from .models import Post, Comment,ContactForms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'context',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class contactform(forms.ModelForm):
    class Meta:
        model=ContactForms
        fields =['Name','Email','Phone_Number','Message']
