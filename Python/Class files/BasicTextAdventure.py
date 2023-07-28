
'''This program implements a simple text-based 
adventure game where players navigate through different 
rooms, interact with objects, and make choices that 
affect the outcome of the story. Players can move 
between rooms by entering cardinal directions 
(north, south, east, west), and the game responds 
with the current room's description. 
The game loop allows players to continue 
exploring until they choose to exit.'''

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.objects = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_object(self, object_name, description):
        self.objects[object_name] = description

# Create rooms and connect them with exits
room1 = Room("Living Room", "You are in the cozy living room.")
room2 = Room("Kitchen", "The kitchen is clean and tidy.")
room1.add_exit("north", room2)
room2.add_exit("south", room1)

# Usage example: Implement the game loop and interactions
current_room = room1
while True:
    print(current_room.name)
    print(current_room.description)

    command = input("What do you want to do? ")
    if command in current_room.exits:
        current_room = current_room.exits[command]
    elif command == "exit":
        break
    else:
        print("Invalid command.")