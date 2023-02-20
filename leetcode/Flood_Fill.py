class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] != color:
            q = [[sr,sc]]
            went = [ [0 for i in image[0]] for j in image]
            while len(q)!=0:
                X = q[0][0]
                Y = q[0][1]
                went[X][Y] = 1
                if X-1>=0 and image[X-1][Y]==image[sr][sc] and went[X-1][Y]==0:
                    q.append([X-1,Y])
                    went[X-1][Y] = 1
                    image[X-1][Y] = color
                if X+1<len(image) and image[X+1][Y]==image[sr][sc] and went[X+1][Y]==0:
                    q.append([X+1,Y])
                    went[X+1][Y] = 1
                    image[X+1][Y] = color
                if Y-1>=0 and image[X][Y-1]==image[sr][sc] and went[X][Y-1]==0:
                    q.append([X,Y-1])
                    went[X][Y-1] = 1
                    image[X][Y-1] = color
                if Y+1<len(image[0]) and image[X][Y+1]==image[sr][sc] and went[X][Y+1]==0:
                        q.append([X,Y+1])
                        went[X][Y+1] = 1
                        image[X][Y+1] = color
                q=q[1:]
            image[sr][sc] = color
        return image