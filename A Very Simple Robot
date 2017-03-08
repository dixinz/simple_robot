# Author: Dixin Zhang
# Student ID: 804604
# Date created: 08/10/2016
# Date modified: 20/10/2016


def simple_interpreter(code):
    """
    the function returns the new state of the robot after executing the program
    """

    code = iter(code)

    # record position and direction

    position = [0, 0]
    direction = 0

    # reference for position and changes of position

    dir_lst = ['N', 'E', 'S', 'W']
    action = ((1, 1), (0, 1), (1, -1), (0, -1))

    def move(code, position, direction):
        '''
        move takes a list of two ints, an int and a number which represents
        the commands, position of the robots and direction of a robot
        respectively. It returns the final position and direction of a robot
        '''

        # change the position and direction by reading the command one by one

        while True:
            try:

                # change the position of the corresponding axis and values

                if next(code) == 'move':
                    position[action[direction][0]] += \
                        action[direction][1]
                else:

                    # change the direction and normalise it

                    direction += 1
                    direction %= 4
            except StopIteration:

                # stop after reading the last command

                break

        # dereference position to letter and return the correct output

        position.append(dir_lst[direction])
        return tuple(position)

    return move(code, position, direction)
