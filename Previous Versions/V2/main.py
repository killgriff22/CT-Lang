import sys,os
A_Register = None
B_Register = None
window = None
Functions = []
ExtraAddressSpace = [] #for adding files
def interpret(File,counter_start=0):
    global A_Register,B_Register,window
    global ExtraAddressSpace
    with open(f"./{File}.ct","r") as file:
        addresses = file.readlines()
        program_counter = counter_start
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
                        Functions.append([instruction[1], int(instruction[2].strip("\n")),File])
                    elif instruction[0] == "CALL":
                        for function in Functions:
                            if function[0] == instruction[1] and File == function[2]:
                                B_Register = instruction[2]
                                A_Register = program_counter
                                program_counter = int(function[1])
                            elif function[0] == instruction[1] and not File == function[2]:
                                B_Register = instruction[2]
                                A_Register = program_counter
                                interpret(function[2],function[1])
                                program_counter=A_Register
                    elif instruction[0] == "IMPORT":
                        interpret(instruction[1].strip("\n"))
                    elif instruction[0] == "CJUMP":
                        Address = int(instruction[2].strip("\n"))
                        jump=False
                        if instruction[1] == ">":
                            if A_Register > B_Register:
                                jump=True
                        elif instruction[1] == "<":
                            if A_Register < B_Register:
                                jump=True
                        elif instruction[1] == "=":
                            if A_Register == B_Register:
                                jump=True
                        elif instruction[1] == ">=":
                            if A_Register >= B_Register:
                                jump=True
                        elif instruction[1] == "<=":
                            if A_Register <= B_Register:
                                jump=True
                        elif instruction[1] == "!=":
                            if not A_Register == B_Register:
                                jump=True
                        elif instruction[1] == "!<":
                            if not A_Register < B_Register:
                                jump=True
                        elif instruction[1] == "!>":
                            if not A_Register > B_Register:
                                jump=True
                        elif instruction[1] == "!>=":
                            if not A_Register >= B_Register:
                                jump = True
                        elif instruction[1] == "!<=":
                            if not A_Register <= B_Register:
                                jump = True
                        if jump:
                            program_counter = Address
                    elif instruction[1] == "LOADDISK":
                        path = addresses[program_counter][9:]
                        print("loading ",path)
                        with open(path,"r") as f:
                            ExtraAddressSpace = f.readlines()
                            f.close()
                    elif instruction[0] == "READEA":
                        print(B_Register,len(ExtraAddressSpace))
                        A_Register = ExtraAddressSpace[B_Register].strip("\n")
                    elif instruction[0] == "READEB":
                        B_Register = ExtraAddressSpace[A_Register].strip("\n")
            elif "PEND" in instruction:
                return
            program_counter+=1
interpret("main")