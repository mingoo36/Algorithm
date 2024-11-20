def solution(numlist, n):
    numlist.sort(reverse=True)
    numlist = sorted(numlist, key = lambda x : abs(n-x))
    return numlist