def solution(nums):
    answer = 0
    mom =[]
    mom_m = set(nums)
    a = len(nums)//2
   
    for j in mom_m:
        mom += [j]
        if len(mom) <= a:
            answer +=1
    return answer
