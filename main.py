from fastapi import FastAPI
from pydantic import BaseModel


class Sentence(BaseModel):
    sentence: str


pig_latin_app = FastAPI()


@pig_latin_app.post("/piglatin-converter/")
async def piglatin_converter(sentence: Sentence):
    return {"message": translate_to_piglatin(sentence.sentence)}


def translate_to_piglatin(user_sentence):
    ay = 'ay'
    consonant = (
        'B', 'C', 'D', 'F', 'G', 'H', 'J',
        'K', 'L', 'M', 'N', 'P', 'Q', 'R',
        'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
    )
    vowel = ('A', 'E', 'I', 'O', 'U')
    punctuation = (',', '?', '!', ';', '.', ':')
    pig_latin_string = ""
    words = user_sentence.split()

    for word in words:
        first_letter = word[0]
        first_letter = str(first_letter)

        last_letter = str(word[-1])
        re_add_punctuation = False
        re_add_capitalization = False

        if last_letter in punctuation:
            word = word[:-1]
            re_add_punctuation = True

        if first_letter.isupper():
            re_add_capitalization = True

        first_letter = first_letter.upper()
        if first_letter in consonant:
            consonant_prefix = ''
            for letter in word[0:3:1]:
                if letter.upper() in consonant:
                    consonant_prefix += letter
                else:
                    break
            length_of_consonants = len(consonant_prefix)
            length_of_word = len(word)
            remove_consonants = word[length_of_consonants:length_of_word]
            pig_latin = remove_consonants + consonant_prefix + ay
            if re_add_punctuation:
                pig_latin += last_letter
            if re_add_capitalization:
                pig_latin = pig_latin.capitalize()
            pig_latin_string = pig_latin_string + ' ' + pig_latin

        elif first_letter in vowel:
            pig_latin = word + ay
            if re_add_punctuation:
                pig_latin += last_letter
            if re_add_capitalization:
                pig_latin = pig_latin.capitalize()
            pig_latin_string = pig_latin_string + ' ' + pig_latin

        else:
            print('?')

    return pig_latin_string
