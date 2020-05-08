import sys
import platform
import codecs
import mojimoji
from get_del_ins_num import get_del_ins_num
import utils

d_num = 6
i_num = 6
lang = "ja"
#####

def process(text):
    err_corr = text.split("\t")
    if len(err_corr) == 2:
        err = mojimoji.zen_to_han(err_corr[0].rstrip('\n'), kana=False)
        err = mojimoji.han_to_zen(err, ascii=False, digit=False)
        corr = mojimoji.zen_to_han(err_corr[1].rstrip('\n'), kana=False)
        corr = mojimoji.han_to_zen(corr, ascii=False, digit=False)
        err_lang = utils.lang_check(err, lang)
        corr_lang = utils.lang_check(corr, lang)

        if err_lang and corr_lang:
            errs = list(err)
            corrs = list(corr)
            del_num, ins_num = get_del_ins_num(errs, corrs)
            del_portion = del_num / len(errs)
            ins_portion = ins_num / len(corrs)
            if del_num < d_num and ins_num < i_num and del_portion < 0.4 and ins_portion < 0.4:
                 print(err + "\t" + corr)

if __name__ == "__main__":
    assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
    file = sys.argv[1]
    with codecs.open(file, 'r', encoding='utf8') as f:
        for text in f:
            process(text)