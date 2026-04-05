class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def find_peak(l,r):
            while l <= r:
                m = l + (r-l) // 2
                if mountainArr.get(m)>mountainArr.get(m-1) and mountainArr.get(m+1)>mountainArr.get(m):
                    l = m+1
                elif mountainArr.get(m)<mountainArr.get(m-1) and mountainArr.get(m)>mountainArr.get(m+1):
                    r = m-1
                else:
                    return m
            

        def b_search(l,r,flag):
            while l<=r:
                m = l + (r-l) // 2

                if mountainArr.get(m) == target:
                    return m
                elif mountainArr.get(m)<target:
                    if flag:
                        l = m+1
                    else:
                        r = m-1
                else:
                    if flag:
                        r = m-1
                    else:
                        l = m+1
                
            return -1

        peak = find_peak(0, mountainArr.length()-1)
        print(peak)
        res = b_search(0, peak, True)
        if res == -1:
            res = b_search(peak+1, mountainArr.length()-1, False)

        return res
        

