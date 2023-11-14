_ = input()
n_sum = sum(map(int, input().split()))
if n_sum == 0:
    print("Stay")
elif n_sum > 0:
    print("Right")
elif n_sum < 0:
    print("Left")
