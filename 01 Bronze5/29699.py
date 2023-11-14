a = "WelcomeToSMUPC"
n = int(input())
if n > 0:
    n -= 1
print(a[n % 14])
