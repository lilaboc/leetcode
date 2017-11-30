# https://leetcode.com/problems/flood-fill/description/
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        seen = set()
        self.points(image, sr, sc, image[sr][sc], seen)
        for i in seen:
            image[i[0]][i[1]] = newColor
        return image
        


    def points(self, image, x, y, color, seen):
        width = len(image)
        height = len(image[0])
        seen.add((x, y))
        
        points = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        points = filter(lambda x:  x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < height and image[x[0]][x[1]] == color and (x[0],x[1]) not in seen, points)
        [self.points(image, i[0], i[1], color, seen) for i in points]


            

        
#print Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
#print Solution().floodFill([[0,0,0],[0,0,0]], 0, 0, 2)
