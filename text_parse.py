# import olivertwist



text_dict = {
'character_count': 0,
'character_count_excluding_spaces': 0,
'line_count': 0,
'word_count': 0,
'sentence_count': 0,
'paragraph_count': 0,
'average_words_per_sentence': 0,
'average_sentences_per_paragraph': 0
}

def parse_text():
    file = open('olivertwist.txt')
    text = file.read().replace(" ", "").replace('\n','')
    file.close()
    working_list = list(text)
    print(working_list)
    text_dict['character_count'] = len(working_list)

parse_text()
print(text_dict)