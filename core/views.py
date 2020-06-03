from django.shortcuts import render, redirect

# Create your views here.

def homepage(request):
    if request.user.is_authenticated
        return redirect (to='snippet_list')

    return render(request, "core/home.html")

def snippet_list(request):
    snippets = request.user.snippets.all()
    # Clinton had () at the end of this line, but I think he removed them later?
    return render(request, "core/snippet_list.html", {"snippets": snippets})