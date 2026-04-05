class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=set()
        new_arr = sorted(intervals, key=lambda e: e[0])
        i=0
        while i<len(new_arr):
            start_index = new_arr[i][0]
            end_index = new_arr[i][1]
            j=i+1

            while (j<len(new_arr) and end_index >=new_arr[j][0]):
                if new_arr[j][1]>new_arr[i][1]:
                    end_index = new_arr[j][1]
                j+=1

            res.add((start_index,end_index))
            i=j

        result=list(res)
        result.sort()
        return result

                