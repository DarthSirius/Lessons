#python_string = 'Hello! My name is Python. I will help you to analyze some data'
#n = python_string.count('')
#print(n**3)

def distance_between_dots(x1,y1,x2,y2):
    try:
        coord = [x1,y1,x2,y2]
        for i in coord:
            if type(i) != int and type(i) != float:
                raise ValueError
    except ValueError:
        print("Arguments are not numbers!")
        return
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    return dist

print(distance_between_dots(5,2,8,3))
print(distance_between_dots('a',2,8,3))