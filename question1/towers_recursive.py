# Towers of Hanoi Recursive solution

# keep track of number of moves - ideally should be 2^n
MOVE_COUNT = 0

# recursive function
def move_disks(n, source_peg, transfer_peg, extra_peg, tower_names):
    # I got which peg was which mixed up so the second transfer peg is the one holding the end tower
    # doesn't really change the solution since it could be printed differently so I'll leave it
    if n == 1:
        # move the physical disk from the list
        disk = source_peg.pop()
        transfer_peg.append(disk)
        
        print(f"Move disk {disk} from tower {tower_names[0]} to tower {tower_names[1]}")
        print_towers(source_peg, transfer_peg, extra_peg)
        return

    # move n-1 disks from source to transfer
    move_disks(n - 1, source_peg, extra_peg, transfer_peg, (tower_names[0], tower_names[2], tower_names[1]))

    # move the nth disk from source to extra
    disk = source_peg.pop()
    transfer_peg.append(disk)
    print(f"Move disk {disk} from tower {tower_names[0]} to tower {tower_names[1]}")
    print_towers(source_peg, transfer_peg, extra_peg)

    # move the n-1 disks from transfer to extra
    move_disks(n - 1, extra_peg, transfer_peg, source_peg, (tower_names[2], tower_names[1], tower_names[0]))

# print function for convenience
def print_towers(A, B, C):
    global MOVE_COUNT
    MOVE_COUNT = MOVE_COUNT + 1
    print("A: " + str(A))
    print("B: " + str(B))
    print("C: " + str(C))
    print("------------------- MOVE " + str(MOVE_COUNT))


def main():

    # initial state
    n = 3
    A = list(range(n, 0, -1)) # [3, 2, 1] - bottom to top
    B = []
    C = []

    print("----------- Initial state:")
    print_towers(A, B, C)

    # start the recursion
    # pass the tower lists themselves and a list of names for the print statements
    move_disks(n, A, B, C, ("A", "B", "C"))

    print("----------- Complete")


if __name__ == "__main__":
    main()