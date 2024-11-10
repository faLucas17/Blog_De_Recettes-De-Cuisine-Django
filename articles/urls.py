from django.urls import path
from articles import views
from articles.views import article_detail_view, delete_article, home, modifier_article, useradmin, article_list_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("index/", home, name="index"), 
    path("useradmin/", useradmin, name="useradmin"),
    path("edit_article/<int:id>/", modifier_article, name="modifier_article"),
    path('useradmin/delete/<int:id>/', delete_article, name='delete_article'),
    path('articles/', article_list_view, name='article-list'),  # Utilisez article_list_view ici
    path('articles/<int:id>/', article_detail_view, name='article-detail'),  # URL pour les détails de l'article
    path('Apropos/', views.apropos, name='apropos'),
    path('recettes/', views.recettes, name='recettes'),
    path('videos/', views.videos, name='videos'),
    path('livreDeCuisine/', views.livreDeCuisine, name='livreDeCuisine'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
