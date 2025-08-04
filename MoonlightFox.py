import heapq
import sys

def solution():
    input = sys.stdin.readline
    INF = float('inf')

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, d = map(int, input().split())
        cost = d * 2  # 늑대의 속도 대비 정수 계산용
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    # 여우: 일반 다익스트라
    def dijkstra_fox():
        distance = [INF] * (N + 1)
        distance[1] = 0
        hq = [(0, 1)]
        while hq:
            dist, now = heapq.heappop(hq)
            if distance[now] < dist:
                continue
            for nxt, cost in graph[now]:
                new_dist = dist + cost
                if new_dist < distance[nxt]:
                    distance[nxt] = new_dist
                    heapq.heappush(hq, (new_dist, nxt))
        return distance

    # 늑대: 빠름(0), 느림(1) 상태 다익스트라
    def dijkstra_wolf():
        distance = [[INF] * (N + 1) for _ in range(2)]
        distance[0][1] = 0
        hq = [(0, 1, 0)]  # dist, node, state
        while hq:
            dist, now, state = heapq.heappop(hq)
            if distance[state][now] < dist:
                continue
            for nxt, cost in graph[now]:
                if state == 0:  # 지금 빠르게 → 다음 느리게
                    new_dist = dist + cost // 2
                    next_state = 1
                else:  # 지금 느리게 → 다음 빠르게
                    new_dist = dist + cost * 2
                    next_state = 0
                if new_dist < distance[next_state][nxt]:
                    distance[next_state][nxt] = new_dist
                    heapq.heappush(hq, (new_dist, nxt, next_state))
        return distance

    fox = dijkstra_fox()
    wolf = dijkstra_wolf()

    count = 0
    for i in range(2, N + 1):
        wolf_min = min(wolf[0][i], wolf[1][i])
        if fox[i] < wolf_min:
            count += 1

    print(count)


if __name__ == "__main__":
    import sys
    from io import StringIO

    sys.stdin = StringIO("""5 6
1 2 3
1 3 2
2 3 2
2 4 4
3 5 4
4 5 3
""")
    solution()