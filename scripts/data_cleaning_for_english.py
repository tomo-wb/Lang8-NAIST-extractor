import sys
import platform
import codecs
from nltk import tokenize
import mojimoji
import langid

# number of parallel processing
para = 4

# settings for xxx2018 paper
d_num = 6
i_num = 6
#####

def check_ascii(text):
    if text:
        return max([ord(char) for char in text]) < 128
    return True

def levenshtein_distance(errs, corrs):
    errs_len = len(errs)
    corrs_len = len(corrs)
    inf = float("inf")
    dp = [[inf for i in range(corrs_len+1)] for j in range(errs_len+1)]
    dp[0][0] = 0

    for i in range(-1, errs_len):
        for j in range(-1, corrs_len):
            if i == -1 and j == -1:
                continue
            elif i >= 0 and j >= 0:
                if errs[i].lower() == corrs[j].lower():
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1] + 1, dp[i+1][j] + 1)
                else:
                    dp[i+1][j+1] = min(dp[i][j] + 1, dp[i][j+1] + 1, dp[i+1][j] + 1)
            elif i >= 0:
                dp[i+1][j+1] = dp[i][j+1] + 1
            elif j >= 0:
                dp[i+1][j+1] = dp[i+1][j] + 1

    del_num, ins_num = 0, 0
    while i > 0 and j > 0:
        dp_val = [dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]
        min_idx = dp_val.index(min(dp_val))
        if dp[i][j] == dp[i-1][j-1] and min_idx == 0:
            i -= 1
            j -= 1
            continue
        elif min_idx == 0:
            del_num += 1
            ins_num += 1
            i -= 1
            j -= 1
        elif min_idx == 1:
            del_num += 1
            i -= 1
        else:
            ins_num += 1
            j -= 1
    return del_num, ins_num

def lang_check(text):
    text = mojimoji.zen_to_han(text.rstrip('\n'), kana=False)
    lang, prob = langid.classify(text)
    ascii = check_ascii(text)

    if lang == 'en' and ascii:
        return True
    else:
        return False

def process(text):
    err_corr = text.split("\t")
    if len(err_corr) == 2:
        err_lang = lang_check(err_corr[0])
        corr_lang = lang_check(err_corr[1])
        if err_lang and corr_lang:
            errs = tokenize.word_tokenize(err_corr[0])
            corrs = tokenize.word_tokenize(err_corr[1])
            del_num, ins_num = levenshtein_distance(errs, corrs)
            if del_num < d_num and ins_num < i_num:
                print(" ".join(errs) + "\t" + " ".join(corrs))

if __name__ == "__main__":
    assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
    file = sys.argv[1]
    with codecs.open(file, 'r', encoding='utf8') as f:
        for text in f:
            process(text)
        #Parallel(n_jobs=para, verbose=5)([delayed(process)(text) for text in f])

