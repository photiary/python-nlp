import hanja

def convert_hanja_to_hangul(text):
    if isinstance(text, str):
        return hanja.translate(text, 'substitution')
    return text