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


def buildTraversalPath(world: World):
    traversal_stack = LifoQueue()
    visited_rooms = {}
    opp_direction = {
        "n": "s",
        "e": "w",
        "s": "n",
        "w": "e"
    }

    traversal_stack.put((world.starting_room, -1, []))
    while not traversal_stack.empty():
        cur_room, prev_room_id, room_path = traversal_stack.get()
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
                return room_path
            else:
                # choose a random unexplored direction
                direction = random.choice(
                    getUnexploredExits(cur_room, visited_rooms))
                traversal_stack.put((cur_room.get_room_in_direction(
                    direction), cur_room.id, room_path + [direction]))

    # isDeadEnd = False
    # rtn_path = []
    # traversal_stack = LifoQueue()
    # visited_rooms = {}
    # opp_direction = {
    #     "n": "s",
    #     "e": "w",
    #     "s": "n",
    #     "w": "e"
    # }

    # traversal_stack.put((world.starting_room, []))
    # while not isDeadEnd and not traversal_stack.empty():
    #     cur_room, room_path = traversal_stack.get()
    #     exits = cur_room.get_exits()

    #     if cur_room.id not in visited_rooms:
    #         # set connection to previous room as current room id
    #         if len(room_path) > 0:
    #             prev_room = cur_room.get_room_in_direction(
    #                 opp_direction[room_path[-1]])
    #             visited_rooms[prev_room.id][room_path[-1]] = cur_room.id

    #         # add current room to visited
    #         visited_rooms[cur_room.id] = {}

    #         # add each doorway to current room dataset
    #         for direction in exits:
    #             visited_rooms[cur_room.id][direction] = None
    #             traversal_stack.put((cur_room.get_room_in_direction(
    #                 direction), room_path + [direction]))

    #     # if we found a dead end, stop
    #     if len(exits) == 1 and len(room_path) > 0 and visited_rooms[cur_room.id][opp_direction[room_path[-1]]] is not None:
    #         isDeadEnd = True
    #         rtn_path = room_path

    # return rtn_path
