import sys

# the index into a memory array, AKA location, address, pointer

# 1, PRINT_BEEJ
# 2, HALT
# 3, SAVE_REG store a value in a register
# 4, PRINT_REG print the register value in decimal
# 5, PUSH
# 6, POP

# think of a big array of bytes, 8-bits per byte
memory = [0] * 256

# registers[4] = 37
registers = [0] * 8

registers[7] = 0xF4  # Stack pointer

# load the program file
address = 0

if len(sys.argv) != 2:
    print("usage: comp.py progname")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            temp = line.split()
            if len(temp) == 0:
                continue
            if temp[0][0] == "#":
                continue
            try:
                memory[address] = int(temp[0])
            except ValueError:
                print(f"Invalid num: {temp[0]}")
                sys.exit(1)
            address += 1


except FileNotFoundError:
    print(f"Couldn't open {sys.argv[1]}")
    sys.exit(2)

if address == 0:
    print("Program was empty")
    sys.exit(3)
# print(memory[:10])

# sys.exit(0)

running = True

pc = 0  # program counter, the index into memory of the currently_executing instruction

while running:
    ir = memory[pc]  # instruction register

    if ir == 1:
        print("Beej!")
        pc += 1

    elif ir == 2:
        running = False
        pc += 1

    elif ir == 3:  # SAVE_REG
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        registers[reg_num] = value
        pc += 3  # increment by the # of operands

    elif ir == 4:  # PRINT_REG
        reg_num = memory[pc + 1]
        print(registers[reg_num])
        pc += 2

    elif ir == 5:  # PUSH
        # decrement stack pointer
        registers[7] -= 1

        # get val from register
        reg_num = memory[pc + 1]
        value = registers[reg_num]  # this is the value we want to push

        # store it on the stack
        top_of_stack_addr = registers[7]
        memory[top_of_stack_addr] = value

        pc += 2

        print(f"stack: {memory[0xE4:0xF4]}")

    # this code doesn't work for the beej machine, but does for LS-8

    # number_of_arguments = ir >> 6
    # size_of_this_instruction = number_of_arguments + 1
    # pc += size_of_this_instruction
