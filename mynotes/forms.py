from django.forms import ModelForm, HiddenInput
from .models import Category, Note

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'creator', ]
        widgets = {'creator': HiddenInput()}


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['photo', 'date', 'name', 'description', 'category', 'noter', ]
        widgets = {'noter': HiddenInput()}

