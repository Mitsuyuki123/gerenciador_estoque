from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gerenciador_estoque/', include('gerenciador_estoque.urls')),
    path('', lambda request: redirect('gerenciador_estoque/', permanent=True))
]
