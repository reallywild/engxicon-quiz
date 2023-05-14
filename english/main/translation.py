from typing import ClassVar
from googletrans import Translator 
from random import choice
from nltk.corpus import stopwords 
import re 
from .models import Dictionary, ProgDictionary, TVDictionary, BookDictionary
from django.db import models        


class WordSelector:
    def __init__(self, sentence):
        self.sentence = sentence
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(
            {'was', 'by', 'about', 'of', 'off', 'on', "i'm", 'else', "i'll", "can't", "you'll", "being", "one", "if", "not", "women", "men", "ever", "watson", "jeff", "else's"}
        )

    def clean_sentence(self):
        sentence = re.split(r"[,.?!;:’\s]+", self.sentence.lower())
        return sentence
    
    def filter_sentence(self, min_length, max_length):
        filtered_words = [word for word in self.clean_sentence() if min_length <= len(word) <= max_length and word not in self.stop_words]
        return filtered_words
    
    def choose_word(self, filtered_words):
        random_word = choice(filtered_words)
        return random_word
    
class WordTranslation:
    table: ClassVar[models.Model] = Dictionary
    
    def __init__(self):
        self.sentence = choice(self.table.objects.values_list('sentence', flat=True))
        self.translator = Translator()
        self.ws = WordSelector(self.sentence)
        self.chosen_word = self.ws.choose_word(self.ws.filter_sentence(3, 15))
        
    def __str__(self): 
        result = self.translator.translate(self.chosen_word, src='en', dest='ru')
        return result.text
    
    def get_chosen_word(self):
        return self.chosen_word
    

class TranslationProg(WordTranslation):
    table: ClassVar[models.Model] = ProgDictionary

    def __init__(self):
        super().__init__()

class TranslationTV(WordTranslation):
    table: ClassVar[models.Model] = TVDictionary

    def __init__(self):
        super().__init__()

class TranslationBook(WordTranslation):
    table: ClassVar[models.Model] = BookDictionary

    def __init__(self):
        super().__init__()


# class WordTranslation:
    
#     def __init__(self):
#         self.sentence = choice(Dictionary.objects.values_list('sentence', flat=True))
#         self.translator = Translator()
#         self.ws = WordSelector(self.sentence)
#         self.chosen_word = self.ws.choose_word(self.ws.filter_sentence(3, 15))
        
#     def __str__(self): 
#         result = self.translator.translate(self.chosen_word, src='en', dest='ru')
#         return result.text
    
#     def get_chosen_word(self):
#         return self.chosen_word
    

# class TranslationProg(WordTranslation):
#     def __init__(self):
#         self.sentence = choice(ProgDictionary.objects.values_list('sentence', flat=True))
#         self.translator = Translator()
#         self.ws = WordSelector(self.sentence)
#         self.chosen_word = self.ws.choose_word(self.ws.filter_sentence(3, 15))

#     def __str__(self): 
#         result = self.translator.translate(self.chosen_word, src='en', dest='ru')
#         return result.text
    
#     def get_chosen_word(self):
#         return self.chosen_word
    
# class TranslationTV():
#     def __init__(self):
#         self.sentence = choice(TVDictionary.objects.values_list('sentence', flat=True))
#         self.translator = Translator()
#         self.ws = WordSelector(self.sentence)
#         self.chosen_word = self.ws.choose_word(self.ws.filter_sentence(3, 15))

#     def __str__(self): 
#         result = self.translator.translate(self.chosen_word, src='en', dest='ru')
#         return result.text
    
#     def get_chosen_word(self):
#         return self.chosen_word