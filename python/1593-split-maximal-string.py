class Solution:
    def split(self, idx: int, visited: set, current: str):
        if idx == len(self.string):
            if current == '':
                return visited
            if current not in visited:
                visited.add(current)
                return visited
            return set()
        else:
            char: str = self.string[idx]
            current += char
            if current in visited:
                return self.split(idx + 1, visited, current)
            # We have two options -> either pick the
            # current character and add it, or do not
            # add it and consider it along the next character.
            return max(
                self.split(idx + 1, visited | {current}, ''),
                self.split(idx + 1, visited, current),
                key=lambda x: len(x)
            )
            
        
    def maxUniqueSplit(self, s: str) -> int:
        self.string = s
        result: set = self.split(
            idx=0,
            visited=set(),
            current=''
        )
        return len(result)
