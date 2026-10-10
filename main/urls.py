from django.urls import path
from . import views
from profiles import views as profile_views  # Profiles app er views

urlpatterns = [
    path("", views.index, name="index"),
    path("success_stories/", views.success_stories, name="success_stories"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("groom/", views.groom_list, name="groom"),
    path("bride/", views.bride_list, name="bride"),
    path("groom/<int:pk>/", views.groom_detail, name="groom_detail"),
    path("bride/<int:pk>/", views.bride_detail, name="bride_detail"),

    # Search
    path("search/", profile_views.profile_search, name="profile_search"),

    # Groom profile create
    path("create-groom/", views.create_groom, name="create_groom"),

    # Groom profile create
    path("create-bride/", views.create_bride, name="create_bride"),

    # Comments
    path("comments/", views.comment_list, name="comments"),
    path("comments1/", views.comment1_list, name="comments1"),
]
