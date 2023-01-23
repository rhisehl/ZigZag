import time, sys
indent = 0 #how many spaces to indent
indentIncreasing = True #whether indenting is increasing or not

try:
    while True: #main program loop
        print (' ' * indent, end='')
        print('********')
        time.sleep(.1) #pause for 1/10 second
        
        if indentIncreasing:
            #increase number of spaces:
            indent = indent + 1
            if indent == 20:
                # change direction"
                indentIncreasing = False
        else:
            #decrease number of spaces:
            indent = indent - 1
            if indent == 0:
                #change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()