global f
f = 0

#this t_movie function is used to select movie name 
def t_movie():
    global f
    f = f+1
    print("Which movie do you want to watch?")
    print("1. The Batman")
    print("2. No Country for Old Men")
    print("3. Obsession")
    print("4. Back")
    movie = int(input("Choose your Movie: "))
    if movie == 4:
      # in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater 
      center()
      theater()
      return 0
    
    if f == 1:
      theater()
# this theater function used to select screen 
def theater():
    print("Which screen do you want to watch movie : ")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    a = int(input("Choose your Screen: "))
    ticket = int(input("Number of ticketS you want : "))
    timing(a)
    # this timing function used to select timing for movie 
def timing(a):
    time1 = {
        "1": "10:00-1:00",
        "2": "1:10-4:10",
        "3": "4:20-7:20",
        "4": "7:30-10:30"
    }
    time2 = {
        "1": "10:15-1:15",
        "2": "1:25-4:25",
        "3": "4:35-7:35",
        "4": "7:45-10:45"
    }
    time3 = {
        "1": "10:30-1:30",
        "2": "1:40-4:40",
        "3": "4:50-7:50",
        "4": "8:00-10:45"
    }
    if a == 1:
        print("Choose your time:")
        print(time1)
        t = input("Select your time:")
        x = time1[t]
        print("Successful!!! Enjoy movie at "+x)
    elif a == 2:
        print("Choose your time:")
        print(time2)
        t = input("Select your time:")
        x = time2[t]
        print("Successful!!! Enjoy movie at "+x)
    elif a == 3:
        print("Choose your time:")
        print(time3)
        t = input("Select your time:")
        x = time3[t]
        print("Successful!!! Enjoy movie at "+x)
    return 0

def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Not Available!!")

def center():
    print("Which theater do you wish to see the movie? ")
    print("1. INOX")
    print("2. IMAX")
    print("3. PJP Cinepolis")
    print("4. Back")
    a = int(input("Choose your option: "))
    movie(a)
    return 0

# this function is used to select city 
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1. Ranchi")
    print("2. Jamshedpur")
    print("3. Delhi")
    place = int(input("choose your option: "))
    if place == 1:
      center()
    elif place == 2:
      center()
    elif place == 3:
      center()
    else:
      print("wrong choice")


city() # it calls the function city





