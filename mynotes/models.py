from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Note(models.Model):
    photo = models.ImageField('Picture', upload_to='covers/', null=True, blank=True)
    date = models.DateField('Add date in format (yyyy-mm-dd)', null=True, blank=True)
    name = models.CharField('Name', max_length=200)
    description = HTMLField('Description', max_length=2000, blank=True, default='')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
    noter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.date})'

    def get_absolute_url(self):
        return reverse('note-detail', args=[str(self.id)])


class Category(models.Model):
    title = models.CharField('Category', max_length=100, unique=True, help_text='Enter category name for your note (e.g. Important)')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    def display_notes(self):
        return ', '.join(note.name for note in self.notes.all()[:3])

    display_notes.short_description = 'Notes'


