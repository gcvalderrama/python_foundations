from collections import deque




def elements(blocks, height):

    for h in height:
        

    pivot = 0
    max = 0    
    for i in range(len(blocks)):
        b = blocks[i]                
        
        if pivot + b >= sum(blocks[i:]):            
            print( '{}  array {}'.format( pivot + b, blocks[i:]) )
            if pivot > max:
                max = pivot            
            pivot = 0            
        pivot += b   

    if pivot > max:
        max = pivot

    return max   

if __name__ == "__main__":
    blocks = [1, 3, 1, 3, 3] 
    height = 2

    print(elements(blocks, height))

