from levenshtein_distance import levenshtein_distance

def get_del_ins_num(errs, corrs):
    i, j, dp = levenshtein_distance(errs, corrs)
    del_num, ins_num = 0, 0
    while i > 0 or j > 0:
        if i == 0:
            min_idx = 2
        elif j == 0:
            min_idx = 1
        else:
            dp_val = [dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]
            min_idx = dp_val.index(min(dp_val))

        if dp[i][j] == dp[i-1][j-1] and min_idx == 0:
            i -= 1
            j -= 1
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

if __name__ == "__main__":
    e = ["A", "B", "C", "E", "G"]
    c = ["A", "B", "C", "D", "E", "F", "G"]
    get_del_ins_num(e, c)