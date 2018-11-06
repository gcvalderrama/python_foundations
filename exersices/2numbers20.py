
def test_20(data):
    result = []
    for i in data:
        for j in data:
            if i * j == 20:
                result.append((i, j))
                return result
    return result

# is possible to have negative numbers
# does the array contain any duplicate
if __name__ == "__main__":
    input_data = [2, 4, 1, 6, 5, 40, -1]
    print(test_20(input_data))
