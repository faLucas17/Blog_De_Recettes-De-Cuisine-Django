from django.shortcuts import get_object_or_404, redirect, render

from articles.models import Article

from articles.forms import ArticleForm  # Assure-toi d'importer ton formulaire

from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    message= Article.objects.all()
    return render(request, "index.html", {"message":message})


def useradmin(request):
    articles = Article.objects.all()  # Récupérer tous les articles
    form = ArticleForm()  # Initialiser le formulaire en dehors du bloc POST

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Inclure les fichiers si nécessaire
        if form.is_valid():
            form.save()  # Enregistrer l'article dans la base de données
            return redirect('useradmin')  # Redirige vers la page useradmin après l'ajout

    return render(request, "useradmin.html", {"articles": articles, "form": form})  # Passe le formulaire au template




def modifier_article(request, id):
    article = get_object_or_404(Article, id=id)  # Récupère l'article à modifier
    if request.method == 'POST':
        edit_form = ArticleForm(request.POST, request.FILES, instance=article)  # Remplit le formulaire avec l'article existant
        if edit_form.is_valid():
            edit_form.save()  # Enregistre les modifications
            return redirect('useradmin')  # Redirige vers la page useradmin après la modification
    else:
        edit_form = ArticleForm(instance=article)  # Remplit le formulaire avec les données de l'article

    return render(request, "edit_article.html", {"edit_form": edit_form, 'article': article})  # Passe le formulaire au template

def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()  # Supprime l'article
        return redirect('useradmin')  # Redirige vers la page useradmin
    return redirect('useradmin')  # Redirige vers la page useradmin si ce n'est pas une méthode POST

def article_list_view(request):
    articles = Article.objects.all()  # Récupère tous les articles
    return render(request, 'articles_list.html', {'articles': articles})

def article_detail_view(request, id):
    article = get_object_or_404(Article, id=id)  # Récupère l'article par ID
    return render(request, 'article_detail.html', {'article': article})  # Passe l'article au template

def apropos(request):
    return render(request, 'apropos.html')

def recettes(request):
    return render(request, 'recettes.html')

def videos(request):
    return render(request, 'videos.html')

def livreDeCuisine(request):
    return render(request, 'livreDeCuisine.html')

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        objet = request.POST.get('objet')
        
        # Envoyer l'e-mail
        try:
            send_mail(
                subject=f"Contact Form: {objet}",
                message=f"Nom: {nom}\nEmail: {email}\nObjet: {objet}",
                from_email='votre-email@gmail.com',  # Remplacez par votre adresse Gmail
                recipient_list=['ffmaman17@gmail.com'],  # L'adresse où vous souhaitez recevoir l'e-mail
                fail_silently=False,
            )
            messages.success(request, 'Votre message a été envoyé avec succès.')
        except Exception as e:
            messages.error(request, "Erreur lors de l'envoi de l'e-mail. Veuillez réessayer.")
        
        return redirect('contact')

    return render(request, 'contact.html')