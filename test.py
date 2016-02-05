b=0
while b<10:
    b+=1
    if b!=10:
        print(b,end=",")
    else:
        print(b)


theList=["Yo","My","Name","is","Kanishk","Motherfucker"]
print(theList)
theList.insert(0,"Hey")
print(theList)

for i in range(-10,10+2,2):
    print(i)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
#Damn dude you can have an else statement associated with a loop. That is crazy dude. Freaking crazy. But it does not happen when
# there is a break. They don't freaking mention these advanced concepts anywhere else except the tutorial dude. Awesome man awesome.
def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

a=[100,2000,20000]
#Nice now this map stuff makes sense dude. I am so glad I am doing this python tutorial dude. Stuff makes much more sense now.
#the map object is an iterable so you need to list it. Nice I got this shit dude. Python is the second language I am learning after java
# in so much freaking detail. It seems really useful so far. I am a bloody learning machine.
# try new things and keep learning motherfucker. I know you will win dude.
list(map(fib,a))

def giveSame(a):
    return(a)
alpha = [1,2,3,4]

print(alpha is giveSame(alpha))

fib(1000)
#Wow you can rename functions that is so crazy dude. I don't know if I will be able to remember this stuff dude. I guess I will have to write
# a lot of code and read a lot of code in python to truly get used to all of this dude. Crazy dude. That is so crazy.
f=fib
f(100)
#Wow dude. Learning this stuff is so much easier because I know java. I know a lot of stuff I should and do expect. Some things are new and interesting indeed
#Ok I need to ask questions and become more active in dance class with the women dude.

#Wow so many keywords to remember dude.

print(1 in [1,2,3])

# This is intesting everything is rememebered by reference cool dude. So the yobaby things is remembered nice. and it shows up when i print yobaby.
# cool dude.
# Python is indeed a complex and rich language dude. I did not know this. Good to learn this stuff. I hope I become better and better at this dude.

yobaby=[]
def f(a, L=yobaby):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(yobaby.append(4))
print(f(5))

#Difference between positional and keyword arguments. Nice man I get it. I get it. Its amazing awesome man
#cool thing is did you know you can also use a hash map to pass on values. isn't that amazing dude. Cool man cool.
# A lot of technicalities to this python language dude. Cool man cool. Learning a lot of stuff. Need to get better and better dude.
# Need to slowly start using python for more and more things because of its usefulness. Its extremely useful dude. I needed a structured
#tutorial though. Its interesting how I mix up structured and unstructured data dude. cool man.
def yoMan(man1="the man",man2="superman"):
    print(man1+man2)
    return man1+man2
yoMan("cool","dude")
yoMan(man2="the dude",man1="cool")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

#Wow this is really advanced you don't even need to format everything as a hashmap it automatically creates a hashmap from the keywords and their
#arguments this is super interesting dude. Python is really freaking advanced in that sense dude. I don't know if I will be able to remember all this stuff
#I should practice more using this code to complete tasks. See how it goes dude. I want to use all these shortcuts. And I think I can. Cool man
# this is really cool. This should solve and simplify a lot of problems I had with Java anyway. I know I regularly used to pass lists and stuff
# in java. That might not be such a big deal in python. Lets see if I use all these advanced concepts or not. Good to know all these butterknife
#languaged dude. Cool man.
# the *args thing is really useful. Even the **hashmap is really useful. I think I am going to use this shit when I write my code. cool man.
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# this is so much easier because I know java
#Wow you can have nested functions and you can return functions. That is crazy dude. Absolutely crazy. Now I understand the reason you could
#rename functions all this makes much more sense now. Awesome
def makeAFunction(name):
    def namifier(age):
        print("Hi my name is "+name+" and I am "+age)
    return namifier

func=makeAFunction("Kanishk")
#Wow it worked crazy dude. Freaking amazing dude. I make a completely new function using this technique.
#This is crazy dude. Yes you can have embedded functions in python. This is crazy dude. Amazing. This is such an incredibly flexible and powerful
#language. You can do so much with so few keywords dude. Break the rules and see what happens dude. Break the freaking rules make the eye contact
#Crazy dude. Interesting I must try this.
func("26")

lst=[1,2,3,4,5,6]
#So a new object is created when you do this. Interesting. I did not know that.
print(lst is lst.copy())
#Cool man Start using python more and more. And you will become really freaking good at this shit dude.
#Comeon you can do this Kanishk. Work harder. Make this thing work. Make this thing work.

print([x**2 for x in range(10)])
#This is one way to define anonymous fucntions.
# Dude this is too concise for me. I am not sure if I will be able to remember this shit.
# Let me try to think about this I will try to do this

