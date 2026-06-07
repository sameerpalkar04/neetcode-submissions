class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        size = len(height)
        left_to_right = [1]*size
        right_to_left = [1]*size

        left_to_right[0] = height[0]
        for i in range(1, size):
            left_to_right[i] = max(left_to_right[i-1], height[i])
        
        right_to_left[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            right_to_left[i] = max(right_to_left[i+1], height[i])
        
        for i in range(size):
            result += min(left_to_right[i], right_to_left[i])-height[i]
        return result
