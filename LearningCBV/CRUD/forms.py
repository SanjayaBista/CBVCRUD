from django import forms
from .models import Blog

class BlogAddForm(forms.ModelForm):
    status = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.CharField(widget=forms.Select(choices=status, attrs={'class': 'form-control'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'status', 'author']