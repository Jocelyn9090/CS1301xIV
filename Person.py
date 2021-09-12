#Classes can also have references to other instances of
#themselves. Consider this Person class, for example, 
#that allows for an instance of a father and mother
#to be given in the constructor.
#
#Create 3 instances of this class. The first should have 
#the name "Mr. Burdell" with an age of 53. The second
#instance should have a name of "Mrs. Burdell" with an age
#of 53 as well. Finally, make an instance with the name of
#"George P. Burdell" with an age of 25. This final instance
#should also have the father attribute set to the instance 
#of Mr. Burdell, and the mother attribute set to the 
#instance of Mrs. Burdell. Finally, store the instance of 
#George P. Burdell in a variable called george_p. (It does
#not matter what variable names you use for Mr. and Mrs.
#Burdell.)

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

#Write your code here!

burdell = Person("Mr. Burdell", 53)
mrsburdell = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, burdell, mrsburdell)



#The code below will let you test your code. It isn't used
#for grading, so feel free to modify it. As written, it
#should print George P. Burdell, Mrs. Burdell, and Mr.
#Burdell each on a separate line.
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)


#OR


#There are two slightly different ways we could approach this.
#First, the more obvious way is to create all three instances
#first, then link them up. So, first we create each instance:

george_p = Person("George P. Burdell", 25)
the_mother = Person("Mrs. Burdell", 53)
the_father = Person("Mr. Burdell", 53)

#Then, we declare that george_p's mother and father are
#the_mother and the_father:

george_p.mother = the_mother
george_p.father = the_father


#OR 2

#Instead of creating all three instances first, we could instead
#create mother and father solely as the attributes of george_p.
#To do this, we'd first create george_p:

george_p = Person("George P. Burdell", 25)

#And then we'd use the same constructors to create the mother and
#the father, but instead of assigning them to an intermediate
#variable, we would assign them directly to george_p's attributes:

george_p.mother = Person("Mrs. Burdell", 53)
george_p.father = Person("Mr. Burdell", 53)


#OR 3

#We can even accomplish this all in one line by using the
#keyword parameters to the Person constructor:

george_p = Person("George P. Burdell", 25, mother = Person("Mrs. Burdell", 53), father = Person("Mr. Burdell", 53))

#We can use the keyword parameters to pass mother and father
#directly into the constructor, or we can even set those
#keywords equal to those new instances directly!
