matrix=[1,2,3,4,5,6]
row_size=2
coloumn_size=3
Reward=[-0.1,-0.1,1,-0.1,-0.1,-0.05]
direct=[0,0,0,0,0,0]
directional=["North","East","South","West","Nothing"]
utility=[0,0,0,0,0,0]
path=[[coloumn_size,-1,1],[1,coloumn_size,-coloumn_size],[-coloumn_size,1,-1],[-1,-coloumn_size,coloumn_size],[0]]
Gama=0.999
Epsilon=0.01
difference=float("inf")# set the difference to infinity
iteration=0

def value (path_value,BOX,J,probability,Out_off):
     value=0;
  
     if (BOX%coloumn_size==0 and J==1): # check the wall and return to itself
          value=path_value + Gama*probability*utility[box-1]
     elif (BOX%coloumn_size==1 and J==-1 or Out_off=="true"):
          value=path_value + Gama*probability*utility[box-1]
     
     else :  # it not found wall 
          value=path_value+ Gama*probability*utility[(box+j)-1]
 
     return value
# check the utility converges using Epsilon and gamma
while (difference > (Epsilon*((1-Gama)/Gama))):
     iteration+=1
     
     utility_copy=utility.copy()
     for box in matrix:
            best_path=0
            for x in range (0,5):
                path_value=0
                k=0
                value1=0
                for j in path[x]:
                        if x==4:
                            path_value+=  Gama*1*utility[box-1]
                        elif ((box+j) in matrix)  :
                              if k==0:
                                
                                path_value=value(path_value,box,j,0.9,"false")
                              else:
                               
                                path_value=value(path_value,box,j,0.05,"false")
# check whether the going direction valid or invalid
                        else:
                             if k==0:
                               
                                  path_value=value(path_value,box,j,0.9,"true")
                             else:
                          
                           
                                 path_value=value(path_value,box,j,0.05,"true")
                        k+=1
# if path is optimal set to it               
                if (best_path <path_value) or x==0:
                     best_path=path_value
                     direct[box-1]=x
 # checking the terminate state                     
            if (iteration==1 and box==3):
             utility_copy[box-1]=(best_path + Reward[box-1])
            elif (iteration==100): # if not converge the utlity break the code
                 break;
            elif (box!=3):
                 utility_copy[box-1]=(best_path + Reward[box-1])
         
    
     differences = [abs(utility[s] - utility_copy[s]) for s in range(0, 6)]
     difference = max(differences)
     
     utility.clear()
     utility=utility_copy.copy()
     utility_copy.clear()
     
# print the utilities and the direction
for i in range (0,len(matrix)):
        
     print(directional[direct[i]]," ",utility[i])


print(iteration,difference)