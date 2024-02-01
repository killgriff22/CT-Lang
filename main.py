import sys,os
A_Register = None
B_Register = None
variables = {}
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
                    match instruction[0]:
                        case "NOOP":
                            pass
                        case "LOAD":
                            instruction.pop(0)
                            name  = instruction.pop(0)
                            addr = int(instruction.pop(0))
                            variables[name] = addresses[addr]
                        case "IN":
                            instruction.pop(0)
                            name  = instruction.pop(0)
                            type_ = instruction.pop(0).lower()
                            data  = " ".join(instruction)
                            ans   = input(data)
                            match type_.lower():
                                case "int":
                                    if ans.isdigit():
                                        variables[name] = int(ans)
                                case "str":
                                    variables[name] = ans
                                case "bool":
                                    variables[name] = eval(f"{ans[0].upper()}{ans[1:].lower()}")
                        case "SET":
                            instruction.pop(0)
                            name = instruction.pop(0)
                            data = " ".join(instruction)
                            if not data or data.lower() == "none":
                                variables[name] = None
                            elif data.isdigit():
                                variables[name] = int(data)
                            elif data.lower() in ["true","false"]:
                                variables[name] = eval(f"{data[0].upper()}{data[1:].lower()}")
                        case "ADD":
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                a = variables[instruction[0]]
                            elif instruction[0].isdigit():
                                a= int(instruction[0])
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                b = variables[instruction[0]]
                            elif instruction[0].isdigit():
                                b = int(instruction[0])
                            instruction.pop(0)
                            if bool(len(instruction)):
                                variables[instruction[0]] = a+b
                            else:
                                print(a+b)
                        case "SUB":
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                a = variables[instruction[0]]
                            elif instruction[0].isdigit():
                                a= int(instruction[0])
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                b = variables[instruction[0]]
                            elif instruction[0].isdigit():
                                b = int(instruction[0])
                            instruction.pop(0)
                            if bool(len(instruction)):
                                variables[instruction[0]] = a-b
                            else:
                                print(a-b)
                        case "PY":
                            instruction.pop(0)
                            code = " ".join(instruction)
                            exec(code)
                        case "PRINT":
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                name = instruction.pop(0)
                                print(name)
                            else:
                                print(" ".join(instruction))
                        case "JUMP":
                            instruction.pop(0)
                            if instruction[0] in variables.keys():
                                program_counter = int(instruction[0])
                        case "JUMPA":
                            program_counter = A_Register
                        case "FUNC":
                            Functions.append([instruction[1], int(instruction[2].strip("\n")),File])
                        case "CALL":
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
                        case "IMPORT":
                            interpret(instruction[1].strip("\n"))
                        case "CJUMP":
                            instruction.pop(0)
                            a = instruction.pop(0)
                            comparator = instruction.pop(0)
                            b = instruction.pop(0)
                            Address = int(instruction.pop(0))
                            if a in variables.keys():
                                a = variables[a]
                            elif a.isdigit():
                                a = int(a)
                            elif a.lower() in ["true","false","none"]:
                                a = eval(f"{a[0].upper()}{a[1:].lower()}")
                            if b in variables.keys():
                                b = variables[b]
                            elif b.isdigit():
                                b = int(b)
                            elif b.lower() in ["true","false","none"]:
                                b = eval(f"{b[0].upper()}{b[1:].lower()}")
                            jump=False
                            match comparator:
                                case ">":
                                    if a > b:
                                        jump=True
                                case "<":
                                    if a < b:
                                        jump=True
                                case "=":
                                    if a == b:
                                        jump=True
                                case ">=":
                                    if a >= b:
                                        jump=True
                                case "<=":
                                    if a <= b:
                                        jump=True
                                case "!=":
                                    if not a == b:
                                        jump=True
                                case "!<":
                                    if not a < b:
                                        jump=True
                                case "!>":
                                    if not a > b:
                                        jump=True
                                case "!>=":
                                    if not a >= b:
                                        jump = True
                                case "!<=":
                                    if not a <= b:
                                        jump = True
                            if jump:
                                program_counter = Address
                        case "LOADDISK":
                            path = addresses[program_counter][9:]
                            print("loading ",path)
                            with open(path,"r") as f:
                                ExtraAddressSpace = f.readlines()
                                f.close()
                        case "READEA":
                            instruction.pop(0)
                            name = instruction.pop(0)
                            addr = int(instruction.pop(0))
                            variables[name] = ExtraAddressSpace[addr].strip("\n")
            elif "PEND" in instruction:
                return
            program_counter+=1
interpret("main")