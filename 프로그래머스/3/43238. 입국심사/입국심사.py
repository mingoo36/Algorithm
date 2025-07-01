# 심사 가능한 모든 시간 중에서 이분탐색으로 최소값 추출
def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)
        
        if total >= n: ## 심사가능한 인원이 n보다 클때
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
            
    return answer