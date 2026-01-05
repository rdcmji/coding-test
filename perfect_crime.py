import logging, string, math
from collections import defaultdict

#key값 별로 map 작성해서 count 만큼 돌리기?
def solution3(info, catch_a, catch_b):
    LCM = math.lcm(*range(1,4))
    sorted_keys = []
    sum_b = 0
    sum_a = 0
    min_a = 3
    min_b = 3
    #map설정
    count_info = defaultdict(int)
    for i in info:
        key = str(i)
        if key not in count_info:
            sorted_keys.append(i)
        count_info[key] += 1
        sum_a += i[0]
        sum_b += i[1]
        min_a = min(min_a, i[0])
        min_b = min(min_b, i[1])
    #
    if sum_b < catch_b:
        return 0
    if (sum_a >= catch_a and min_b >= catch_b) or (sum_b >=catch_b and min_a >= catch_a):
        return -1
    if catch_a <= min_a:
        return 0
    if catch_b <= min_b:
        return sum_a
    if catch_a + catch_b <= len(info) + 2:
        return -1
    #우선순위에 따른 정렬
    sorted_keys = sorted(sorted_keys, key = lambda x: (LCM - x[1]*LCM/x[0], x[0]))
    print(sorted_keys)
    answer = catch_a
    def trace(idx, sum_a, sum_b):
        nonlocal answer
        if idx >= len(sorted_keys):
            return answer
        key = sorted_keys[idx]
        a, b = key
        count = min(count_info[str(key)], math.ceil((sum_b - catch_b+1)/b))
        print()
        print(f"idx is {idx}, count is {count}")
        end = max(-1, count-4)
        for i in range(count,end, -1):
            print(f"idx is {idx}, count is {i}")
            new_sum_a = sum_a + a*i
            new_sum_b = sum_b - b*i
            print(f"new_sum_a is {new_sum_a}, answer is {answer}, new_sum_b is {new_sum_b}")
            if new_sum_a > answer:
                continue
            if new_sum_b < catch_b:
                answer = new_sum_a
                continue
            trace(idx+1, new_sum_a, new_sum_b)
    trace(0,0,sum_b)
    print(answer)
    return answer if answer < catch_a else -1

#n번 반복해서 찾기
def solution2(info, catch_a, catch_b):
    LCM = math.lcm(*range(1,4))
    #map설정
    count_info = defaultdict(int)
    sorted_keys = []
    sum_b = 0
    sum_a = 0
    for i in info:
        count_info[str(i)] += 1
        sorted_keys.append(i)
        sum_b += i[1]
    if sum_b < catch_b:
        return [0,[]]
    #우선순위에 따른 정렬
    sorted_keys = sorted(sorted_keys, key = lambda x: (LCM - x[1]*LCM/x[0], x[0]))

    prev_key = False
    for key in sorted_keys:
        a, b = key
        if prev_key:
            prev_a, prev_b = prev_key
            if a < prev_a and sum_b + prev_b - b < catch_b:
                sum_a = sum_a - prev_a + a
                sum_b = sum_b + prev_b - b
                prev_key = key

            continue


        # count 조건 확인: catch b보다 작음을 확신하는 최솟값을 count 값으로 한다.
        count = min(count_info[str(key)], math.ceil((sum_b - catch_b+1)/key[1]))
        sum_b = sum_b - (b*count)
        sum_a = sum_a + (a*count)
        # 원하는 sum b 조건을 충족한 경우
        if sum_b < catch_b :
            #catch b랑 sum b 차이가 큰 경우
            if catch_b - sum_b > 1:
                prev_key = key
            else:
                break
    return [sum_a if sum_a < catch_a else -1, count_info]

#brute force 모든 경우 해보기
def solution(info, catch_a, catch_b):
    count = 0
    answer = catch_a
    def sum_trace(idx, sum_a, sum_b):
        nonlocal count, answer
        count+=1
        logging.info(f"idx is {idx}, sum_a is {sum_a}, sum_b is {sum_b}")
        # impossible case
        if sum_a >= catch_a or sum_a >= answer:
            return catch_a

        if sum_b < catch_b:
            answer = min(answer, sum_a)
            return sum_a

        #impossible case
        if idx >= len(info):
            return catch_a
        
        my_a, my_b = info[idx]
        idx += 1
        
        return min(sum_trace(idx, sum_a, sum_b), sum_trace(idx, sum_a+my_a, sum_b-my_b))

    sum_a, sum_b = list(map(sum, zip(*info)))
    min_a, min_b = list(map(min, zip(*info)))
    info = sorted(info)

    if (sum_a >= catch_a and min_b >= catch_b) or (sum_b >=catch_b and min_a >= catch_a):
        return -1
    if catch_a <= min_a:
        return 0
    if catch_b <= min_b:
        return sum_a
    if catch_a + catch_b <= len(info) + 2:
        return -1
    answer = sum_trace(0, 0, sum_b)
    
    # logging.info(f"count is {count}")
    # print(f"count is {count}")
    print(answer)
    return answer if answer < catch_a else -1

def answer(info, catch_a, catch_b):
    dp = {0:0}
    for a,b in info:
        ndp = {}
        for k,v in dp.items():
            if a+k < catch_a:
                ndp[a+k] = min(ndp.get(a+k,v),v)
            if b+v < catch_b:
                ndp[k] = min(ndp.get(k,b+v),b+v)
        dp=ndp
    if dp:
        return min(dp)
    return -1
# print(solution3([[1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 1],
#          [1, 2],
#          [1, 2]], 6, 8))

# count_info = defaultdict(int)
# print('sdf' in count_info)
dp = {0:0}
print(dp.items())