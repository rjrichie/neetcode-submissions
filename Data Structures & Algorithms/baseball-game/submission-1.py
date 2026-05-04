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
                record.append(2 * record[-1])
            elif op == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(op))

        for num in record:
            score += num
        return score