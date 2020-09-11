from util import Stack, Queue

"""
from readme: You may find the commands player.current_room.id, player.current_room.get_exits() and player.travel(direction) useful.
"""

class Graph():
    def __init__(self, player):
        self.rooms = {}
        self.player = player
        self.stack = Stack()
        self.player = player
        self.opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    def add_room(self, room_id):
        """
        Add a vertex to the graph.
        must add the room in format room_id = {'n': "?", 'e': "?"}
        1. Get exits from room id
        2. add each direction as keys to the dictionary 
        3. add "?" as the value to each key
        """
        exits = self.player.current_room.get_exits()
        self.rooms[room_id] = {}
        for i in exits:
            self.rooms[room_id][i] = "?" 
    def find_unexplored_directions(self, room_id):
        exits = [k for k,v in self.rooms[room_id].items() if v == "?"]
        return exits


    def dft(self, path):
        stack = self.stack

        starting_room = self.player.current_room.id
        #add starting room to graph and push it on to stack
        starting_room = self.player.current_room.id
        self.add_room(starting_room)
        print(self.rooms)
        
        #find direction to move in 
        unexplored_directions = self.find_unexplored_directions(starting_room)
        #move it
        direction = unexplored_directions.pop()
        #travel that direction
        self.player.travel(direction)
        #add direction traveled to path and its opposite direction to stack
        path.append(direction)
        stack.push(self.opposite_directions[direction])
        new_room = self.player.current_room.id
        #add it to graph
        self.add_room(new_room)
        self.rooms[new_room][self.opposite_directions[direction]] = starting_room
        print(self.rooms)

        while stack.size() > 0:
            current_room = self.player.current_room.id
            #find current rooms unexplored exits
            unexplored_directions = self.find_unexplored_directions(current_room)
            #if there are unexplored exits:
            if len(unexplored_directions) > 0:
                #travel in that one of them
                direction_to_travel = unexplored_directions.pop()  
                self.player.travel(direction_to_travel)     
                #add opposite of direction traveled to stack 
                stack.push(self.opposite_directions[direction_to_travel])
                #add direction traveled to path
                path.append(direction_to_travel)
                #if new room not in graph we should add it
                new_room = self.player.current_room.id
                if new_room not in self.rooms.keys():
                    self.add_room(new_room)
                #update both new room's dictionary and current room's to show each other
                self.rooms[current_room][direction_to_travel] = new_room
                self.rooms[new_room][self.opposite_directions[direction_to_travel]] = current_room
            #if there are no unexplored rooms:
            else:
                #pop from stack and move that direction
                back_track_direction = stack.pop()
                self.player.travel(back_track_direction)
                path.append(back_track_direction)

        return path

                 

            


        




        
                




