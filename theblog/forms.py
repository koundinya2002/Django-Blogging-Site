from django import forms
from .models import Post, Comment, Reply#, Category

#choices = [('un-organized','un-organized'),('coding', 'coding')]
# choices = Category.objects.all().values_list('name','name')

choice_list = []

# for item in choices:
#     choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image', 'body')#'title_tag', 'impression'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control',}),
            # 'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'impression': forms.Textarea(attrs={'class':'form-control', "placeholder":"write the headline for your blog"}),
        }



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body') #,'title_tag', 'impression',, 'header_image'

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            # 'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Text to appear on tab'}),
            # 'category': forms.Select(choices= choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            # 'impression': forms.Textarea(attrs={'class':'form-control', "placeholder":"write the headline for your blog"}),
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