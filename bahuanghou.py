def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        a = (state[i] - nextX)
        b = (nextY - i)
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield pos,
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


for solution in queens(8):
    print(solution)
