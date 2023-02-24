# ==========================================================
# ENCAPSULATION
# ==========================================================

# Creates / Incorporates CLASSES that creates a "blueprint"
# Reusing components / functions



# ==========================================================
# INHERITANCE
# ==========================================================

# Creates a sub-class of a class
# EXAMPLE
class Coffee:
    def __init__(self, type):
        self.type = type

class Cappucino:
    def __init__(self, name):
        self.name = name

class Latte:
    def __init__(self, name):
        self.name = name

class Mocha:
    def __init__(self, name):
        self.name = name



# ==========================================================
# POLYMORPHISM
# ==========================================================

# Alters a method from a CLASS to suit what the CURRENT CLASS needs
# Overwrites existing information



# ==========================================================
# ABSTRACTION
# ==========================================================

# The "Rules" of how you want things to connect
# EXAMPLE
# Without a Barista coffee machines wouldn't function UNLESS operated on
class Barista:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.postion = data['postion']
