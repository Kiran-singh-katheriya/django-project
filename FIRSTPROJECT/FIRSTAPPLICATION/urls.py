from django.urls import path
from FIRSTAPPLICATION import views

urlpatterns = [
    path('index/',views.display),
    path('Home/',views.displayTemplate)
]
