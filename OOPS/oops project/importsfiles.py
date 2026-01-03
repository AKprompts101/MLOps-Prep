from project import chatbook

# user1 =chatbook()
# ==============================================================================
# encapsulation
# ==============================================================================
# print(user1.__name) # encapsulation protection
# print(user1._chatbook__name)   #this is how we se hide data (encapulated data)


# ==============================================================================
# Getter and Setter
# ==============================================================================
# print(user1.get_name())     #Getter and Setter
# user1.set_name("AK")
# print(user1.get_name())


# ==============================================================================
# Static Method
# ==============================================================================
user1 =chatbook()
# print(user1.id)

# user2 =chatbook()
# print(user2.id)

# user3 =chatbook()
# print(user3.id)

#getter and setter Static method

print(user1.id)
chatbook.set_id(101) # set user id as 101

user2=chatbook()
print(user2.id)

user3=chatbook()
print(user3.id)


