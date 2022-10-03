# 1
n, m, k = map(int, input().split()) # 5 8 3
a = input().split() # 2 4 5 4 6

a.sort()
first = a[n-1]
second = a[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 2
n, m, k = map(int, input().split()) # 5 8 3
a = input().split() # 2 4 5 4 6

a.sort()
first = a[n-1]
second = a[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count)* first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)