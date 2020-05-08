from levenshtein_distance import levenshtein_distance

def align_err_cor(errs, corrs):
    i, j, dp = levenshtein_distance(errs, corrs)

    err_vals, corr_vals = [], []
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
            corr_vals.append(corrs[j])
            err_vals.append(errs[i])
        elif min_idx == 0:
            i -= 1
            j -= 1
            corr_vals.append(corrs[j])
            err_vals.append(errs[i])
        elif min_idx == 1:
            i -= 1
            corr_vals.append(None)
            err_vals.append(errs[i])
        else:
            j -= 1
            corr_vals.append(corrs[j])
            err_vals.append(None)
    corr_vals.reverse()
    err_vals.reverse()
    return err_vals, corr_vals

if __name__ == "__main__":
    e = ["A", "B", "C", "E", "G", "H"]
    c = ["A", "B", "C", "D", "E", "F", "G"]
    print(align_err_cor(e, c))
    # output is 
    # (['A', 'B', 'C', None, 'E', None, 'G', 'H'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', None])