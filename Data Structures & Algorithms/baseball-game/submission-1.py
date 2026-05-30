class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in range(len(operations)):
            if operations[i] == '+':
                add = result[-1] + result[-2]
                result.append(add)
            elif operations[i] == 'D':
                double = result[-1] * 2
                result.append(double)
            elif operations[i] == 'C':
                result.pop()
            else:
                result.append(int(operations[i]))
        return sum(result)