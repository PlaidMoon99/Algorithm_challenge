import sys
import heapq

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    problems = [tuple(map(int, input().split())) for _ in range(n)]
    
    # 데드라인 오름차순, 같은 데드라인이면 컵라면 수 큰 순(선택사항: 없어도 정답)
    problems.sort(key=lambda x: (x[0], x[1]))
    
    heap = []  # 지금까지 선택한 문제들의 컵라면 수를 담는 최소 힙
    for d, ramen in problems:
        heapq.heappush(heap, ramen)
        # 선택한 문제 수가 현재 데드라인을 넘으면, 가장 이득이 작은 문제 버리기
        if len(heap) > d:
            heapq.heappop(heap)
    
    print(sum(heap))
    
if __name__ == "__main__":
        main()
