from django.shortcuts import render, redirect
from django.urls import reverse
from .translation import WordTranslation, TranslationProg, TranslationTV, TranslationBook


# Главная страница 
def main(request):
    translation = WordTranslation()
    sentence = translation.sentence
    chosen_word = translation.get_chosen_word()
    if request.method == 'POST':
        entered_word = request.POST.get('wordinput')
        if str(entered_word).lower() == str(request.POST.get('translation')).lower():
            return redirect(reverse('main_correct'))
        else:
            return redirect(reverse('main_incorrect'))
    
    return render(request, 'main.html', {'sentence': sentence, 'translation': translation, 'word': chosen_word, 'message': request.GET.get('message', '')})

def main_correct(request):
    message = "Вы ответили правильно!"
    return redirect(reverse('main') + '?message=' + message)

def main_incorrect(request):
    message = "Вы ответили неправильно."
    return redirect(reverse('main') + '?message=' + message)


# Страница с программной терминологией
def prog(request):
    translation = TranslationProg()
    sentence = translation.sentence
    chosen_word = translation.get_chosen_word()
    if request.method == 'POST':
        entered_word = request.POST.get('wordinput')
        if str(entered_word).lower() == str(request.POST.get('translation')).lower():
            return redirect(reverse('prog_correct'))
        else:
            return redirect(reverse('prog_incorrect'))
    
    return render(request, 'prog.html', {'sentence': sentence, 'translation': translation, 'word': chosen_word, 'message': request.GET.get('message', '')})

def prog_correct(request):
    message = "Вы ответили правильно!"
    return redirect(reverse('prog') + '?message=' + message)

def prog_incorrect(request):
    message = "Вы ответили неправильно."
    return redirect(reverse('prog') + '?message=' + message)


# Страница с предложениями из сериалов и фильмов
def tv(request):
    translation = TranslationTV()
    sentence = translation.sentence
    chosen_word = translation.get_chosen_word()
    if request.method == 'POST':
        entered_word = request.POST.get('wordinput')
        if str(entered_word).lower() == str(request.POST.get('translation')).lower():
            return redirect(reverse('tv_correct'))
        else:
            return redirect(reverse('tv_incorrect'))
    
    return render(request, 'tv.html', {'sentence': sentence, 'translation': translation, 'word': chosen_word, 'message': request.GET.get('message', '')})

def tv_correct(request):
    message = "Вы ответили правильно!"
    return redirect(reverse('tv') + '?message=' + message)

def tv_incorrect(request):
    message = "Вы ответили неправильно."
    return redirect(reverse('tv') + '?message=' + message)


# книжная страница 
def book(request):
    translation = TranslationBook()
    sentence = translation.sentence
    chosen_word = translation.get_chosen_word()
    if request.method == 'POST':
        entered_word = request.POST.get('wordinput')
        if str(entered_word).lower() == str(request.POST.get('translation')).lower():
            return redirect(reverse('book_correct'))
        else:
            return redirect(reverse('book_incorrect'))
    
    return render(request, 'book.html', {'sentence': sentence, 'translation': translation, 'word': chosen_word, 'message': request.GET.get('message', '')})

def book_correct(request):
    message = "Вы ответили правильно!"
    return redirect(reverse('book') + '?message=' + message)

def book_incorrect(request):
    message = "Вы ответили неправильно."
    return redirect(reverse('book') + '?message=' + message)

def handler404(request, exception):
    return render(request, '404.html', status=404)