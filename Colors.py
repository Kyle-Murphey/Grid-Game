class Colors:

    def output(number):
        WHITE = '\033[0m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        BLUE = '\033[34m'
        YELLOW = '\033[33m'

        if (number == 0):
            return "{}{}{}".format(WHITE, number, WHITE)
        elif (number == 1):
            return "{}{}{}".format(RED, number, WHITE)
        elif (number == 2):
            return "{}{}{}".format(GREEN, number, WHITE)
        elif (number == 3):
            return "{}{}{}".format(BLUE, number, WHITE)
        elif (number == 4):
            return "{}{}{}".format(YELLOW, number, WHITE)