class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        neighbor = list(zip([1,0,-1,0],[0,1,0,-1]))
        row = len(image)
        col = len(image[0])
        origin_color = image[sr][sc]
        seen = set()
        while queue:
            x, y = queue.pop(0)
            for step in neighbor:
                next_x, next_y = x+step[0], y+step[1]
                if (0 <= next_x < row) and (0 <= next_y < col) \
                    and ((next_x, next_y) not in seen) \
                    and (image[next_x][next_y]==origin_color):
                    queue.append((next_x, next_y))
            image[x][y] = newColor
            seen.add((x,y))
        return image
