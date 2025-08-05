import sys
from bisect import bisect_right

def all_subset_sums(arr):
    """arr의 모든 부분합을 리스트로 반환 (공집합 포함)."""
    sums = [0]
    for w in arr:
        # 기존 합들에 w를 더한 새 합들을 확장
        # (리스트 덮어쓰기를 피하려 새 리스트를 만들어 병합)
        new = [s + w for s in sums]
        sums += new
    return sums

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    weights = list(map(int, input().split()))
    
    # 반으로 나누기
    mid = N // 2
    left = weights[:mid]
    right = weights[mid:]
    
    # 각 절반의 모든 부분합
    left_sums = all_subset_sums(left)
    right_sums = all_subset_sums(right)
    
    # 용량 C를 넘는 합은 굳이 유지하지 않아도 되지만,
    # 오른쪽은 정렬 후 이진탐색으로 상한만 체크할 것이므로 전부 두고,
    # 왼쪽은 반복 중에 sL > C인 경우만 건너뜀으로 충분.
    right_sums.sort()
    
    # 왼쪽 부분합마다, 오른쪽에서 (C - sL) 이하의 개수를 더함
    count = 0
    for sL in left_sums:
        if sL <= C:
            remain = C - sL
            # right_sums에서 remain 이하의 원소 개수
            cnt = bisect_right(right_sums, remain)
            count += cnt
        # sL > C이면 어떤 오른쪽 합을 더해도 초과 -> 스킵
    
    print(count)