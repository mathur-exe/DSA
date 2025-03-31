
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    fleet : int = 0
    pair = list(zip(position, speed)) # pair: pos, speed
    pair.sort(reverse=True) 
    time_stack = []

    for pos, s in pair:
        time_stack.append((target - pos) / s)
        if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
            time_stack.pop()

    return len(time_stack)

    