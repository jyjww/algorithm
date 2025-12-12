def solution(nums):
    seen = set(nums)
    
    if len(nums) // 2 < len(seen):
        return len(nums) // 2
    else:
        return len(seen)