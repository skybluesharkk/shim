import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    # 배열의 크기 N, M
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    # 배열 입력 받기
    arr = []
    for _ in range(N):
        row = list(map(int, data[idx:idx + M]))
        arr.append(row)
        idx += M

    # 2차원 누적 합 배열 생성
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = arr[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

    # 쿼리 개수 K
    K = int(data[idx])
    idx += 1

    results = []
    for _ in range(K):
        i = int(data[idx])
        j = int(data[idx + 1])
        x = int(data[idx + 2])
        y = int(data[idx + 3])
        idx += 4

        # (i, j)부터 (x, y)까지의 부분 합 계산
        result = dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1]
        results.append(result)

    # 결과 출력
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
