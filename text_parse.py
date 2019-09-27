punctuation = ['!', '.', '-', ':', ',', '_', "'"]

text_dict = {
'character_count': 0, # =)
'character_count_excluding_spaces': 0,  # =)
'letter_count': 0,  # =)
'line_count': 0, # =)
'word_count': 0, # =)
'sentence_count': 0,
'paragraph_count': 0,
'average_words_per_sentence': 0,
'average_sentences_per_paragraph': 0
}

def parse_text():
    file = open('olivertwist.txt')
    text = file.read()
    file.close()
    strip = text.replace(" ", "").replace('\n','')
    working_chars = list(strip)
   
    text_dict['character_count'] = len(text)
    text_dict['character_count_excluding_spaces'] = len(list(strip))

    for char in working_chars:
       if punctuation.count(char) >= 1:
           strip = strip.replace(char, "")

    text_dict['letter_count'] = len(list(strip))
    text_dict['line_count'] = text.count('\n',)
    text_dict['word_count']= len(text.split())

    working_paragraphs = text.split('\n')

    para_list = filter(None, working_paragraphs)

    text_dict['paragraph_count'] = len(para_list)

    print(para_list)


parse_text()
print(text_dict)