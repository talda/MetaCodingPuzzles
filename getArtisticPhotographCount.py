def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  print(C)
  backdrops = 0
  backdrops_list = [0]

  for ch in C:
    if ch == 'B':
      backdrops += 1
    backdrops_list.append(backdrops)
  # print("backdrops_list:" + str(backdrops_list))
      

  photographers = 0
  photographers_list = [0]
  for ch in C:
    if ch == 'P':
      photographers += 1
    photographers_list.append(photographers)
  
  # print("photographers_list:" + str(photographers_list))
  photos = 0
  for indA in range(0,N):
    if C[indA] == 'A':
      print(indA)
      photos_ = (backdrops_list[min(indA + Y + 1, N)] - backdrops_list[min(indA + X, N)]) * (photographers_list[max(indA - X + 1, 0)] - photographers_list[max(indA - Y, 0)])
      photos += photos_
      # print("photos:" + str(photos_)) 
      photos_ = (photographers_list[min(indA + Y + 1, N)] - photographers_list[min(indA + X, N)]) * (backdrops_list[max(indA - X + 1, 0)] - backdrops_list[max(indA - Y, 0)])
      photos += photos_
      # print("photos:" + str(photos_)) 
  return photos

def main():
    # Call the function
    print(getArtisticPhotographCount(8, ".PBAAP.B", 1, 3))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()


from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
  # Write your code here
  return 0
