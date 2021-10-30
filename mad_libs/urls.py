from django.urls import path, include

urlpatterns = [
    path('', include('libs_app.urls')),
]
