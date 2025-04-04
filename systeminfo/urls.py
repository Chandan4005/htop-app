from django.urls import path
from .views import htop  # Import the `htop` function from views.py

urlpatterns = [
    path('htop/', htop, name='htop'),  # 👈 Add this line
]
