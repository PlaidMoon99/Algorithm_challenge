from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    grid = [list(row) for row in storage]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 현재 그리드에서 '외부에 연결된 빈칸(.)'을 표시하는 BFS
    def compute_external_empty():
        visited = [[False]*m for _ in range(n)]
        q = deque()

        # 테두리의 빈칸들을 시작점으로 추가
        for r in range(n):
            for c in (0, m-1):
                if grid[r][c] == '.' and not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))
        for c in range(m):
            for r in (0, n-1):
                if grid[r][c] == '.' and not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] == '.':
                    visited[nr][nc] = True
                    q.append((nr, nc))
        return visited

    for req in requests:
        target = req[0]
        if len(req) == 2:
            # 크레인: 해당 글자 전부 제거
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == target:
                        grid[r][c] = '.'
        else:
            # 지게차: 요청 순간 접근 가능한 것만 제거
            visited_empty = compute_external_empty()
            to_remove = []
            for r in range(n):
                for c in range(m):
                    if grid[r][c] != target:
                        continue
                    accessible = False
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        # 격자 밖으로 인접 -> 바로 외부와 연결된 것
                        if not (0 <= nr < n and 0 <= nc < m):
                            accessible = True
                            break
                        # 인접 칸이 빈칸이고 그 빈칸이 외부와 연결된 경우
                        if grid[nr][nc] == '.' and visited_empty[nr][nc]:
                            accessible = True
                            break
                    if accessible:
                        to_remove.append((r, c))
            for r, c in to_remove:
                grid[r][c] = '.'

    # 남아있는 컨테이너 수 반환
    return sum(1 for r in range(n) for c in range(m) if grid[r][c] != '.')


# 예제 테스트
print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))  # 11
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))  # 4
