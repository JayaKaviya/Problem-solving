n=2
m=str(n) 
l=['2','3','4','5','6','7','8','9','0'] 
if m in l: 
    print("false")
else:  
    while n!=1: 
        n=sum([int(i)**2 for i in str(n)]) 
    print("true")
        
   




#  while int(m)!=1:
#         for i in m: 
#               k=int(i)**2 
#               a=a+k 
#         m,a=str(a),0 
#             # if int(m)==1: 
#    return "true" 
      
