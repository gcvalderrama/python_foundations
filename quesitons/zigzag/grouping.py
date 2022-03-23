
def mean(numbers):
    return sum(numbers) / len(numbers)

def grouping(serie):
    map = dict()
    for i in range(len(serie)):
        numbers = serie[i]
        m = mean(numbers)
        if m in map:
            map[m].append(i) 
        else:
            map[m] = [i]
    
    return list(map.values())

if __name__ == "__main__":
    a = [[-2,4,7,-6,2,-5,3], 
        [-1,0,0,0], 
        [2,2,-6,17,9,-22,30,-16,0,-1,-11,6,0,-4], 
        [3,3,-8,-2,3]]
    
    print(grouping(a))
