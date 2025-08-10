def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}  # 이름 → 인덱스 매핑

    # 1. 선물 주고받기 기록 행렬
    gift_count = [[0] * n for _ in range(n)]  # gift_count[i][j] = i가 j에게 준 선물 수
    give_total = [0] * n  # 각자 준 선물 총합
    recv_total = [0] * n  # 각자 받은 선물 총합

    for g in gifts:
        a, b = g.split()
        ai, bi = idx[a], idx[b]
        gift_count[ai][bi] += 1
        give_total[ai] += 1
        recv_total[bi] += 1

    # 2. 선물 지수 계산
    gift_score = [give_total[i] - recv_total[i] for i in range(n)]

    # 3. 다음 달 받을 선물 개수 계산
    next_month = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if gift_count[i][j] > gift_count[j][i]:  # i가 j에게 더 많이 줌 → 다음 달 i가 받음
                next_month[i] += 1
            elif gift_count[i][j] < gift_count[j][i]:  # j가 i에게 더 많이 줌 → 다음 달 j가 받음
                next_month[j] += 1
            else:  # 같으면 선물 지수 비교
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1
                # 같으면 아무도 안 받음

    return max(next_month)

if __name__ == "__main__":
        solution()
