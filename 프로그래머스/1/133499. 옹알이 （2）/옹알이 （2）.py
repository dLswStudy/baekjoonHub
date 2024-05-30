# 풀이법: 
# 1. 문자열 a, b, c 조합으로 이루어진 문자열은 그 문자열에서 a 빼고 b 빼고 c 빼면 빈 문자열임을 이용.

def solution(babbling):
    answer = 0

    for babble in babbling:
        if not validate_babble(babble):
            print(f"{babble} 은 실패")
            continue
        else:
            print(f"{babble} 은 성공")
            answer += 1

    return answer

# 발음할 수 있는 babble 인지 검사
def validate_babble(babble):
    print('babble', babble, end=' // ')
    
    ongAls = ['aya','ye','woo','ma'] # 옹알이 단어들
    # 연속 옹알이 있으면 False
    for ongAl in ongAls:
        if ongAl*2 in babble:
            return False

    # babble 에서 조카의 옹알이 제거
    for ongAl in ongAls:
        if ongAl in babble:
            babble = babble.replace(ongAl,'#')
            
    babble = babble.replace('#','')

    if babble:
        return False

    return True

