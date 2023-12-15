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


#ETA Calculator
def eta(first_stop, second_stop, route_map):
   
    legs = route_map

    # Get the travel time between the first and second stop
    travel_time = legs[(first_stop, second_stop)]['travel_time_mins']

    return travel_time

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

time_to_arrival = eta("upd", "admu", legs)

print("Estimated time of arrival from upd to admu: " + str(time_to_arrival) + " minutes")
#Example
