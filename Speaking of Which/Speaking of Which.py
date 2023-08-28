#take the modulo of intermediate and final results to prevent them from becoming too large.
MOD = 1000009
def decrypt(encrypted_password):
#length of password.
    n = len(encrypted_password)
#initializes a list dp  of length n+1.
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
#if the current character is 'o' or 'e', it can only be paired with the previous character.
        dp[i] = dp[i - 1]
#check if the previous character and the current character can be paired.
        if encrypted_password[i - 2] != 'o' and encrypted_password[i - 2] != 'e' and (encrypted_password[i - 1] == 'o' or encrypted_password[i - 1] == 'e'):
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    return dp[n]
#take a input user.
encrypted_password = input()
result = decrypt(encrypted_password)
print(result)