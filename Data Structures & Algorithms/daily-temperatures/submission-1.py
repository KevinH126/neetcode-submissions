class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_ = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack_) == 0:
                stack_.append(i)
            else:
                while stack_ and temperatures[stack_[-1]] < temperatures[i]:
                    output[stack_[-1]] = i-stack_[-1]
                    stack_.pop()
                stack_.append(i)
        while len(stack_) > 0:
            output[stack_[-1]] = 0
            stack_.pop()
        return output