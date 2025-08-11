def time_to_sec(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def sec_to_time(sec):
    h = sec // 3600
    sec %= 3600
    m = sec // 60
    s = sec % 60
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)

    # 시청 변화 기록
    times = [0] * (play_sec + 2)
    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        times[start_sec] += 1
        times[end_sec] -= 1

    # 초별 시청자 수
    for i in range(1, play_sec + 1):
        times[i] += times[i - 1]

    # 초별 누적 재생 시간
    for i in range(1, play_sec + 1):
        times[i] += times[i - 1]

    # 슬라이딩 윈도우로 최대 구간 찾기
    max_time = times[adv_sec - 1]
    max_start = 0
    for start in range(adv_sec, play_sec):
        cur_time = times[start] - times[start - adv_sec]
        if cur_time > max_time:
            max_time = cur_time
            max_start = start - adv_sec + 1

    return sec_to_time(max_start)
