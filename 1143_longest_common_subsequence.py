# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

# If there is no common subsequence, return 0.


def longest_common_subsequence(text1: str, text2: str) -> int:
    len1, len2 = len(text1), len(text2)

    dp = [[0] * len2 + 1 for _ in range(len1 + 1)]

    for i in range(len1):
        for j in range(len2):
            if text1[i] == text2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1[j], dp[i][j+1]])

    return dp[-1][-1]
