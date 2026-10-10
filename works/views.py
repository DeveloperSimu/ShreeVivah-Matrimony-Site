from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import FirstlookForm, MehendiDesignForm
from .models import Firstlook, MehendiCategory, MehendiDesign
from django.contrib.auth.decorators import login_required

@login_required
def work(request):
    return render(request, 'works/work.html')

@login_required
def services(request):
    return render(request, 'works/services.html')

@login_required
def plans(request):
    return render(request, 'works/plans.html')

@login_required
def firstlook(request):
    firstlooks = Firstlook.objects.order_by("-pk")
    form = FirstlookForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Your Firstlove story has been added.")
            return redirect("firstlook")

    return render(
        request,
        "works/firstlook.html",
        {"firstlooks": firstlooks, "form": form},
    )

@login_required
def mehendi(request):
    form = MehendiDesignForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )

    if request.method == "POST" and form.is_valid():
        design = form.save(commit=False)
        design.submitted_by = request.user
        design.save()
        messages.success(
            request,
            "Your mehendi design has been added to the gallery.",
        )
        return redirect("mehendi")

    return render(
        request,
        "works/mehendi.html",
        {
            "categories": MehendiCategory.objects.all(),
            "designs": MehendiDesign.objects.select_related("category").all(),
            "form": form,
        },
    )

@login_required
def haldi(request):
    return render(request, 'works/haldi.html')

@login_required    
def fire(request):
    return render(request, 'works/fire.html')

@login_required
def together(request):
    return render(request, 'works/together.html')

@login_required
def hand(request):
    return render(request, 'works/hand.html')
