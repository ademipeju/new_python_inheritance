#create a Class named Parent and create two other 
# classes children and grandchildren. The children must inherit from their parent, and the grandchildren
#  must inherit from both parent and children.

class Parent:
    def __init__(self, family_name, state):
        self.family_name= family_name
        self.state= state
    def describe(self):
        return f"my father's name is {self.family_name}, and I am from {self.state}"

class Children(Parent):
    def __init__(self, fname, occupation, family_name, state):
        super().__init__(family_name, state)
        self.fname= fname
        self.occupation= occupation
    def describe(self):
        super().describe()
        return f"I am {self.fname}, {self.family_name} and I am a  large scale {self.occupation}, I am from {self.state}"
        
        

class GrandChildren(Children):
    def __init__(self, name, occupation, family_name, state, cartoon, fname, grade):
        super().__init__(fname, occupation, family_name, state)
        self.cartoon= cartoon
        self.name= name
        self.grade= grade
    def describe(self):
        super().describe()
        return f"my name is {self.name}, {self.family_name}, and my favourite animation is {self.cartoon}, my father's occupation is a {self.occupation}, I am also from {self.state}"
         
       
        
parent= Parent(family_name="OGUNSOLA", state="ekiti")

children= Children(fname= "Oladipo", occupation= "farmer", family_name="OGUNSOLA", state="ekiti")
print(children.describe())

grandchildren= GrandChildren(name= "Enoch", cartoon= "PJ Mask", occupation= "farmer", family_name= "OGUNSOLA", state="ekiti", fname= "Oladipo", grade= "Basic1")
print(grandchildren.describe())




    