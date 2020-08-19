# the index into a memory array, AKA location, address, pointer

# 1, PRINT_BEEJ
# 2, HALT
# 3, SAVE_REG store a value in a register
# 4, PRINT_REG print the register value in decimal

# think of a big array of bytes, 8-bits per byte
memory = [
    1,  # PRINT_BEEJ
    #
    3,  # SAVE_REG R4 37, instruction itself is also called 'opcode'
    4,  # 4 and 37 are arguments to SAVE_REG, also called "operands" //could theoretically be written like SAVE_REG(4, 37)
    37,
    #
    4,  # PRINT_REG R4
    4,
    #
    2,  # HALT
]

# registers[4] = 37
registers = [0] * 8

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

    # this code doesn't work for the beej machine, but does for LS-8

    # number_of_arguments = ir >> 6
    # size_of_this_instruction = number_of_arguments + 1
    # pc += size_of_this_instruction
