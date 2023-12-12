 
 
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    A, B = min(A, B), max(A, B)
    maxD = 10
    mult = 1
    num = 0
    for numDigits in range(1, 13):
        if A < maxD:
            for i in range(1, 10):
                if A <= i*mult and i*mult <= B:
                    num += 1
            
        maxD *= 10
        mult = mult*10 + 1
        
    return num

def main():
    # Call the function
    A = 75
    B = 300
    print(getUniformIntegerCountInInterval(A, B))
    A = 1
    B = 9
    print(getUniformIntegerCountInInterval(A, B))
    A = 999999999999
    B = 999999999999
    print(getUniformIntegerCountInInterval(A, B))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
    
   