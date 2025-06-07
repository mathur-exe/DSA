text1 = "abcde"
text2 = "ace"
n, m = len(text1), len(text2)

dp = [[0]*(m+1) for _ in range(n+1)]
print(dp)