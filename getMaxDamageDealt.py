from typing import List
# Write any import statements here

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:

    B = float(B)
    H = [float(h)/B for h in H]
    DH = [(d*h) for d, h in zip(D, H)]

    dd = 0.0
    first = 0
    for dh in DH:
        if dh > DH[first]:
            first = DH.index(dh)
    
    second = 0 if first != 0 else 1
    for dh in DH:
        if dh > DH[second] and dh < DH[first]:
            second = DH.index(dh)
           
    print(first, second) 
    dd = DH[first] + DH[second] + H[first] * D[second]
    dd2 = DH[second] + DH[first] + H[second] * D[first]
    if dd2 > dd:
        dd = dd2
        first, second = second, first
    foundMax = False
    while not foundMax:
        foundMax = True
        for newf in range(N):
            if newf == first or newf == second:
                continue
            damage1 = DH[newf] + DH[second] + H[newf] * D[second]
            damage2 = DH[first] + DH[newf] + H[first] * D[newf]
            if damage1 > damage2:
                if damage1 > dd:
                    first = newf
                    dd = damage1
                    foundMax = False
            elif damage2 > dd:
                second = newf
                dd = damage2
                foundMax = False
        
    return dd


def main():
    N = 3
    H = [2, 1, 4]
    D = [3, 1, 2]
    B = 4
    # print(getMaxDamageDealt(N, H, D, B))
    N = 4
    H = [1, 1, 2, 100]
    D = [1, 2, 1, 3]
    B = 8
    # print(getMaxDamageDealt(N, H, D, B))
    N = 4
    H = [1, 1, 2, 3]
    D = [1, 2, 1, 100]
    B = 8
    print(getMaxDamageDealt(N, H, D, B))


# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
