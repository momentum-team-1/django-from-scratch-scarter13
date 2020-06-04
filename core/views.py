from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        #return redirect (to='snippet_list')
        snippets = request.user.snippets.all
    else:
        snippets = []

    return render(request, "snippets/home.html", {"snippets": snippets})

def snippet_list(request):
    snippets = request.user.snippets.all()
    # Clinton had () at the end of this line, but I think he removed them later?
    return render(request, "steve_project/snippet_list.html", {"snippets": snippets})