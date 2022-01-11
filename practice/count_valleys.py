steps = 8
path = UDDDUDUU
op -> 1

_/\      _
   \    /
    \/\/

    
def valleys(path, steps):
  each_step, count = 0,0
  path = path.split()
  for i in path:
    if i == 'D':
      each_step-=1
    else:
      each_step+=1
    if each_step == 0 and  i == 'U':
      count+=1
  return count    
    
   
    
  
