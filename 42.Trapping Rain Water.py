class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left=0; right = len(height)-1 
        edge = min(height[left],height[right])
        i = 1;cum =0
        while (left+i <= right) or (left <= right - i):
            if edge == height[left]:
                while left+i<=right and height[left+i] <= edge:
                    cum += edge - height[left+i]
                    i += 1
                if left+i<=right:
                    left = left + i
                    edge = min(height[left],height[right])
                    i = 1       
            else:
                while left <= right - i and height[right-i]<= edge:
                    cum += edge - height[right-i]
                    i += 1
                if right - i >= left:
                    right = right - i
                    edge = min(height[left],height[right])
                    i = 1
        return cum