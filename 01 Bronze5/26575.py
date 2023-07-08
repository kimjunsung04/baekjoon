for _ in range(int(input())):
    d, f, p = map(float, input().split())
    total_cost = d * f * p
    formatted_cost = "${:.2f}".format(total_cost)
    print(formatted_cost)
