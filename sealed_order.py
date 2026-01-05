import string
def solution(n, bans):
    alphabet = string.ascii_lowercase 
    #
    def alpha_to_num(alpha):
        num = 0
        for i in range(len(alpha)):
            a = alpha[-i-1]
            n = alphabet.find(a) + 1
            num += 26**i*n
        print(alpha, num)
        return num
    def num_to_alpha(num):
        alpha = ''
        while(num != 0):
            print(num)
            quotient,remainder = divmod(num, 26)
            if remainder == 0:
                quotient -=1
                alpha = 'z'+alpha
            else:
                alpha = alphabet[remainder-1] + alpha
            num = quotient
        print(alpha)
        return alpha

    # sort bans
    bans = sorted(bans, key= lambda x:( len(x), x))
    print(bans)
    for ban in bans:
        if alpha_to_num(ban) <= n:
            n+=1
        else:
            break
    return num_to_alpha(n)

answer = solution(30, ["d", "e", "bb", "aa", "ae"])
print(answer)