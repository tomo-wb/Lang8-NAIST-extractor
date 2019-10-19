def levenshtein_distance(errs, corrs):
    errs_len = len(errs)
    corrs_len = len(corrs)
    dp = [[i+j for i in range(corrs_len+1)] for j in range(errs_len+1)]

    for i in range(1, errs_len+1):
        for j in range(1, corrs_len+1):

            if errs[i-1].lower() == corrs[j-1].lower():
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1] + 1)
            else:
                dp[i][j] = min(dp[i-1][j-1] + 2, dp[i-1][j] + 1, dp[i][j-1] + 1)

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
