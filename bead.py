from collections import deque

# 이동 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy, board):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt

def bfs(board, rx, ry, bx, by):
    visited = set()
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visited.add((rx, ry, bx, by))
    
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            return 0
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i], board)
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i], board)
            
            # 파란 구슬이 구멍에 들어간 경우
            if board[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬이 구멍에 들어간 경우
            if board[nrx][nry] == 'O':
                return 1
            
            # 두 구슬이 같은 위치라면, 더 많이 움직인 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth+1))
    
    return 0

# 입력
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

rx = ry = bx = by = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(bfs(board, rx, ry, bx, by))
