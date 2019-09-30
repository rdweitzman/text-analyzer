import requests
import json

response = requests.get(input("Provide the url for the .txt file you would like to analyze from the Project Gutenberg website (or elsewhere): "))

working_responce = response.content.decode("utf-8")

punctuation = ['!', '.', '-', ':', ',', '_', "'"]

text_dict = {
'character_count': 0, 
'character_count_excluding_spaces': 0,  
'letter_count': 0,  
'line_count': 0, 
'word_count': 0, 
'sentence_count': 0, 
'paragraph_count': 0, 
'average_words_per_sentence': 0, 
'average_sentences_per_paragraph': 0 
}

def count_sentence(para_array):
    sentence_arr = []
    sentence_count = 0
    word_sen = []

    for sent in para_array:
        word_sen.append(len(sent))

    for item in para_array:
        sentence_arr.append(item.count('.'))
        sentence_count += item.count('.')

    for point in sentence_arr:
        if point < 1:
            sentence_arr.remove(point)

    text_dict['sentence_count'] = sentence_count
    text_dict['average_sentences_per_paragraph'] = sum(sentence_arr) / len(sentence_arr)   
    text_dict['average_words_per_sentence'] = sum(word_sen) / len(word_sen)
    
def parse_text(user_document):

    strip = user_document.replace(" ", "").replace('\n','')
    working_chars = list(strip)
   
    text_dict['character_count'] = len(user_document)
    text_dict['character_count_excluding_spaces'] = len(list(strip))

    for char in working_chars:
       if punctuation.count(char) >= 1:
           strip = strip.replace(char, "")

    text_dict['letter_count'] = len(list(strip))
    text_dict['line_count'] = user_document.count('\n',)
    text_dict['word_count']= len(user_document.split())

    working_paragraphs = user_document.split('\n')

    working_str = ''
    empty = ''
    working_arr = []

    for var in working_paragraphs:
        if var is not empty: 
         working_str += var
        else:
            working_arr.append(working_str)
            working_str = ''

    count_sentence(working_arr)
    text_dict['paragraph_count'] = len(working_arr)

parse_text(working_responce)

for title in text_dict:
    print('%s: %s' %(title, text_dict[title]))