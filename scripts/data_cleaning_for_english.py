import sys
import platform
import codecs
from nltk import tokenize
import mojimoji
import utils
from get_del_ins_num import get_del_ins_num

# number of parallel processing
para = 4

# settings
d_num = 6
i_num = 6
lang = "en"
#####

def check_ascii(text):
    if text:
        return max([ord(char) for char in text]) < 128
    return True

def process(text):
    err_corr = text.split("\t")
    if len(err_corr) == 2:
        err = mojimoji.zen_to_han(err_corr[0].rstrip('\n'), kana=False)
        corr = mojimoji.zen_to_han(err_corr[1].rstrip('\n'), kana=False)
        err_lang = utils.lang_check(err, lang) if check_ascii(err) else False
        corr_lang = utils.lang_check(corr, lang) if check_ascii(corr) else False

        if err_lang and corr_lang:
            errs = tokenize.word_tokenize(err)
            corrs = tokenize.word_tokenize(corr)
            del_num, ins_num = get_del_ins_num(errs, corrs)
            del_portion = del_num / len(errs)
            ins_portion = ins_num / len(corrs)
            if del_num < d_num and ins_num < i_num and del_portion < 0.33 and ins_portion < 0.33:
                print(errs + "\t" + corrs)

if __name__ == "__main__":
    assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
    file = sys.argv[1]
    with codecs.open(file, 'r', encoding='utf8') as f:
        for text in f:
            process(text)
        #Parallel(n_jobs=para, verbose=5)([delayed(process)(text) for text in f])

