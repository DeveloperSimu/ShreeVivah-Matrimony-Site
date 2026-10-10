from django.shortcuts import get_object_or_404, render, redirect
from .models import BrideProfile, Comment, GroomProfile
from .forms import GroomForm, BrideForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

@login_required
def about(request):
    return render(request, 'main/about.html')

@login_required
def success_stories(request):
    return render(request, 'main/success_stories.html')

@login_required
def contact(request):
    return render(request, 'main/contact.html')

@login_required
def bride_list(request):
    brides = BrideProfile.objects.select_related("user")
    return render(
        request,
        "main/bride.html",
        {
            "brides": brides.filter(is_sample=False),
            "featured_brides": brides.filter(is_sample=True, is_featured=True),
            "extra_brides": brides.filter(is_sample=True, is_featured=False),
        },
    )

@login_required
def groom_list(request):
    grooms = GroomProfile.objects.select_related("user")
    return render(
        request,
        "main/groom.html",
        {
            "grooms": grooms.filter(is_sample=False),
            "featured_grooms": grooms.filter(is_sample=True, is_featured=True),
            "extra_grooms": grooms.filter(is_sample=True, is_featured=False),
        },
    )

@login_required
def create_groom(request):
    form = GroomForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST" and form.is_valid():
        groom = form.save(commit=False)
        groom.user = request.user
        groom.save()
        return redirect("groom")
    return render(
        request,
        "main/create_profile.html",
        {
            "form": form,
            "profile_type": "Groom",
            "profile_list_url": "groom",
        },
    )

@login_required
def create_bride(request):
    form = BrideForm(
        request.POST if request.method == "POST" else None,
        request.FILES if request.method == "POST" else None,
    )
    if request.method == "POST" and form.is_valid():
        bride = form.save(commit=False)
        bride.user = request.user
        bride.save()
        return redirect("bride")
    return render(
        request,
        "main/create_profile.html",
        {
            "form": form,
            "profile_type": "Bride",
            "profile_list_url": "bride",
        },
    )


@login_required
def bride_detail(request, pk):
    profile = get_object_or_404(BrideProfile, pk=pk)
    return render(
        request,
        "profiles/extra_profile.html",
        {"profile": profile, "profile_list_url": "bride"},
    )


@login_required
def groom_detail(request, pk):
    profile = get_object_or_404(GroomProfile, pk=pk)
    return render(
        request,
        "profiles/extra_profile.html",
        {"profile": profile, "profile_list_url": "groom"},
    )

@login_required
def comment_list(request):
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect("comments")
    else:
        form = CommentForm()
    return render(
        request,
        "main/comments.html",
        {"comments": comments, "form": form}
    )

@login_required
def comment1_list(request):
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.save()
            return redirect("comments1")  # url name keo update koro
    else:
        form = CommentForm()

    return render(
        request,
        "main/comments1.html",   # ekhane comments1.html use korlam
        {"comments": comments, "form": form}
    )