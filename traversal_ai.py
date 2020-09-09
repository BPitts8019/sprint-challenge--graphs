from queue import Queue, LifoQueue
from world import World
from room import Room
import random


def getUnexploredExits(cur_room, visited_rooms):
    unexplored_exits = []
    for direction in cur_room.get_exits():
        if direction not in visited_rooms[cur_room.id]:
            unexplored_exits.append(direction)

    return unexplored_exits


def findDeadEnd(starting_room, visited_rooms):
    search_stack = LifoQueue()
    opp_direction = {
        "n": "s",
        "e": "w",
        "s": "n",
        "w": "e"
    }

    search_stack.put((starting_room, -1, []))
    while not search_stack.empty():
        cur_room, prev_room_id, room_path = search_stack.get()
        exits = cur_room.get_exits()
        if cur_room.id not in visited_rooms:
            print(cur_room)
            # Mark room as visited
            visited_rooms[cur_room.id] = set()

            # Mark directions moved as explored
            if len(room_path) > 0:
                visited_rooms[prev_room_id].add(room_path[-1])
                visited_rooms[cur_room.id].add(opp_direction[room_path[-1]])

            if len(exits) == 1 and prev_room_id in visited_rooms:
                # reached a dead end; go back to a room with unexpolored exits
                return (cur_room, room_path)
            else:
                # choose a random unexplored direction
                direction = random.choice(
                    getUnexploredExits(cur_room, visited_rooms))
                search_stack.put((cur_room.get_room_in_direction(
                    direction), cur_room.id, room_path + [direction]))


def findNextUnexploredRoom(starting_room, visited_rooms):
    pass


# def bft(self, starting_vertex):
#     """
#     Print each vertex in breadth-first order
#     beginning from starting_vertex.
#     """
#     search_queue = Queue()
#     visited_verticies = set()

#     search_queue.put(starting_vertex)
#     while not search_queue.empty():
#         cur_vertex = search_queue.get()
#         if cur_vertex not in visited_verticies:
#             print(cur_vertex)
#             visited_verticies.add(cur_vertex)
#             for connection in self.get_neighbors(cur_vertex):
#                 search_queue.put(connection)


def buildTraversalPath(world: World):
    visited_rooms = {}
    traversal_path = []
    cur_room = world.starting_room

    while cur_room is not None:
        result = findDeadEnd(cur_room, visited_rooms)
        cur_room = result[0]
        traversal_path += result[1]

        cur_room = findNextUnexploredRoom(cur_room, visited_rooms)

    return traversal_path
