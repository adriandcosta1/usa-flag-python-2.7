import sys

first_time = True
second_time = False
first_stars = 6
second_stars = 5
total_lines = 11
stars1_col = 6
stars2_col = 5
total_tokens_per_line = 37
first_total_lines = 24

i = 0
for i in range(total_lines):
    if(first_time or second_time):
        # if second_time is true print space at the beginning of every
        # second line else just empty space
        if(second_time):
            sys.stdout.write(" ")
        # else no space
        else:
            sys.stdout.write("")
        
        # if first_time is true print a star and a space
        if(first_time):
            j = 0
            for j in range(stars1_col):
                sys.stdout.write("* ")
             
            # first line is done reverse these two variables   
            second_time = True
            first_time = False
        # if not first_time print "* " and at the end of stars
        # write space
        else:
            m = 0
            for m in range(stars2_col):
                sys.stdout.write("* ")
                
            # write an extra space after every second line of stars
            sys.stdout.write(" ")
            
            # reverse these two variables again
            first_time = True
            second_time = False
        
        # write an extra space after every second line of stars
        sys.stdout.write(" ")
        
        # draw the underscore lines (the stripes besides stars)
        l = 0
        for l in range(first_total_lines):
            sys.stdout.write("_")
        
        # now flush out or write stripes and stars besides stripes
        sys.stdout.flush()
        
        # if there are 8 lines printed print a newline
        print("")
        
        # if stars and stripes lines are total of 8 make these variables
        # false
        if (i == 8):
            first_time = False
            second_time = False
    
    # then draw the last lines, flush it and print new line    
    if ((not first_time) and (not second_time)):
        k = 0
        for k in range(total_tokens_per_line):
            sys.stdout.write("_")
            
        sys.stdout.flush()  
        print("")