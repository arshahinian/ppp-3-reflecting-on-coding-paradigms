#Utils
def int_or_default(number,default):
    if type(number) == int:
        return number
    return int_or_default(default,0)

def fancy_print_list(numList):
    if isinstance(numList,list) == False:
        print(0)
    if len(numList) == 0:
        print(0)    
    fancy_display = ""
    for num in numList:
        fancy_display = f"{fancy_display} {num}"
    print(fancy_display)

# Functional Programming
# Implement a function that will flatten and sort an array of integers in ascending order,
# and which adheres to a functional programming paradigm.

def flatten_and_sort(numList):
    if isinstance(numList,list) == False:
        return []
    if len(numList) == 0:
        return []
    myNumList = []
    for numListItem in numList:        
        if type(numListItem) == int:            
            myNumList.append(numListItem)
        elif isinstance(numListItem,list):
            myNumList.extend(flatten_and_sort(numListItem))
        else:
            myNumList.append(-1)
    myNumList.sort()
    return myNumList

print(flatten_and_sort([1,2,3]))
print(flatten_and_sort([1,[8,9,10],3]))
print(flatten_and_sort([1,[8,9,[0,34]],3]))

# How does this solution ensure data immutability?
# --> This solution makes sure the list being passed into the function
# --> is looped through, and its values are added to a newly created list, which is returned.
# --> Because of this the data returned is not changed or modified by the input data or any other outside variables or logic.
# Is this solution a pure function? Why or why not?
# --> This is a pure function because it has no side effects, due to the same reasons answered in the previous question.
# --> This is also a pure function because when you put in the same values over and over again you get the same results.
# Is this solution a higher order function? Why or why not?
# --> No, this function is NOT a higher order function, as it does not have a function as a passed in argument to it.
# Would it have been easier to solve this problem using a different programming style?
# --> No, I thought functional programming was a good style to use, because it is a specific utility that needs to be preformed
# --> and can be used across a wide array of applications.
# Why in particular is functional programming a helpful paradigm when solving this problem?
# --> Object Oriented programming would require the abstraction of empirical things or concepts in the world to be organized into classes.
# --> These classes would then be used to instantiate objects. This style of programming would make a list sorting function too complex.
# --> It would introduce unnecessary hiding of values, properties, and methods to do a strait forward coding behavior.
# --> Functional programming suits this problem better, as it will solve the functional problem in a clean and direct way.

# Object Oriented Prompt
# Watto needs a new system for organizing his inventory of podracers.
# Help him do this by implementing an Object Oriented solution according to the following criteria.
# First, he'll need a general Podracer class defined with max_speed
# , condition (perfect, trashed, repaired) and price attributes.
# Define a repair() method that will update the condition of the podracer to "repaired".
# Define a new class, AnakinsPod that inherits the Podracer class
# , but also contains a special method called boost that will multiply max_speed by 2.
# Define another class that inherits Podracer and call this one SebulbasPod.
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed = self.max_speed * 2

class SubulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self,other):
        other.condition = "trashed"

a = AnakinsPod(10,"perfect","5000")
print(a.max_speed)
print(a.price)
print(a.condition)

s = SubulbasPod(15,"perfect","5500")
print(s.max_speed)
print(s.price)
print(s.condition)

a.boost()
print(a.max_speed)

s.flame_jet(a)
print(a.condition)
a.repair()
print(a.condition)

# How does this solution demonstrate the four pillars of OOP?
# (It may not demonstrate all of them, describe only those that apply)
# * Encapsulation
# --> The solutions values are represented as properties that are hidden inside their associated objects.
# --> The act of hiding values, is what encapsulation is; making sure that the values are protected within a Class / Type Def.
# --> These Classes need to be instantiated to gain access to the actions of setting and getting the associated hidden variables.
# * Abstraction
# --> The repair method is a good example of abstraction, as it is a method that would be used by Classes that are children of the Podracer Class.
# --> AnakinsPod and SubulbasPod both can be repaired so this method was abstracted out into a super class (or super type).
# * Inheritance
# --> The base or super Class Podracer is the parent Class to the AnakinsPod and SubulbasPod child Class.
# --> This was done by passing Podracer into the two child Classes as an argument.
# --> The python specific method "super", was used to reference the parent class in both AnakinsPod's and SubulbasPod's constructor.
# --> This was done to pass the constructor arguments to the parent object, during instantiation of the child objects.
# * Polymorphism
# --> This could have been done, by creating a reference to the Podracer type
# --> , assigning that reference a child type (AnakinsPod or SublbasPod)
# --> , then referenced the parent type's method by executing an overwritten method existing in both extended (child) classes.
# --> But, we did not do that here and polymorphism was not done in this example.
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# --> No, I do not believe it would have been easier to use a different style of coding for this solution.
# --> This is because the values and actions that need to be executed lend themselves to tangible "things" and "behaviors"
# --> that happen in real life. [Or at least in the movies :)]
# How in particular did Object Oriented Programming assist in the solving of this problem?
# --> As mentioned above, the fact that Pod Racers are a thing that can be described with attributes and actions make OOP work here.
# --> Other styles of coding would not neatly pack the actions and values together into a container that can be used as a type or mold.

# Reflection
# Is one of these coding paradigms "better" than the other? Why or why not?
# --> No, it matters what you are trying to accomplish.
# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
# --> I find OOP more appealing as it mirrors the real world conceptually.
# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using:
# * Functional Programming?
# * --> Functional Programming would be good for Utilities and Service Oriented Solutions for simple data manipulation.
# * Object Oriented Programming?
# * --> OOP is good for almost all coding solutions, there was one time I used it for a File Importer and even though it worked
# * --> , I feel Functional Programming may have worked better.
# Personally, which of these styles takes more work to understand?
# * --> For me Functional Programming but that is because I am used to OOP
# What should be done in order to deepen understanding related to this paradigm?
# * --> I need to study Functional Programming more as I think it would be useful for File and Data Utilities.







        
    
        
    

    
