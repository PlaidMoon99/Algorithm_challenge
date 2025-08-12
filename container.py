from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]

    # 방향 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs_find_accessible(target):
        visited = [[False]*m for _ in range(n)]
        q = deque()

        # 외부 공간 탐색을 위해 테두리에서 빈 공간 탐색
        for r in range(n):
            for c in range(m):
                # 외곽 + 빈 칸
                if (r == 0 or r == n-1 or c == 0 or c == m-1) and grid[r][c] == '.':
                    q.append((r, c))
                    visited[r][c] = True

        # 외부 빈 공간 확장
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    if grid[nr][nc] == '.':
                        visited[nr][nc] = True
                        q.append((nr, nc))
        
        # 접근 가능한 컨테이너 찾기
        accessible = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == target:
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc]:
                            accessible.append((r, c))
                            break
        return accessible

    for req in requests:
        target = req[0]
        if len(req) == 2:
            # 크레인: 해당 알파벳 전부 제거
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == target:
                        grid[r][c] = '.'
        else:
            # 지게차: 접근 가능한 해당 알파벳만 제거
            accessible = bfs_find_accessible(target)
            for r, c in accessible:
                grid[r][c] = '.'

    # 남은 컨테이너 수 계산
    return sum(1 for r in range(n) for c in range(m) if grid[r][c] != '.')


# 테스트
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))  # 11
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))  # 4
