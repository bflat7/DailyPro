import sys
def maximum_product_of_three(lst):
  if lst is None: return None
  elif len(lst) == 1: return lst[0]
  elif len(lst) == 2: return lst[0] * lst[1]

  top3 = [-1 * sys.maxsize] * 3
  bot3 = [sys.maxsize] * 2

  for val in lst:
    if val > top3[0]:
      top3[2] = top3[1]
      top3[1] = top3[0]
      top3[0] = val
    elif val > top3[1]:
      top3[2] = top3[1]
      top3[1] = val
    elif val > top3[2]:
      top3[2] = val
    
    if val < bot3[0]:
      bot3[1] = bot3[0]
      bot3[0] = val
    elif val < bot3[1]:
      bot3[1] = val
    
  return max(top3[0] * top3[1] * top3[2], top3[0] * bot3[1] * bot3[0])

# print(maximum_product_of_three([-4, -4, 2, 8]))
# 128