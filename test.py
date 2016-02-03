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














