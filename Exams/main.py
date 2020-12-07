import exams_script
import sys
import time

'''
THIS PROJECT IS TO FILL OUT EXAMS . (GOOGLE FORM )
~ WAITING FOR MICROSOFT TEAMS
IF YOU WANT TO FILL THE EXAMS.JSON DATABASE , YOU ARE WELCOME!😁
'''


def animations():
    animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]"
    ]

    notcomplete = True
    for i in range(10):
        print('\r', end="")
        print('\r', end="")
        print(animation[i % len(animation)], end='')
        print(f'{(i / 10) * 100}', end="")

        time.sleep(.1)
        exams_script.exams()


def bar():
    responses = 10

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * responses))
    sys.stdout.flush()
    sys.stdout.write("\b" * (responses + 1))  # return to start of line, after '['

    for i in range(1, responses + 1):
        exams_script.exams()
        # update the bar
        print(chr(27) + "[2J")
        sys.stdout.write("~")
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar


animations()
