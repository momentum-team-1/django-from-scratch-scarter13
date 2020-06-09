from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tag
from .forms import SnippetForm 


# Create your views here. recipe  

def homepage(request):
    if request.user.is_authenticated:
        return redirect (to='snippet_list')

    return render(request, "snippets/home.html")

#@login_required
def snippet_list(request):
    snippets = request.user.snippets.all()

    return render(request, "snippets/snippet_list.html", {"snippets": snippets})

#@login_required
def show_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.snippets, pk=snippet_pk)

    return render(request, "snippets/show_snippet.html", {"snippet": snippet})

#@login_required
def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='snippet_list')
    else:
        form = SnippetForm()

    return render(request, "snippets/create_snippet.html", {"form": form})

def delete_snippet(request, pk):
    snippet = get_object_or_404(request.user.snippets, pk=pk)
    if request.method == 'POST':
        snippet.delete()
        return redirect(to='snippet_list')

    return render(request, "snippets/delete_snippet.html",
                  {"snippet": snippet})

def edit_snippet (request, pk):
    snippet = get_object_or_404(request.user.snippets, pk=pk)

    if request.method == 'GET':
        form = SnippetForm(instance=snippet, initial={"tag_names": snippet.get_tag_names()})
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='show_snippet', snippet_pk=snippet.pk)

    return render (request, "snippets/edit_snippet.html", {"form": form, "snippet": snippet})

def view_tag (request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    #snippets = tag.snippets.filter(snippet.visibility=="PUB")
    """
    Note that you will have to pass along 'snippets' in the context along with 'tag' on line 66 when you do decide to activate this; also, some changes you will need in your template
    """
    return render (request, "snippets/tag_detail.html", {"tag": tag})