from queue import Queue, LifoQueue
from world import World
from room import Room


def isRoomVisited():
    pass


def goToDeadEnd(world: World, visited_rooms):
    traversal_stack = LifoQueue()
    traversal_path = []
    isDeadEnd = False

    traversal_stack.put((world.starting_room, []))
    while not isDeadEnd and not traversal_stack.empty():
        cur_room, room_path = traversal_stack.get()
        exits = cur_room.get_exits()

        # set connection to previous room as visited (bi-directional)

        # ensure current room is in dataset
        if cur_room.id not in visited_rooms:
            visited_rooms[cur_room.id] = {}
            # add each doorway to dataset
            for direction in exits:
                visited_rooms[cur_room.id][direction] = None
                traversal_stack.put((cur_room.get_room_in_direction(
                    direction), room_path + [direction]))

        # if we found a dead end, stop
        if len(exits) == 1 and visited_rooms[cur_room.id][exits[0]]):
            isDeadEnd=True
            traversal_path=room_path

    return traversal_path


def buildTraversalPath(world: World):
    visited_rooms={}
    rtn_path=[]

    rtn_path += goToDeadEnd(world, visited_rooms)

    return rtn_path
