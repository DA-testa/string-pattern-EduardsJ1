# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    inp=input().lower()
    if inp=='f':
        with open('tests/06') as f:
            pattern=f.readline().rstrip()
            text=f.readline().rstrip()
    else:
        pattern=input().rstrip()
        text=input().rstrip()
    #print(pattern)
    #print(text)

    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p=len(pattern)
    t=len(text)
    d=256
    q=100000000
    ph=0
    th=0
    result=[]
    h=1
    for i in range(p-1):
        h=(h*d)%q
    for i in range(p):
        ph=(d*ph+ord(pattern[i]))%q
        th=(d*th+ord(text[i]))%q
    #print(th)
    #print(ph)

    for i in range(t-p+1):
     if ph==th:
        if pattern==text[i:i+p]:
           result.append(i)
     if i<t-p:
        th=(d*(th-ord(text[i])*h)+ord(text[i+p]))%q
    
    
   

    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

