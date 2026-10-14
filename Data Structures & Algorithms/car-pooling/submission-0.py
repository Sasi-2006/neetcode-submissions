class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = [0] * 1001  # since locations go up to 1000
        for num, start, end in trips:
            changes[start] += num
            changes[end] -= num
        current_passengers = 0
        for change in changes:
            current_passengers += change
            if current_passengers > capacity:
                return False
        return True