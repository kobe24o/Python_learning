import math
class Solution:
    def circleGame(self, toys, circles, r: int) -> int:
        # r - dis(i,j) >= Rtoy
        dis_c = []
        for c in circles:
            dis_c.append(c[0] * c[0] + c[1] * c[1])
        cir_disc = list(zip(circles, dis_c))
        cir_disc.sort(key=lambda x: x[1]) # 按照到原点的距离排序
        dis_c = [x[1] for x in cir_disc] # 距离的值，一会按这个二分查找
        ans = 0
        import bisect
        def dis(x1, y1, x2, y2):
            return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

        for t in toys:
            x, y, rt = t
            if r < rt: # 肯定套不下
                continue
            # dis(i,j) <= r-rt
            # d*d <= (r-rt)^2
            limit = (r - rt) * (r - rt) # 圆心距离的平方的上限
            d = x * x + y * y # 玩具到原点的距离
            # 二分查找，只有在 玩具附近 +- 圈套半径 范围内的才 有可能套中玩具
            idx_left = bisect.bisect_left(dis_c, math.pow((max(0, math.sqrt(d) - r)), 2))
            idx_right = bisect.bisect_right(dis_c, pow(math.sqrt(d) + r, 2))
            for i in range(idx_left, min(idx_right + 1, len(dis_c))): # 在这个范围内查找
                if dis(x, y, cir_disc[i][0][0], cir_disc[i][0][1]) <= limit:
                    ans += 1
                    break
        return ans