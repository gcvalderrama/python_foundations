def is_zigzag(numbers: list):
    if len(numbers) != 3: 
        raise ValueError('must be 3 elements {}'.format(numbers))
    return 1 if (numbers[0] < numbers[1] > numbers[2]) or  (numbers[0] > numbers[1] < numbers[2])  else 0
if __name__ == "__main__":
    #numbers = [1, 2, 1]
    numbers =  [1, 2, 1, 3, 4]
    numbers =  [1, 3, 4, 5, 6, 14, 14]
    result = list()
    for i in range(len(numbers)):
        if i + 2 < len(numbers):            
            result.append( is_zigzag(numbers[i: i + 3]) )
    print(result)
    
