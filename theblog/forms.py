from django import forms
from .models import Post, Comment, Reply#, Category

choice_list = []

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image', 'body')#'title_tag', 'impression'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body') #,'title_tag', 'impression',, 'header_image'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={}),
        }


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={"placeholder":"reply here"}),
        }