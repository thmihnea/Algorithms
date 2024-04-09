from typing import List, Tuple

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Function that moves the first element of an
        array to the back of it. It is used to emulate
        the queue.
        """
        def move_back(array: List[Tuple[int]]):
            first_entry: Tuple[int] = array[0]
            array.pop(0)
            array.append(first_entry)
            
        """
        Map tickets -> entries by a bijection into a
        list of tuples that also retain the initial position
        of each object. Emulate the queue and return the time
        whenever we want to pop the k-th element.
        """
        entries: List[Tuple[int]] = [(i, amount) for i, amount in enumerate(tickets)]
        time: int = 0
        while len(entries) > 0:
            time += 1
            entry: Tuple[int] = entries[0]
            i, amount = entry
            entries[0] = (i, amount - 1)
            if amount > 1:
                move_back(entries)
            else:
                if i == k:
                    return time
                else:
                    entries.pop(0)
        return 0