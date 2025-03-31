def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    """
    This question uses monotonic stack
    i.e. as we move from R2L the values must be monotonic (either increaseing or decreasing)
    Here, along with the temp, I'll need to store the idx as well
    """

    answer = [0] * len(temperatures)
    stack = []  # pair: idx, temp

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            stackIdx, stackT = stack.pop()
            answer[stackIdx] = i - stackIdx
        stack.append((i, t))

    return answer