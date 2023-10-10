# Dijkstra algorithm input as matrix and output as path

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
        u = min(unvisited, key=lambda node: dist[node])

        # Remove u from the unvisited list
        unvisited.remove(u)

        # Check neighbors of u
        for v in range(n):
            if matrix[u][v] > 0:  # Only consider neighbors with non-zero distance
                alt = dist[u] + matrix[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    # Reconstruct the shortest path and calculate its cost
    path = []
    u = end
    path_cost = 0
    while prev[u] is not None:
        path.insert(0, u)
        path_cost += matrix[u][prev[u]]
        u = prev[u]
    # path.insert(0, start)
    
    return path, path_cost

def pass_value (node_list, matrix,start):
      index=0;
      path=[];
      correct_path=[];
    #   result_grid=[0 for x in range(len(node_list))];
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
      return min_value,correct_path,index;
             
      


#Read input from the file
truck_name_list=[];
output_file=[];
with open("input.txt", "r") as Input_File:
    # Get the count of comma-separated values
    first_Line = Input_File.readline()
    count = first_Line.count(",") + 1

    # Create the n*n matrix to store those values
    matrix = [[0 for _ in range(count)] for _ in range(count)]

    # Read the file and store the values in the matrix
    Input_File.seek(0)
    for i in range(count):
        line = Input_File.readline()
        line = line.strip().split(",")  # Split by comma and remove newline character
        for j in range(count):
            if line[j] == "N":
                matrix[i][j] = 0;
            else:
                matrix[i][j] = int(line[j])

    Truck_List=[];
    Trucks_details=Input_File.readlines();
    for i in Trucks_details:
        capacity=i.split("#");
        truck_name_list.append(capacity[0]);
        Truck_List.append(int(capacity[1]));


# Truck_List=[2,3];

city_list=[i for i in range (1,count)];
    
count_city=len(city_list);
latest_cost=float('inf');
for z in range (0,count*count):
        
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
            truck=city_list[start_point:(end_point+Truck_List[i])];
            start_point+=Truck_List[i];
            end_point+=Truck_List[i];
            index_truck=0;
            x=len(truck);
            for j in range (0,x+1):
                total_cost+=truck_cost;
                if (j==0) :  
                   truck_cost,truck_path,index_truck=pass_value(truck,matrix,0);
                
                else:
                    truck_cost,truck_path,index_truck=pass_value(truck,matrix,index_truck);
                
                    
                if (len(truck)!=0):
                    truck.remove(index_truck);
                
            #  for i in truck_path:
            #      print(i,end=" ");
                one_truck_path.extend(truck_path);
            
            # print(one_truck_path);
            output_file.append(f"{truck_name_list[i]}#{','.join(chr(ord('a') + node) for node in one_truck_path)}")
            
            # full_truck_path.append(one_truck_path);
            one_truck_path.clear();
            

        
            
        if (total_cost<latest_cost):
            latest_cost=total_cost;

            with open("210043V.txt", "w") as output:
                pass
                output.write('\n'.join(output_file))
                output.write(f"\n{total_cost}")
        output_file.clear();
            


                
            


        







