
def script_input():
    code_list = []
    base_code = input("\n>>> ")
    for char in base_code:
        code_list.append(char)
    return code_list

def command_script(code_list):
    current_cell = 0
    array_tape = [0] * 30000
    command = 0
    while command < len(code_list):
    
        if code_list[command] == ">":
            current_cell += 1
        elif code_list[command] == "<":
            current_cell -= 1
        elif code_list[command] == "+":
            array_tape[current_cell] += 1
            if array_tape[current_cell] > 255:
                array_tape[current_cell] -= 256
        elif code_list[command] == "-":
            array_tape[current_cell] -= 1
            if array_tape[current_cell] < 0:
                array_tape[current_cell] += 256
        elif code_list[command] == ".":
            print(chr(array_tape[current_cell]),end = "")
        elif code_list[command] == ",":
            current_input = input(" ")
            current_input = ord(current_input[0])
            array_tape[current_cell] = int(current_input)
        elif code_list[command] == "[":
            if array_tape[current_cell] == 0:
                loop = 1
                while loop > 0:
                    command += 1
                    current_command = code_list[command]
                    if current_command == '[':
                        loop += 1
                    elif current_command == ']':
                        loop -= 1
        elif code_list[command] == "]":
            loop = 1
            while loop > 0:
                command -= 1
                current_command = code_list[command]
                if current_command == '[':
                    loop -= 1
                elif current_command == ']':
                    loop += 1
                elif (current_command == '+' and code_list[command - 1] == '[') or (current_command == '-' and code_list[command - 1] == '['):
                    array_tape[current_cell] = 0
            command -= 1
        command += 1    
            
    secondary_script = script_input()
    command_script(secondary_script)
    

    
