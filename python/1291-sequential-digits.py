class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:

        def countDigits(number: int) -> int:
            copy: int = number
            counter: int = 0
            while copy > 0:
                copy = copy // 10
                counter += 1
            return counter

        def firstDigit(number: int) -> int:
            copy: int = number
            while copy >= 10:
                copy = copy // 10
            return copy

        def generateOnes(amount: int) -> int:
            value: int = 0
            for i in range(amount):
                value += 10 ** i
            return value

        def getNext(first: int, amount: int) -> int:
            value: int = 0
            first_copy: int = first

            for i in range(amount - 1, -1, -1):
                value += first_copy * (10 ** i)
                first_copy += 1

            return value

        def isCorrect(number: int) -> bool:
            stringified: str = str(number)
            for i in range(len(stringified) - 1):
                if int(stringified[i + 1]) - int(stringified[i]) != 1:
                    return False
            return True

        def obtainFirst(low: int) -> int:
            digits: int = countDigits(low)
            first_digit: int = firstDigit(low)

            start: int = getNext(first_digit, digits)
            if start < low:
                start = getNext(first_digit + 1, digits)
                if not isCorrect(start):
                    start = getNext(1, digits + 1)
            elif not isCorrect(start):
                start = getNext(1, digits + 1)

            return start if isCorrect(start) else -1

        current: int = obtainFirst(low)

        if current == -1:
            return []

        result: list = []
        
        if current >= low and current <= high:
            result.append(current)

        while current <= high:
            current_digits: int = countDigits(current)
            next_entry: int = current + generateOnes(current_digits)

            if countDigits(next_entry) > current_digits or current % 10 == 9:
                next_entry = getNext(1, current_digits + 1)
                
            if next_entry <= high:
                result.append(next_entry)
            current = next_entry

        return result
        