# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

n = int(input())

sum = 0 # sum은 python 내장함수이름이라서 덮어씀 total이 더 적함
for i in range(1, n+1):
    sum += i
    # sum = sum + i
print(sum)
