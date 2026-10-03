k = int(input())
t =540 + 45 * k + 5 * (k // 2) + 15 * ((k - 1) // 2)

print(t // 60, t % 60)