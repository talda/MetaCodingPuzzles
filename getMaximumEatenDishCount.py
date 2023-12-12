from typing import List
from collections import defaultdict

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    def default_factory():
        return -1

    lastEatenDish = defaultdict(default_factory)
    numEatenDishes = 0
    for indA in range(0,N):
        print("lastEatenDish:" + str(lastEatenDish))
        if lastEatenDish[D[indA]] == -1:
            numEatenDishes += 1
            lastEatenDish[D[indA]] = numEatenDishes - 1
        elif numEatenDishes - lastEatenDish[D[indA]] > K:
            numEatenDishes += 1            
            lastEatenDish[D[indA]] = numEatenDishes - 1
        
  # Write your code here
    return numEatenDishes



def main():
    # Call the function
    print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 1))
    print(getMaximumEatenDishCount(6, [1, 2, 3, 3, 2, 1], 2))
    print(getMaximumEatenDishCount(7, [1, 2, 1, 2, 1, 2, 1], 2))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()



