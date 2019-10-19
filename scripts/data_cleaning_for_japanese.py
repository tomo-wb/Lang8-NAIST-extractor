import sys
import platform
import codecs
import mojimoji
import langid

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
    #print(del_num, ins_num)
    return del_num, ins_num

def lang_check(text):
    text = mojimoji.zen_to_han(text.rstrip('\n'), kana=False)
    lang, prob = langid.classify(text)

    if lang == 'ja':
        return True
    else:
        return False


def process(text):
    err_corr = text.split("\t")
    if len(err_corr) == 2:
        err_lang = lang_check(err_corr[0])
        corr_lang = lang_check(err_corr[1])

        if err_lang and corr_lang:
            err_corr[0] = mojimoji.han_to_zen(err_corr[0].rstrip('\n'), ascii=False, digit=False)
            err_corr[0] = mojimoji.zen_to_han(err_corr[0], kana=False)
            errs = list(err_corr[0])
            err_corr[1] = mojimoji.han_to_zen(err_corr[1].rstrip('\n'), ascii=False, digit=False)
            err_corr[1] = mojimoji.zen_to_han(err_corr[1], kana=False)
            corrs = list(err_corr[1])
            del_num, ins_num = levenshtein_distance(errs, corrs)
            #print(err_corr[0] + "\t" + err_corr[1])
            if del_num < d_num and ins_num < i_num:
                 print(err_corr[0] + "\t" + err_corr[1])

if __name__ == "__main__":
    assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
    file = sys.argv[1]
    with codecs.open(file, 'r', encoding='utf8') as f:
        for text in f:
            process(text)
