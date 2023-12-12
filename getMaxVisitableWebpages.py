from typing import List

#Not solving all test cases
def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    in_visits = [0] * N
    for l in L:
        in_visits[l - 1] += 1
    max_pages = 0
    num_visited = [set() for _ in range(N)]
    for i in range(N):
        current = i
        while current not in num_visited[i] and len(num_visited[current]) == 0:
            num_visited[i].add(current)
            in_visits[current] -= 1
            current = L[current] - 1
            
        if len(num_visited[current]) > 0 and current != i:
            num_visited[i] = num_visited[i].union(num_visited[current])
            
        if in_visits[current] == 0:
            num_visited[current] = set()
        max_pages = max(max_pages, len(num_visited[i]))
    return max_pages



def main():
    N = 4
    L = [4, 1, 2, 1]
    print(getMaxVisitableWebpages(N, L))
    N = 5
    L = [4, 3, 5, 1, 2]
    print(getMaxVisitableWebpages(N, L))
    N = 5
    L = [2, 4, 2, 2, 3]
    print(getMaxVisitableWebpages(N, L))


# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
from typing import List
# Write any import statements here
