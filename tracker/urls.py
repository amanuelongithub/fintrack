from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('transaction/', views.list_transactions),
    path('transaction/<int:id>/', views.get_transaction),
    path('summary/', views.get_summary),
    path('category/', views.get_summary),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
