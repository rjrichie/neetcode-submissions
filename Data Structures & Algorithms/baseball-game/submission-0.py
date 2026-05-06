class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        tmp1 = 0

        record = []
        while operations:
            op = operations.pop(0)
            if op == "C":
                record.pop()
            elif op == "D":
                record.append(2 * tmp1)
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                tmp1 = int(op)
                record.append(tmp1)

        for num in record:
            score += num
        return score