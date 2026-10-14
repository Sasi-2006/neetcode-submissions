class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [['a', a], ['b', b], ['c', c]]
        while True:
            counts.sort(key=lambda x: -x[1])
            added = False
            for ch, cnt in counts:
                if cnt == 0:
                    continue
                if len(result) >= 2 and result[-1] == result[-2] == ch:
                    continue
                result.append(ch)
                for item in counts:
                    if item[0] == ch:
                        item[1] -= 1
                added = True
                break
            if not added:
                break
        return "".join(result)