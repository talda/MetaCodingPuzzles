from random import randint
from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    print("C:" + str(C))
    current_pos = 1
    current_time = 0
    for pos in C:
        current_time_ = min(min(abs(pos - current_pos), abs(N - pos + current_pos)), abs(N + pos - current_pos))
        print("current_time_:" + str(current_time_))
        current_time += current_time_
        current_pos = pos
  # Write your code here
    return current_time



def main():
    # Call the function
    # print(getMinCodeEntryTime(3, 3, [1, 3, 3]))
    print(getMinCodeEntryTime(10, 4, [randint(1, 10) for i in range(4)]))
# Python's idiom to ensure the mainred function is called when the script is run directly
if __name__ == "__main__":
    main()




