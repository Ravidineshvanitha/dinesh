def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])
    return (c)
print(shuffle([1,2,3,8],[9,14,5,0,7,3]))