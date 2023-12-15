#Relatioship Status
def relationship_status(from_member, to_member, social_graph):
   

    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"
        else:
            return "follower"
    
    if from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by"
    
    return "no relationship"

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
from_member = "@bongolpoc"
to_member = "@joaquin"
result = relationship_status(from_member, to_member, social_graph)
print(result) 
#Example


#Tic-Tac-Toe board Evaluation
def tic_tac_toe(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if len(set([row[col] for row in board])) == 1 and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != '':
        return board[0][0]
    if len(set([board[i][len(board)-1-i] for i in range(len(board))])) == 1 and board[0][len(board)-1] != '':
        return board[0][len(board)-1]

    return "NO WINNER"

board1 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['O', '', 'X'],
]

board2 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
]

board3 = [
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
    ['X', 'X', 'O'],
]

board4 = [
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['O', '', 'O'],
]

board5 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', 'O'],
]

board6 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', ''],
]

board7 = [
    ['X', 'X', 'O', ''],
    ['O', 'X', 'O', 'O'],
    ['X', '', '', 'O'],
    ['O', 'X', '', '']
]
print(tic_tac_toe(board1))  
print(tic_tac_toe(board2)) 
print(tic_tac_toe(board3))  
print(tic_tac_toe(board4))  
print(tic_tac_toe(board5)) 
print(tic_tac_toe(board6)) 
print(tic_tac_toe(board7)) 
#Example


#ETA calculator
#ETA calculator
def eta(first_stop, second_stop, route_map):
    # Extract all unique stops from the route map
    stops = set(stop for legs in route_map.values() for leg in legs.keys() for stop in leg)
    distances = {stop: float('inf') for stop in stops}
    distances[first_stop] = 0
    visited = set()

    # Dijkstra's algorithm
    while len(visited) < len(stops):
        current_stop = min(
            (stop for stop in stops if stop not in visited),
            key=lambda x: distances[x]
        )
        visited.add(current_stop)

        for legs in route_map.values():
            for leg, info in legs.items():
                if leg[0] == current_stop:
                    neighbor_stop = leg[1]
                    total_time = distances[current_stop] + info['travel_time_mins']
                    if total_time < distances[neighbor_stop]:
                        distances[neighbor_stop] = total_time

    # Return the time to travel from first_stop to second_stop
    return distances[second_stop]

legs_1 = {
    ('a1', 'a2'): {'travel_time_mins': 10},
    ('a2', 'b1'): {'travel_time_mins': 10230},
    ('b1', 'a1'): {'travel_time_mins': 1}
}

legs_2 = {
    ("upd", "admu"): {"travel_time_mins": 10},
    ("admu", "dlsu"): {"travel_time_mins": 35},
    ("dlsu", "upd"): {"travel_time_mins": 55}
}

route_map_1 = {'a1': legs_1, 'a2': legs_1, 'b1': legs_1}
route_map_2 = {'upd': legs_2, 'admu': legs_2, 'dlsu': legs_2}

print("Sample Data for legs_1:")
print("upd to dlsu:", eta('upd', 'dlsu', route_map_2))
print("admu to upd:", eta('admu', 'upd', route_map_2))
print("dlsu to admu:", eta('dlsu', 'admu', route_map_2))
print("upd to admu:", eta('upd', 'admu', route_map_2))
print("admu to dlsu:", eta('admu', 'dlsu', route_map_2))

#Example
