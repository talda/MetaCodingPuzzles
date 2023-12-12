from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    solutions = [(0,0,0)]
    n_solutions = []
    u_solutions = []
    for ind, s in enumerate(S):
        for threes in range(max(0, s//3 - 1), s//3+1):
            for twos in [0, 1, 2]:
                ones = s-3*threes-2*twos
                if ones >=0 and ones < 3 and twos < 3:
                  n_solutions.append((ones, twos, threes))              
        for solution in solutions:
            for n_solution in n_solutions:
                ts = (max(solution[0], n_solution[0]), max(solution[1], n_solution[1]), max(solution[2], n_solution[2]))
                found = False
                for us in u_solutions:
                    if us[0] <= ts[0] and us[1] <= ts[1] and us[2] <= ts[2]:
                        found = True
                        break
                    if us[0] > ts[0] and us[1] > ts[1] and us[2] > ts[2]:
                        u_solutions.remove(us)
                if not found:
                    u_solutions.append(ts)
        
        solutions = u_solutions
        n_solutions = []
        u_solutions = []
        
    min_num = solutions[0][0]+solutions[0][1]+solutions[0][2]
    for s in solutions:  
        num = s[0]+s[1]+s[2]
        min_num = min(min_num, num)

    return min_num
  
def main():
    N = 5
    S = [1, 2, 3, 4, 5]
    print(getMinProblemCount(N , S))
    N = 4
    S = [4, 3, 3, 4]
    print(getMinProblemCount(N, S))
    N = 4
    S = [2, 4, 6, 8]
    print(getMinProblemCount(N, S))
    N = 1
    S = [8]
    print(getMinProblemCount(N, S))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()

