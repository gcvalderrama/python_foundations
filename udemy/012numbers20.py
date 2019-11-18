
def test_20(data):
    result = []
    state = []
    for i in data:
        if 20 % i == 0:
            res = 20 / i
            if res in state:
                return [int(res), i]
            else:
                state.append(i)
    return result

# Clarifying Questions
# is possible to have negative numbers
# does the array contain any duplicate
if __name__ == "__main__":
    input_data = [2, 4, 1, 6, 5, 40, -1]
    print(test_20(input_data))
