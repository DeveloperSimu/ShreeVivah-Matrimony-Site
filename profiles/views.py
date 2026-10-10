from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth.decorators import login_required

from main.models import BrideProfile, GroomProfile

@login_required
def rahul(request):
    return render_profile(request, "rahul")

@login_required
def brent(request):
    return render_profile(request, "brent")

@login_required
def matthew(request):
    return render_profile(request, "matthew")

@login_required
def arjun(request):
    return render_profile(request, "arjun")

@login_required
def karan(request):
    return render_profile(request, "karan")

@login_required
def ankita(request):
    return render_profile(request, "ankita")

@login_required
def ishita(request):
    return render_profile(request, "ishita")
    
@login_required
def priya(request):
    return render_profile(request, "priya")

@login_required
def neha(request):
    return render_profile(request, "neha")

@login_required
def sneha(request):
    return render_profile(request, "sneha")

def render_profile(request, slug):
    profile = BrideProfile.objects.filter(slug=slug).first()
    profile_list_url = "bride"
    if profile is None:
        profile = GroomProfile.objects.filter(slug=slug).first()
        profile_list_url = "groom"
    if profile is None:
        raise Http404("Profile not found.")
    return render(
        request,
        "profiles/extra_profile.html",
        {"profile": profile, "profile_list_url": profile_list_url},
    )

@login_required
def extra_profile(request, slug):
    return render_profile(request, slug)


def _find_profiles_by_name(query):
    query = query.strip()
    if not query:
        return []

    results = []
    for model, gender, detail_route in (
        (BrideProfile, "bride", "bride_detail"),
        (GroomProfile, "groom", "groom_detail"),
    ):
        for profile in model.objects.filter(name__icontains=query):
            results.append(
                {
                    "name": profile.name,
                    "gender": gender,
                    "profession": profile.profession,
                    "location": profile.location,
                    "about": profile.about,
                    "photo_url": (
                        profile.photo.url
                        if profile.photo
                        else staticfiles_storage.url(profile.image_path)
                        if profile.image_path
                        else ""
                    ),
                    "url": (
                        reverse("extra_profile", args=(profile.slug,))
                        if profile.slug
                        else reverse(detail_route, args=(profile.pk,))
                    ),
                }
            )

    return sorted(results, key=lambda profile: profile["name"].casefold())


@login_required
def profile_name_suggestions(request):
    query = request.GET.get("q", "").strip()
    results = _find_profiles_by_name(query)
    return JsonResponse({"profiles": results})


@login_required
def profile_search(request):
    query = request.GET.get("q", "").strip()
    profiles = _find_profiles_by_name(query)

    if len(profiles) == 1:
        return redirect(profiles[0]["url"])

    return render(
        request,
        "profiles/search_results.html",
        {"query": query, "profiles": profiles},
    )