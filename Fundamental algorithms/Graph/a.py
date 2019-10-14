


(4,1) (2, 3) (5, 2), (1, 3), (6, 2), (2, 1)
(height, width) 

           ##
      ##   ##
  #   ##   ##
  #   ##   ##
  ######   ###
  ############
  
  
           ##
      ##000##
  #000##000##
  #000##000##
  ######000###
  ############


return 18 

(6,1) (2, 3) (5, 2), (1, 3), (6, 2), (2, 1)
(height, width) 

      ##   ##
  #   ##   ##
  #   ##   ##
  #   ##   ##
  ######   ###
  ############
  
def findUnitsOfWater(wooden_bars):
    # wooden_bars is a list of tuples
    total = 0 
    
    prefixMax = getPrefixMax(wooden_bars)
    suffixMax = getPrefixMax(wooden_bars[::-1])
    
    for i in range(1, len(wooden_bars) - 1):
        
        left_ceiling = prefixMax[i]
        right_ceiling = suffixMax[i]
        min_ceiling = min(left_ceiling, right_ceiling)
        if min_ceiling > wooden_bars[i][1]:
            total += (min_ceiling - wooden_bars[i][1]) * wooden_bars[i][0]
    return total
    
    
prefixMax[i] : tallest wooden bar up to i-1-th position
suffixMax[i] : tallest wooden bar after i+1-th position
prefixMax =  [0,0,0,0,0,0]
            [6,0,0,0,0,0]
            [6,6,0,0,0,0]
            [6,6,6,6,6,6]  
            [6,6,6,6,6,6]
            
def getPrefixMax(wooden_bars):

    prefixMax = [0] * len(wooden_bars)
    prefixMax[0] = wooden_bars[0][1]
    for i in range(1, len(wooden_bars)):
        prefixMax[i] = max(wooden_bars[i][1], prefixMax[i-1])
    
    return prefixMax
    
edge case :
1. equal heights (single wooden bar)
2. pyramid heights 
3. inverted pyramid heights

    
    


