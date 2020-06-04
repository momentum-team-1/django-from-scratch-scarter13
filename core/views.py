from django.shortcuts import render, redirect, get_object_or_404

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
def show_snippet(request, pk):
    snippet = get_object_or_404(request.user.snippets, pk=pk)

    return render(request, "snippets/show_snippet.html", {"snippet": snippet})