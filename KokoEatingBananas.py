
'''
875. Koko Eating Bananas
Given:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

'''

def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k = list(range(0, (max(piles) + 3)))
        idx = self.lbinsearch_coco(1, max(piles) + 2, (piles, h))
        return idx

    def lbinsearch_coco(self, l, r, checkparams):
        while l < r:
            mid = (l + r) // 2
            if self.check_coco(mid, checkparams):
                r = mid
            else:
                l = mid + 1
        return l

    def check_coco(self, mid, checkparams):
        piles, hour = checkparams
        summa = 0
        for pile in piles:
            if pile <= mid:
                summa += 1
            elif pile % mid == 0:
                summa += pile // mid
            else:
                summa += (pile // mid) + 1

        return summa <= hour
