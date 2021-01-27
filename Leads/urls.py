from django.urls import path
from .views import leadlist,leadprofile,createlead


app_name = "leads"

urlpatterns = [
    path('', leadlist ),  
    path('<int:pk>/', leadprofile ),
    path('create/',createlead),
]
 