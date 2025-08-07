from collections import deque
import sys
import copy

sys.setrecursionlimit(10000)

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(choco, visited, sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and choco[nr][nc] == '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))

def is_connected(choco):
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if choco[i][j] == '#':
                bfs(choco, visited, i, j)
                break

    for i in range(N):
        for j in range(N):
            if choco[i][j] == '#' and not visited[i][j]:
                return False
    return True

def find_all_edges(choco):
    edges = []
    for r in range(N):
        for c in range(N):
            if choco[r][c] == '#':
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and choco[nr][nc] == '#':
                        if (nr, nc, r, c) not in edges:
                            edges.append((r, c, nr, nc))
    return edges

def is_all_bridges(choco):
    nodes = []
    node_index = {}
    idx = 0

    # 모든 노드 위치 기록 및 인덱스 부여
    for r in range(N):
        for c in range(N):
            if choco[r][c] == '#':
                nodes.append((r, c))
                node_index[(r, c)] = idx
                idx += 1

    # 인접 리스트 생성
    adj = [[] for _ in range(len(nodes))]
    for i, (r, c) in enumerate(nodes):
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and choco[nr][nc] == '#':
                j = node_index[(nr, nc)]
                if j not in adj[i]:
                    adj[i].append(j)

    # 간선 하나씩 제거해보며 확인
    for i in range(len(nodes)):
        for j in adj[i]:
            if i < j:  # 중복 제거
                # 간선 i-j 제거
                visited = [False] * len(nodes)

                def dfs(u, banned_v):
                    visited[u] = True
                    for v in adj[u]:
                        if (u == i and v == j) or (u == j and v == i):
                            continue  # 간선 제거
                        if not visited[v]:
                            dfs(v, banned_v)

                dfs(i, j)

                if visited[j]:  # 여전히 연결되어 있다면 다리가 아님
                    return False

    return True

result = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == '#':
            temp = copy.deepcopy(grid)
            temp[i][j] = '.'  # 하나 제거

            if not is_connected(temp):
                continue

            if is_all_bridges(temp):
                result.append((i + 1, j + 1))

result.sort()
print(len(result))
for r, c in result:
    print(r, c)
