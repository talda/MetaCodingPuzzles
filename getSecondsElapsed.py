  
from typing import List
# Write any import statements here

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    tunnels = sum(B) - sum(A)
    A.sort()
    B.sort()
    full_circles = K // tunnels
    time = full_circles * C
    tunnel_time = full_circles * tunnels
    last = 0
    if tunnel_time == K:
        return time - (C - B[-1])
    
    for i in range(N):
        if tunnel_time >= K:
            break
        tunnel_time += (B[i] - A[i])
        time += B[i] - last
        last = B[i]
        
    if tunnel_time > K:
        time -= tunnel_time - K
    return time


def main():
    C = 10
    N = 2
    A = [1, 6]
    B = [3, 7]
    K = 7
    print(getSecondsElapsed(C, N, A, B, K))
    C = 50
    N = 3
    A = [39, 19, 28]
    B = [49, 27, 35]
    K = 15
    print(getSecondsElapsed(C, N, A, B, K))

# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()

