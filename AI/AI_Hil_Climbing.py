# To construct this problem I used the Simulated Annealing hill climbing method.
import sys
import random

def min_path(matrix, start, end):
    n = len(matrix)
    dist = [float('inf')] * n  # Initialize distances to infinity
    prev = [None] * n         # Initialize previous nodes as None
    dist[start] = 0           # Distance to start node is 0
    unvisited = list(range(n)) # Initially, all nodes are unvisited

    while unvisited:
        # Find the node with the minimum distance
        min_node = min(unvisited, key=lambda node: dist[node])

        # Remove min_node from the unvisited list
        unvisited.remove(min_node)

        # Check neighbors of min_node
        for v in range(n):
            if matrix[min_node][v] > 0:  # Only consider neighbors with non-zero distance
                full = dist[min_node] + matrix[min_node][v]
                if full < dist[v]:
                    dist[v] = full
                    prev[v] = min_node

    # Reconstruct the shortest path and calculate its cost
    path = []
    min_node = end
    path_cost = 0
    while prev[min_node] is not None:
        path.insert(0, min_node)
        path_cost += matrix[min_node][prev[min_node]]
        min_node= prev[min_node]
    
    
    return path, path_cost
# This function used for find the given list of nodes which node is near to the start node
def pass_value (node_list, matrix,start):
      index=0;
      path=[];
      correct_path=[];
    
      min_value=float('inf');
      for i in range (0,len(node_list)):
          path, min1=min_path(matrix,start,node_list[i]);
          if min_value>min1:
             correct_path.clear();
             min_value=min1;
             index=node_list[i];
             correct_path=path;
          else :
              path.clear();
      return min_value,correct_path,index;  # return the minimum cost and the path of the truck and the next node of the truck
             
      


#Read input from the file
truck_name_list=[];
output_file=[];
with open("input.txt", "r") as Input_File:
    # Get the count of comma-separated values
    first_Line = Input_File.readline()
    count = first_Line.count(",") + 1

    # Create the n*n matrix to store those values
    map_matrix = [[0 for _ in range(count)] for _ in range(count)]

    # Read the file and store the values in the matrix
    Input_File.seek(0)
    for i in range(count):
        line = Input_File.readline()
        line = line.strip().split(",")  # Split by comma and remove newline character
        for j in range(count):
            if line[j] == "N":
                map_matrix[i][j] = 0;
            else:
               map_matrix[i][j] = int(line[j])

    Truck_List=[];
    # add the all trucks_name and capacity to the list
    Trucks_details=Input_File.readlines();
    for i in Trucks_details:
      if (i!="\n"):
        capacity=i.split("#");
        truck_name_list.append(capacity[0]);
        Truck_List.append(int(capacity[1]));




city_list=[i for i in range (1,count)];# initialize the cit_list as the number of cities
    
count_city=len(city_list);
latest_cost=float('inf');
randoming_time=count**2; # choose the randoming time as the n^2 for hill climbing
for z in range (0,randoming_time):
        
 # shuffle the city-list according to the randoming time       
        random.shuffle(city_list);
        

        last_result=[];
        start_point=0;
        end_point=0;
        total_cost=0;
        full_truck_path=[];
        for i in range (0, len(Truck_List)):
            truck_path=[];
            
            one_truck_path=[];
            truck_cost=0;
 # break down the cities according to the truck capacity           
            truck=city_list[start_point:(end_point+Truck_List[i])];
            start_point+=Truck_List[i];
            end_point+=Truck_List[i];
            index_truck=0;
            x=len(truck);
            for j in range (0,x+1):
                total_cost+=truck_cost;
# calculate the cost of the truck and the path of the truck using the pass_value function
                if (j==0) :  
                   truck_cost,truck_path,index_truck=pass_value(truck,map_matrix,0);
                
                else:
                    truck_cost,truck_path,index_truck=pass_value(truck,map_matrix,index_truck);
                
                    
                if (len(truck)!=0):
                    truck.remove(index_truck);
                
           
                one_truck_path.extend(truck_path);
            
# append the truck name and the path of the truck to the output file
            output_file.append(f"{truck_name_list[i]}#{','.join(chr(ord('a') + node) for node in one_truck_path)}")
            
         
            one_truck_path.clear();
            

        
  # calculate the cost of the truck and the path of the truck using the pass_value function          
        if (total_cost<latest_cost and z >randoming_time/2):
# gave a constrainst for Simulated Annealing
            latest_cost=total_cost;
# write the output file
            with open("210043V.txt", "w") as output:
                pass
                output.write('\n'.join(output_file))
                output.write(f"\n{total_cost}")
        output_file.clear();