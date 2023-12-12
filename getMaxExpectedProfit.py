from typing import List

# import itertools
# # Write any import statements here
# def getMaxExpectedProfit_(N: int, V: List[int], C: int, S: float, StartVal: float, history: List[bool], hist_val[float]) -> (float, List[bool], List[float]):
  
#   if N == 1: 
#     if StartVal + V[0] - C > 0:
#       return (StartVal + V[0] - C, history + [True], hist_val + (hist_val[-1] + [StartVal + V[0] - C]))
#     else:
#       return (0, history + [False], hist_val + (hist_val[-1]))

#   takingVal, history_t, hist_val_t = getMaxExpectedProfit_(N - 1, V[1:], C, S, 0, history + [True], hist_val + (hist_val[-1] + [StartVal + V[0] - C])) 
#   notTakingVal, history_n, hist_val_n = getMaxExpectedProfit_(N - 1, V[1:], C, S, (StartVal + V[0]) * (1-S), history+[False], hist_val + hist_val[-1])
#   if  takingVal + V[0] - C > notTakingVal:
#     return (V[0] + takingVal - C, history_t)
#   else:
#     return (notTakingVal, history_n)
def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:

    best = [(0,0)]
    for i in range(0, N):
      best.insert(0, (0,0))
      for b in range(0, len(best)):
        best[b] = (best[b][0]*(1-S), best[b][1])

      val = 0
      for b in best:
        if b[0] + b[1] > val:
          val = b[0] + b[1]
          
      #taking today
      best[0] = (0, val + V[i]- C)
      for b in range(1, len(best)):
        best[b] = (best[b][0] + V[i], best[b][1])
        

    print(best)
    max_p = 0
    for b in best:
      if b[1] > max_p:
        max_p = b[1]
    return max_p



def main():
    # Call the function
  N = 5
  V = [10, 2, 8, 6, 4]
  C = 5
  S = 0.0
  print(getMaxExpectedProfit(N, V, C, S))
  N = 5
  V = [10, 2, 8, 6, 4]
  C = 5
  S = 1.0
  print(getMaxExpectedProfit(N, V, C, S))
  N = 5
  V = [10, 2, 8, 6, 4]
  C = 3
  S = 0.5
  print(getMaxExpectedProfit(N, V, C, S))
  N = 5
  V = [10, 2, 8, 6, 4]
  C = 3
  S = 0.15
  print(getMaxExpectedProfit(N, V, C, S))
  # N = 2
  # V = [10, 4]
  # C = 3
  # S = 0.2
  # print(getMaxExpectedProfit(N, V, C, S))
# Python's idiom to ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()
