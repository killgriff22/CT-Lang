import sys,os
A_Register = None
B_Register = None
Functions = []
with open("./main.ct","r") as file:
    addresses = file.readlines()
    program_counter = 0
    program_start = 0
    firstpass = True
    while program_counter < len(addresses):
        #take in the information from the file
        instruction = addresses[program_counter]
        #determine the action of the instruction
        if "PEND" not in instruction:
                #break down the instruction
                instruction = instruction.split(" ")
                if instruction[0] == "NOOP":
                    pass
                elif instruction[0] == "LOADA":
                    A_Register = addresses[int(instruction[1])].strip("\n")
                elif instruction[0] == "INAI":
                    A_Register = int(instruction[1])
                elif instruction[0] == "INAS":
                    A_Register = str(addresses[program_counter][5:].strip("\n"))
                elif instruction[0] == "LOADB":
                    B_Register = addresses[int(instruction[1])].strip("\n")
                elif instruction[0] == "INBI":
                    B_Register = int(instruction[1])
                elif instruction[0] == "INBS":
                    B_Register = str(addresses[program_counter][5:].strip("\n"))
                elif instruction[0] == "B+A":
                    B_Register += A_Register
                elif instruction[0] == "A+B":
                    A_Register += B_Register
                elif instruction[0] == "B-A":
                    B_Register -= A_Register
                elif instruction[0] == "A-B":
                    A_Register -= B_Register
                elif instruction[0] == "PY":
                    code = addresses[program_counter][3:]
                    exec(code)
                elif instruction[0] == "PRINTA":
                    print(A_Register)
                elif instruction[0] == "PRINTB":
                    print(B_Register)
                elif instruction[0] == "AINT":
                    A_Register = int(A_Register)
                elif instruction[0] == "ASTR":
                    A_Register = str(A_Register)
                elif instruction[0] == "BINT":
                    B_Register = int(B_Register)
                elif instruction[0] == "BSTR":
                    B_Register = str(B_Register)
                elif instruction[0] == "JUMP":
                    print(f"Jumping to {int(instruction[1])}")
                    program_counter = int(instruction[1])
                    pass
                elif instruction[0] == "JUMPA":
                    print(f"Jumping to {A_Register}")
                    program_counter = A_Register
                    pass
                elif instruction[0] == "JUMPB":
                    print(f"Jumping to {B_Register}")
                    program_counter = B_Register
                    pass
                elif instruction[0] == "FUNC":
                    Functions.append([instruction[1], int(instruction[2].strip("\n"))])
                elif instruction[0] == "CALL":
                    for function in Functions:
                        if function[0] == instruction[1]:
                            B_Register = instruction[2]
                            A_Register = program_counter
                            program_counter = int(function[1])
        elif "PEND" in instruction:
            exit()
        program_counter+=1