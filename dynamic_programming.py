from collections import defaultdict

def fibonacci_recursive(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def dyna_fibonacci(n, state):
    if n <= 2:
        state[n] = 1
    if state[n] is None:
        state[n] = dyna_fibonacci(n-1, state) + dyna_fibonacci(n-2, state)
    return state[n]


def dyna_fibonacci_tabular(n):
    results = [1, 1]
    for i in range(2, n):
        results.append(results[i-1] + results[i-2])
    return results[-1]


if __name__ == "__main__":
    print(fibonacci_recursive(6))
    print(dyna_fibonacci(6, defaultdict(lambda: None)))
    print(dyna_fibonacci_tabular(6))

