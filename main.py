import sys,os
A_Register = None
B_Register = None
def func(instruction, a_register, b_register, addresses):
    return
with open("./main.ct","r") as file:
    addresses = file.readlines()
    program_counter = 0
    program_start = 0
    firstpass = True
    while program_counter < len(addresses):
        #take in the information from the file
        instruction = addresses[program_counter]
        #determine the action of the instruction
        if "CTFF" not in instruction:
                func(instruction, A_Register, B_Register, addresses)
                #break down the instruction
                instruction = instruction.split(" ")
                if instruction[0] == "CT00":
                    pass
                elif instruction[0] == "CTA1":
                    A_Register = addresses[int(instruction[1])].strip("\n")
                elif instruction[0] == "CTA2":
                    A_Register = int(instruction[1])
                elif instruction[0] == "CTA3":
                    A_Register = str(addresses[program_counter][5:].strip("\n"))
                elif instruction[0] == "CTB1":
                    B_Register = addresses[int(instruction[1])].strip("\n")
                elif instruction[0] == "CTB2":
                    B_Register = int(instruction[1])
                elif instruction[0] == "CTB3":
                    B_Register = str(addresses[program_counter][5:].strip("\n"))
                elif instruction[0] == "CTC1":
                    B_Register += A_Register
                elif instruction[0] == "CTC2":
                    A_Register += B_Register
                elif instruction[0] == "CTC3":
                    B_Register -= A_Register
                elif instruction[0] == "CTC4":
                    A_Register -= B_Register
                elif instruction[0] == "CTPP":
                    code = addresses[program_counter][5:]
                    exec(code)
                elif instruction[0] == "CTPA":
                    print(A_Register)
                elif instruction[0] == "CTPB":
                    print(B_Register)
                elif instruction[0] == "CTAI":
                    A_Register = int(A_Register)
                elif instruction[0] == "CTAS":
                    A_Register = str(A_Register)
                elif instruction[0] == "CTBI":
                    B_Register = int(B_Register)
                elif instruction[0] == "CTBS":
                    B_Register = str(B_Register)
                elif instruction[0] == "CTJJ":
                    print(f"Jumping to {int(instruction[1])}")
                    program_counter = int(instruction[1])
                    pass
                elif instruction[0] == "CTJA":
                    print(f"Jumping to {A_Register}")
                    program_counter = A_Register
                    pass
                elif instruction[0] == "CTJB":
                    print(f"Jumping to {B_Register}")
                    program_counter = B_Register
                    pass
                    
        elif "CTFF" in instruction:
            exit()
        program_counter+=1