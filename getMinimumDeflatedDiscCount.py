from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    lastR = R[-1]
    deflated = 0
    for r in R[-2::-1]:
        if r >= lastR:
            deflated += 1
            lastR -= 1
            if lastR == 0:
                return(-1)
        else:
            lastR = r
            
            
    
  
    return deflated


def main():
    # Call the function
    N = 5
    R = [2, 5, 3, 6, 5]
    print(getMinimumDeflatedDiscCount(N, R))
    N = 3
    R = [100, 100, 100]
    print(getMinimumDeflatedDiscCount(N, R))
    N = 4
    R = [6, 5, 4, 3] 
    print(getMinimumDeflatedDiscCount(N, R))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
    
   