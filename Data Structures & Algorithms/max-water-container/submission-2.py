class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum_area = 0
        left = 0
        right = len(heights)-1

        while left<=right:
            curr_height = min(heights[left], heights[right])
            width = right-left
            area = width*curr_height
            maximum_area = max(maximum_area, area)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maximum_area