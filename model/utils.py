import pypinyin
from googletrans import Translator

def chinese_to_pinyin(text):
    result = pypinyin.pinyin(text, style=pypinyin.Style.TONE)  # Will include tone marks
    return ' '.join([pinyin[0] for pinyin in result])

def chinese_to_english(text):
    """
    Translate Chinese text to English using Google Translate.
    
    Args:
        text (str): Chinese text to translate (can be traditional or simplified)
        
    Returns:
        str: English translation
    """
    translator = Translator()
    result = translator.translate(text, dest='en')
    return result.text


