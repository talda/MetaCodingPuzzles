
from typing import List
from typing import List, Tuple
# Write any import statements here
Vals_dict = {}
def findVal(Val: chr, G: List[List[str]]) -> List[Tuple[int, int]]:
    if Val in Vals_dict:
        return Vals_dict[Val]
    found = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == Val:
                found.append((i, j))
                
    Vals_dict[Val] = found
    return found

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    Vals_dict.clear()
    positions = []
    positions.append((findVal('S', G)[0], 0, 'S'))
    visited = {}
    visited[positions[0][0]] = True
    while len(positions) > 0:
        pos, t, val = positions.pop(0)
        if val == 'E':
            return t
        
        dxdy = [(0,1), (1,0), (0,-1), (-1,0)]
        for dd in dxdy:
            npos = (pos[0] + dd[0], pos[1] + dd[1])
            if npos[0] < R and npos[0] >= 0 and npos[1] < C and npos[1] >= 0 and G[npos[0]][npos[1]] != '#':
                if npos in visited:
                    continue
                else:
                    visited[npos] = True
                    positions.append((npos, t+1, G[npos[0]][npos[1]]))
        if G[pos[0]][pos[1]] >= 'a' and G[pos[0]][pos[1]] <= 'z':
            telpos = findVal(G[pos[0]][pos[1]], G)
            for tp in telpos:
                if tp in visited:
                    continue
                else:
                    visited[tp] = True
                    positions.append((tp, t+1, G[tp[0]][tp[1]]))
                    
                    
    return -1
        
    


def main():
    # Call the function
    R = 3
    C = 3
    G = ['.E.', '.#E', '.S#']
    print(getSecondsRequired(R, C, G))
    R = 3
    C = 4
    G = ['a.Sa', '####', 'Eb.b']
    print(getSecondsRequired(R, C, G))
    R = 3
    C = 4
    G = ['aS.b', '####', 'Eb.a']
    print(getSecondsRequired(R, C, G))
    R = 1
    C = 9
    G = ['xS..x..Ex']
    print(getSecondsRequired(R, C, G))

# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
from typing import List
# Write any import statements here
