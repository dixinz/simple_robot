# Author: Dixin Zhang
# Student ID: 804604
# Date created: 08/10/2016
# Date modified: 20/10/2016


def repeat_interpreter(code):
    '''
    repeat_interpreter(code) that takes a list code containing a program that
    comprises 'move', 'turn' and 'repeat' statements, and returns a tuple
    corresponding to the new state of the robot after executing the program.
    '''

    # initialise position and direction
    pstn = [0, 0]
    dirc = 0

    # reference table for direction and action on corresponding axis
    dir_lst = ['N', 'E', 'S', 'W']
    action = ((1, 1), (0, 1), (1, -1), (0, -1))

    def move(code, pstn, dirc):
        '''
        move takes a list of commands, a position number, a direction number
        and a dictionary of macro command references, it returns the final
        state of a robot after executing these commands.
        '''

        # tempcode to record the code of each repeat
        tempcode = []

        # number of repeat required
        repeat_no = 0

        # flag to indicate if repeat is activated
        repeat = False
        # execute the code one by one
        for i in range(len(code)):

            # no repeat required, make changes to position and direction
            if not repeat:
                if code[i] == 'move':
                    pstn[action[dirc][0]] += action[dirc][1]
                elif code[i] == 'turn':
                    dirc += 1
                    dirc %= 4

                # encountered 'repeat'! turn on the flag and start record the
                # command that requires repeating
                elif code[i] == 'repeat':
                    repeat = True

            # now record the commands which need repeating
            else:

                # get the numeber of times of repeat
                if type(code[i]) == int:
                    repeat_no = code[i]
                
                # encounter the first 'end', call move again the get the
                # state after repeat
                elif code[i] == 'end':
                    for i in range(repeat_no):
                        (pstn, dirc) = move(tempcode, pstn, dirc)
                else:
                    tempcode.append(code[i])
        return (pstn, dirc)

    # translates direction number to letter and form the final tuple
    (pstn, dirc) = move(code, pstn, dirc)
    pstn.append(dir_lst[dirc])
    return tuple(pstn)
