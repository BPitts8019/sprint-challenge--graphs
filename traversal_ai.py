from queue import Queue, LifoQueue
from world import World
from room import Room


def goToDeadEnd(world: World, visited_rooms):
    traversal_stack = LifoQueue()
    traversal_path = []

    traversal_stack.put([world.starting_room])
    while not traversal_stack.empty():
        room_path = traversal_stack.get()
        prev_room: Room = None
        cur_room: Room = room_path[-1]

        # ensure current room is in dataset
        if cur_room.id not in visited_rooms:
            visited_rooms[cur_room.id] = {}
            # add each doorway to dataset
            for door in cur_room.get_exits():
                visited_rooms[cur_room.id][door] = None

    return traversal_path


def buildTraversalPath(world: World):
    visited_rooms = {}
    rtn_path = []

    rtn_path += goToDeadEnd(world, visited_rooms)

    return rtn_path
