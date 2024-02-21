from modules import *
A_Register = None
B_Register = None
variables = {}
Functions = []
ExtraAddressSpace = [] #for adding files
screen = None
VRAM = None
LastVRAM = None
RAM = [ 0 for _ in range(4096) ]
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)
def Screen_update(pos=(0,0)):
    global VRAM,LastVRAM,screen
    #create a dict of all the items in VRAM that are different than in LastVRAM with the format item:pos
    changes = {VRAM[i]:(i%500,i//500) for i in range(len(VRAM)) if VRAM[i] != LastVRAM[i]}
    for change in changes.keys():
        # Get the position of the change
        pos = changes[change]
        # Get the color from VRAM and convert it to hexadecimal
        color_hex = hex(change)[2:].zfill(6)
        # Split the color into RR, GG, BB parts
        color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        # Set the color at the current position
        screen.set_at(pos, color)
    LastVRAM = VRAM.copy()
def interpret(File,counter_start=0):
    global A_Register,B_Register,screen,VRAM,variables,Functions,LastVRAM
    global ExtraAddressSpace
    with open(f"./{File}{'.ct' if '.ct' not in File else ''}","r") as file:
        addresses = file.readlines()
        program_counter = counter_start
        while program_counter < len(addresses):
            #take in the information from the file
            instruction = addresses[program_counter]
            #break down the instruction
            instruction = instruction.split(" ")
            instruction[-1]=instruction[-1].strip()
            match instruction[0].strip():
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
                    data = " ".join(instruction).strip()
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
                    if len(instruction):
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
                    addr = int(instruction.pop(0).strip())
                    if addr in variables.keys():
                        program_counter = variables[addr]
                        continue
                    else:
                        program_counter = int(addr)-1 if int(addr)-1 >= 0 else int(addr)
                        continue
                case "JUMPA":
                    program_counter = A_Register
                    continue
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
                        continue
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
                case "PEND":
                    return
                case "INITPYGAME":
                    screen = pygame.display.set_mode((500,500))
                    VRAM = [0 for _ in range(500*500)]
                    LastVRAM = [0 for _ in range(500*500)]
                case "VRAM":
                    if VRAM:
                        instruction.pop(0)
                        x = int(instruction.pop(0)) if instruction[0].isdigit() else variables[instruction.pop(0)] if instruction[0] in variables.keys() else print("Invalid VRAM address") if not instruction[0].isdigit() else print("VRAM Address must be a variable or int")
                        y = int(instruction.pop(0)) if instruction[0].isdigit() else variables[instruction.pop(0)] if instruction[0] in variables.keys() else print("Invalid VRAM address") if not instruction[0].isdigit() else print("VRAM Address must be a variable or int")
                        r = hex(int(instruction.pop(0)))[2:] if instruction[0].isdigit() else hex(variables[instruction.pop(0)])[2:] if instruction[0] in variables.keys() else eval(instruction.pop(0)) if "RAM" in instruction[0] else print("Invalid Color R") if not instruction[0].isdigit() else print("VRAM Address must be a variable or int") if not "RAM" in instruction[0] else print("VRAM Address must be a variable or int")
                        g = hex(int(instruction.pop(0)))[2:] if instruction[0].isdigit() else hex(variables[instruction.pop(0)])[2:] if instruction[0] in variables.keys() else eval(instruction.pop(0)) if "RAM" in instruction[0] else print("Invalid Color G") if not instruction[0].isdigit() else print("VRAM Address must be a variable or int") if not "RAM" in instruction[0] else print("VRAM Address must be a variable or int")
                        b = hex(int(instruction.pop(0)))[2:] if instruction[0].isdigit() else hex(variables[instruction.pop(0)])[2:] if instruction[0] in variables.keys() else eval(instruction.pop(0)) if "RAM" in instruction[0] else print("Invalid Color B") if not instruction[0].isdigit() else print("VRAM Address must be a variable or int") if not "RAM" in instruction[0] else print("VRAM Address must be a variable or int")
                        #print(x,y,r,g,b, x+y*50)
                        color = int(f"0x{r}{g}{b}",16)
                        VRAM[x+y*500] = color
                        Screen_update()
                    else:
                        print("VRAM (pygame) not initialized")
                case "PYGAME":
                    instruction.pop(0)
                    instruction2 = instruction.pop(0)
                case "RAM":
                    instruction.pop(0)
                    addr = int(instruction.pop(0))
                    data = instruction.pop(0)
                    if addr > 4096:
                        print("RAM address out of bounds")
                    else:
                        if data in variables.keys() and type(variables[data]) is int:
                            RAM[addr] = variables[data]
                        elif data.isdigit():
                            RAM[addr] = int(data)
                        elif data.startswith("0x"):
                            RAM[addr] = int(data,16)
                case "PUSHFRAME":
                    if "DEBUG" in addresses[0]:
                        Debug_instruction = addresses[0].strip().split(" ")
                        match Debug_instruction[0]:
                            case "PRINTDEBUG":
                                print(f"PUSHED FRAME {clock.get_fps()}")
                            case "GRAPHDEBUG":
                                fps = font.render(str(int(clock.get_fps()//1)),True,(255,255,255))
                                rect = pygame.surface.Surface((fps.get_width(),fps.get_height()))
                                rect.fill((0,0,0))
                                if len(Debug_instruction) == 2:
                                    if Debug_instruction[1] == "1":
                                        screen.blit(rect,(0,0))
                                        screen.blit(fps,(0,0))
                                    elif Debug_instruction[1] == "2":
                                        screen.blit(rect,(0,500-fps.get_height()))
                                        screen.blit(fps,(0,500-fps.get_height()))   
                                    elif Debug_instruction[1] == "3":
                                        screen.blit(rect,(500-fps.get_width(),0))
                                        screen.blit(fps,(500-fps.get_width(),0))
                                    elif Debug_instruction[1] == "4":
                                        screen.blit(rect,(500-fps.get_width(),500-fps.get_height()))
                                        screen.blit(fps,(500-fps.get_width(),500-fps.get_height())) 
                                else:
                                    screen.blit(rect,(500-fps.get_width(),0))
                                    screen.blit(fps,(500-fps.get_width(),0))
                    pygame.display.flip()
                    if len(instruction) == 2:
                        if instruction[1].isdigit():
                            clock.tick(int(instruction[1]))
                        else:
                            CTERROR("Frame Rate Must be an Integer")
                    else:
                        clock.tick(60)
            program_counter+=1
            if screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
interpret("main")