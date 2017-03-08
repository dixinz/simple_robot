# Author: Dixin Zhang
# Student ID: 804604
# Date created: 08/10/2016
# Date modified: 20/10/2016


def macro_interpreter(code, macros):
    '''
    that takes a list code containing the operators 'move' or 'turn' or any
    macros defined in the dictionary macros, and returns a tuple corresponding
    to the new state of the robot after executing the program.
    '''

    # initialise position and direction
    pstn = [0, 0]
    dirc = 0

    # references for direction and action made to position of different
    # direction
    dir_lst = ['N', 'E', 'S', 'W']
    action = ((1, 1), (0, 1), (1, -1), (0, -1))

    def move(code, pstn, dirc, macros):
        '''
        move takes a list of commands, a position number, a direction number
        and a dictionary of macro command references, it returns the final
        state of a robot after executing these commands.
        '''
        # execute all commands one by one
        for i in range(len(code)):

            # change the corresponding axis and values of position if 'move'
            if code[i] == 'move':
                pstn[action[dirc][0]] += action[dirc][1]

            # change the direction and normalise it
            elif code[i] == 'turn':
                dirc += 1
                dirc %= 4

            # if the command is a macro, translate it to simple commands
            else:
                tempcode = macros.get(code[i])

                # call move again to get the state after executing the macro
                (pstn, dirc) = move(tempcode, pstn, dirc, macros)
        return (pstn, dirc)

    # inital call to update the postion and direction
    (pstn, dirc) = move(code, pstn, dirc, macros)

    # translates direction number to letter and form the final tuple
    pstn.append(dir_lst[dirc])
    return tuple(pstn)
