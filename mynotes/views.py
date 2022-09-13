from django.views.decorators.http import require_POST

from .models import Category, Note
from django.contrib import messages
from django.contrib.auth.forms import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import CategoryForm, NoteForm
from .filters import Categoryfilter


# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


def categories(request):
    paginator = Paginator(Category.objects.filter(creator=request.user), 5)
    page_number = request.GET.get('page')
    paged_categories = paginator.get_page(page_number)

    userscategory = Note.objects.filter(noter=request.user)
    userscategories = userscategory.all()

    filterbycategory = Categoryfilter(request.GET, queryset=userscategories)
    userscategories = filterbycategory.qs

    context = {
        'categories': paged_categories,
        'filterbycategory': filterbycategory,
        'userscategories': userscategories,
    }
    return render(request, 'categories.html', context)


def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('/categories')
    context = {
        'form': form
    }
    return render(request, 'category_form.html', context)


def updateCategory(request, pk):
    category=Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return redirect('/categories')
    context = {
        'form': form
    }
    return render(request, 'category_form.html', context)


def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('/categories')

    context = {
        'item': category
    }
    return render(request, 'delete.html', context)


def category(request, category_id):
    single_category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category.html', {'category': single_category})


def notes(request):
    paginator = Paginator(Note.objects.filter(noter=request.user), 5)
    page_number = request.GET.get('page')
    paged_notes = paginator.get_page(page_number)
    context = {
        'notes': paged_notes
    }
    return render(request, 'notes.html', context=context)


def addNote(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.noter = request.user
            form.save()
            return redirect('/notes')
    context = {
        'form': form
    }
    return render(request, 'note_form.html', context)


def updateNote(request, pk):
    note=Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.instance.noter = request.user
            form.save()
            return redirect('/notes')
    context = {
        'form': form
    }
    return render(request, 'note_form.html', context)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('/notes')

    context = {
        'item': note
    }
    return render(request, 'delete_note.html', context)


def search(request):
    query = request.GET.get('query')
    search_results = Note.objects.filter(Q(noter=request.user), Q(name__icontains=query))
    return render(request, 'search.html', {'notes': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already in use!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with e-mail {email} already exist!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, 'Registration was successful! Please login')
                    return redirect('register')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'register.html')


