
from typing import List
# Write any import statements here


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    def total_dist(i: int, N:int, c: int) -> int:
        d1 = min(abs(i-c), N-abs(i-c))
        return d1    
    
    C = [c-1 for c in C]
    options = {}
    options[(0,0)] = 0
    n_options = {}
    for c in C:
        for key, val in options.items():
            d0 = total_dist(key[0], N, c)
            nop = (c, key[1])
            nop = (min(nop), max(nop))
            if nop not in n_options or n_options[nop] > val + d0:
                n_options[nop] = val + d0
            d0 = total_dist(key[1], N, c)
            nop = (key[0], c)
            nop = (min(nop), max(nop))
            if nop not in n_options or n_options[nop] > val + d0:
                n_options[nop] = val + d0
        print(n_options)    
        options = n_options
        n_options = {}
    return min(options.values())
                
            
            
def main():
    N = 3
    M = 3
    C = [1, 2, 3]
    print(getMinCodeEntryTime(N, M, C))
    N = 10
    M = 4
    C = [9, 4, 4, 8]
    print(getMinCodeEntryTime(N, M, C))


# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
from typing import List
# Write any import statements here