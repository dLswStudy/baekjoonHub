def n_to_pn(n):
    return 'IO' * n + 'I'
def count_overlapping_occurrences(main_str, sub_str):
    count = 0
    start = 0
    while True:
        start = main_str.find(sub_str, start)
        if start == -1:
            break
        count += 1
        start += 1  # 겹치는 부분 문자열을 찾기 위해 start를 한 칸 이동
    return count

i1 = int(input())
i2 = int(input())
i3 = input()
print(count_overlapping_occurrences(i3, n_to_pn(i1)))