from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs_accessible(target):
        visited = [[False]*m for _ in range(n)]
        q = deque()

        # 외부 공기 시작점: 바깥 가상 좌표에서 탐색
        for r in range(n):
            q.append((-1, r))  # 위쪽 외부
            q.append((n, r))   # 아래쪽 외부
        for c in range(m):
            q.append((c, -1))  # 왼쪽 외부
            q.append((c, m))   # 오른쪽 외부

        accessible = set()

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    if grid[nr][nc] == '.':
                        visited[nr][nc] = True
                        q.append((nr, nc))
                    elif grid[nr][nc] == target:
                        accessible.add((nr, nc))
        return accessible

    for req in requests:
        target = req[0]
        if len(req) == 2:  # 크레인
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == target:
                        grid[r][c] = '.'
        else:  # 지게차
            for r, c in bfs_accessible(target):
                grid[r][c] = '.'

    return sum(1 for r in range(n) for c in range(m) if grid[r][c] != '.')


# 테스트
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))  # 11
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))  # 4
