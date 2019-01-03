def script_meep():
    code_list = []
    base_code = input("\n>>> ")
    code_list = base_code.split()
    return code_list

def meep_script(code_list):
    current_cell = 0
    array_tape = [0] * 30000
    command = 0
    while command < len(code_list):
    
        if code_list[command] == "meeP":
            current_cell += 1
        elif code_list[command] == "Meep":
            current_cell -= 1
        elif code_list[command] == "mEEp":
            array_tape[current_cell] += 1
        elif code_list[command] == "MeeP":
            array_tape[current_cell] -= 1
        elif code_list[command] == "MEEP":
            print(chr(array_tape[current_cell]),end = "")
        elif code_list[command] == "meep":
            current_input = input(" ")
            current_input = ord(current_input[0])
            array_tape[current_cell] = int(current_input)
        elif code_list[command] == "mEEP":
            if array_tape[current_cell] == 0:
                loop = 1
                while loop > 0:
                    command += 1
                    current_command = code_list[command]
                    if current_command == 'mEEP':
                        loop += 1
                    elif current_command == 'MEEp':
                        loop -= 1
        elif code_list[command] == "MEEp":
            loop = 1
            while loop > 0:
                command -= 1
                current_command = code_list[command]
                if current_command == 'mEEP':
                    loop -= 1
                elif current_command == 'MEEp':
                    loop += 1
            command -= 1
        command += 1    
            
    secondary_meep = script_meep()
    meep_script(secondary_meep)