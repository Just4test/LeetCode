# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def p2s(point):
            return "{}_{}".format(point.x, point.y)
        
        #去除重复的点
        map = {}
        for point in points:
            if map.get(p2s(point)):
                map[p2s(point)][1] += 1
            else:
                map[p2s(point)] = [point, 1]
        points = []
        for k in map:
            points.append(map[k][0])
            
        point_len = len(points)
        if point_len <= 2:
            result = 0
            for point in points:
                result += map[p2s(point)][1]
            return result
        #搞个表以免重复计算
        map_flag = [[-1 for x in range(point_len)] for y in range(point_len)]
        
        max_result = 0
        for i, p0 in enumerate(points):
            for j in range(i + 1, point_len):
                if map_flag[i][j] != -1:
                    continue
                p1 = points[j]
                current_result = map[p2s(p0)][1] + map[p2s(p1)][1]
                for k in range(j + 1, point_len):
                    p2 = points[k]
                    if (p0.x == p1.x and p0.x == p2.x) or (p0.y - p1.y) * (p0.x - p2.x) == (p0.y - p2.y) * (p0.x - p1.x):
                        current_result += map[p2s(p2)][1]
                        map_flag[i][k] = j
                        
                if current_result > max_result:
                    max_result = current_result
        
        return max_result