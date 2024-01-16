# urls.py
from django.urls import path
from .views import HomeView, TestemunhoListCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "api/testemunhos/",
        TestemunhoListCreateView.as_view(),
        name="testemunho-list-create",
    ),
]
