from collections import deque

def fibonacci_queue(n):
    queue = deque([0,1])
    
    if n >= 0:
        for i in range(n):
            queue.append(queue[0] + queue[1])
            queue.popleft()
    else:
        for i in range(abs(n)):
            queue.appendleft(queue[1] - queue[0])
            queue.pop()

    return queue[0]

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    else:
        return fibonacci_recursive(n + 2) - fibonacci_recursive(n + 1)

def lucas_queue(n):
    queue = deque([2,1])

    if n >= 0:
        for i in range(n):
            queue.append(queue[0] + queue[1])
            queue.popleft()
    else:
        for i in range(abs(n)):
            queue.appendleft(queue[1] - queue[0])
            queue.pop()

    return queue[0]

def lucas_recursive(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas_recursive(n - 1) + lucas_recursive(n - 2)
    else:
        return lucas_recursive(n + 2) - lucas_recursive(n + 1)  

def golomb_recursive(n):
    if n == 1:
        return 1
    else:
        return 1 + golomb_recursive(n - golomb_recursive(golomb_recursive(n - 1)))
