# 1
n, m = map(int, input().split()) # n 열 m 행
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data) # min 함수 사용
    for j in range(m):
        # '가장 작은 수'들 중에서 가장 큰 수 찾기
        result = max(result, min_value)
print(result)

# 2
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data: # 이중 반복문
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)