import sys
import codecs
import json

filename = sys.argv[1]

langs = {}
with codecs.open(filename, 'r', encoding='utf8') as f:
    for line in f:
        try:
            jsonData = json.loads(line, strict=False)
            l2_lang, l1_lang = jsonData[2], jsonData[3]
            l2_langs = l2_lang.split(", ")
            for lang in l2_langs:
                if not lang in langs:
                    langs[lang] = 1
            if not l1_lang in langs:
                langs[l1_lang] = 1
        except:
            pass
langs_list = []
for k in langs.keys():
    langs_list.append(k)

print(langs_list)