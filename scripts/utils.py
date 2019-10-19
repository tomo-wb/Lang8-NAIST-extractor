import langid

def lang_check(text, lang):
    predicted_lang, prob = langid.classify(text)

    if predicted_lang == lang:
        return True
    else:
        return False