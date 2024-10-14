class Solution:
    def findInMountainArray(self, target: int, mountain_arr: any) -> int:
        
        def search(low, high):
            if high < low:
                return -1
            
            mid = low + (high - low) // 2
            current = mountain_arr.get(mid)

            if mid > 0:
                previous = mountain_arr.get(mid - 1)
            else:
                previous = float('-inf')

            if mid < mountain_arr.length() - 1:
                next = mountain_arr.get(mid + 1)
            else:
                next = float('-inf')

            if current > previous and current > next:
                return mid
            elif current < previous:
                return search(low, mid - 1)
            else:
                return search(mid + 1, high)
            
        def search_left(low, high, target):
            while low <= high:
                mid = low + (high - low) // 2
                current = mountain_arr.get(mid)

                if current == target:
                    return mid
                elif current < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        def search_right(low, high, target):
            while low <= high:
                mid = low + (high - low) // 2
                current = mountain_arr.get(mid)

                if current == target:
                    return mid
                elif current > target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        k = search(0, mountain_arr.length() - 1)
        left_idx = search_left(0, k, target)
        if left_idx != -1:
            return left_idx
        
        right_idx = search_right(k + 1, mountain_arr.length() - 1, target)
        return right_idx
