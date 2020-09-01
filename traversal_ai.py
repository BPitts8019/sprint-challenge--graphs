from queue import Queue, LifoQueue
from world import World
from room import Room


def isRoomVisited():
    pass


def buildTraversalPath(world: World):
    isDeadEnd = False
    rtn_path = []
    traversal_stack = LifoQueue()
    visited_rooms = {}
    opp_direction = {
        "n": "s",
        "e": "w",
        "s": "n",
        "w": "e"
    }

    traversal_stack.put((world.starting_room, []))
    while not isDeadEnd and not traversal_stack.empty():
        cur_room, room_path = traversal_stack.get()
        exits = cur_room.get_exits()

        if cur_room.id not in visited_rooms:
            # set connection to previous room as current room id
            if len(room_path) > 0:
                prev_room = cur_room.get_room_in_direction(
                    opp_direction[room_path[-1]])
                visited_rooms[prev_room.id][room_path[-1]] = cur_room.id

            # add current room to visited
            visited_rooms[cur_room.id] = {}

            # add each doorway to current room dataset
            for direction in exits:
                visited_rooms[cur_room.id][direction] = None
                traversal_stack.put((cur_room.get_room_in_direction(
                    direction), room_path + [direction]))

        # if we found a dead end, stop
        if len(exits) == 1 and len(room_path) > 0 and visited_rooms[cur_room.id][opp_direction[room_path[-1]]] is not None:
            isDeadEnd = True
            rtn_path = room_path

    return rtn_path
