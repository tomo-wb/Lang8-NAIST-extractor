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
    return i, j, dp