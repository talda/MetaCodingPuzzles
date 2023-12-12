from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    ones = 0
    twos= 0

    for s in S:
        twos = max(twos, s // 2)
        ones = max(ones, s % 2)


    # print("ones:" + str(ones) + " twos:" + str(twos))
    return ones+twos



def main():
    # Call the function
    print(getMinProblemCount(6, [1, 2, 3, 4, 5, 6]))
    N = 4
    S = [4, 3, 3, 4]
    print(getMinProblemCount(N, S))
    N = 4
    S = [2, 4, 6, 8]
    print(getMinProblemCount(N, S))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()



