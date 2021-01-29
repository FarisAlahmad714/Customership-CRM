from django.urls import path
from .views import leadlist,leadprofile,createlead,updatelead,deletelead


app_name = "leads"

urlpatterns = [
    path('', leadlist ),  
    path('<int:pk>/', leadprofile ),
    path('<int:pk>/update/', updatelead ),
    path('<int:pk>/delete/', deletelead ),   
    path('create/',createlead),
    
]
 