# this is one way to do it that I find extremely comprehensible. Cool man, I like this shit nice.
def po(i):
    return i**2

print(list(map(po,range(i))))
#Work harder kanishk. Avoid distractions. Avoid more and more distractions. Cut down on certain things to buy more time.
#The sad fact is you can't do everything. So do a few things well. Yeah I agree with that philosophy. I'm going to follow it and do a few
# things really really well dude.

t=[1,2,3,4]
print(t)
#Wow tuple unpacking and packing is so cool dude. Lets see if this also works with lists
a,b,c,d=t
#Wow this does work with lists amazing dude. Cool man cool. So many cool and interesting features build into python man.
print(b)

dictionary={}
#Zip reversed. Blah blah blah so many thing. Its good to know these features but I doubt I am going to remember all of them.
# I should quickly read python programming guide and then just start coding. The important section is the packages
# I think I will hit this section next. Cool man

var="Hellow Hellow          ".strip().capitalize().split()
print(var)

class Dog:
    #This is like saying this is a public static method or variable. Its so precisely defined in Java but also accurately and powerfully
    #in python. You just have to remember how it was used. If you write self that is an instance method.
    tricks = []
    @classmethod #Wow I had no idea you could do this. The python documentation is slightly incomplete. It makes more sense to come to
    #Python with the Java knowledge in mind dude. Cool man cool. It is pretty much the same thing.
    def weirdMethod(cls):
        return cls

    def weirderMethdod(self):
        return self

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

#Very compact way of defining classes in python. Ok I like it dude. Cool. I think I need to experiment a little bit more to figure this stuff out
# I still don't know how to distinguish between class methods and instance methods for example.

#I want to be one of the people solving these problems dude. I am good at this. I am good at thinking and learning new things.
#Thinking and learning systematically, leveraging my brains associative thinking capabilities. So interesting dude. Amazing man.
#Very different perspective. Wow, I feel much better right now. Its crazy how I suddenly felt really sleepy. Like an insulin drop. Its crazy.


d=Dog
print(Dog is Dog.weirdMethod())

aa=Dog("yolo")

print(aa is aa.weirdMethod())

#bb=Dog()

#print(len(bb.name))


class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


#Nice this is really freaking useful dude. I can apply this to my own code. Nice dude. Nice. I did not realize I could do this
# this is super freaking awesome dude. Nice dude super nice dude. Awesomeness. Amazingness. I am going to DEFINITELY use this functionality
# also I think I will follow Arjun when it comes to coding style. I think he has it down right dude. He has it down. This is awesome.
#Cool this begins my python journey. Now I know. And will know as I keep on practicing and stuff dude. Nice man nice.
#Take what you can get dude. Take what you can get my man. Take what you can get.

#This is so cool dude. Nice.
#Python is a weird and interesting language. I am glad to have learned it dude. Nice nice nice man. Awesome freaking awesome man.
#Wow Sam stayed in his lab for 4 years thats pretty awesome man. Almost like being a PhD student man. Nice. I think I am better prepared for this stuff dude.

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



#these generator thingys also seems really cool. The question is though. Will I use all these features when I am writing code.
#Not completely sure am I. No I am not. But I can do a lot more if the degree i have with me dude.

# you have to be really carefull when using import in python because the way you import severely affects the namespace and you can hide or shadow current variables or functions with the same name dude
#its nice to see that python can do shell stuff. Awesome man super duper awesome man. I like this cool dude. cool. Lambe race ka ghoda. Ok dude. Lets do this shit. I guess I am dancing in a short while.
#Lets go at 8:30. Thats the best time to go dude. #Maybe 8:35 cool man cool
#interesting you can use data compression algorithms in python. Such an expansive and flexible language dude. Nice. No wonder so many people use python dude. Awesome.

#Wow, you can also time stuff dude. Nice awesome dude. I did not know you could do that stuff amazing man amazing awesomeness.
#what does assert in python mean anyway. I haven't really seen anyone use assert accept arjun. What the fuck is this assert thing. I can understand a lot of the code that arjun wrote though. Amazing dude awesomeness
#Well I don't have a live example like dynetica. But I think this is good enough dude.

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())   # automatically validate the embedded tests

#awesome man you can run tests directly from the docstrings. Wow, python indeed is a very versatile and expansive language. I love it awesome dude. I think its going to be my new workhorse
# as I cut my dependence from java. Java is a great language but python seems to have a LOT MORE packages which is freaking awesome dude. Super awesome.