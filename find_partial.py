#https://www.hackerrank.com/challenges/ctci-contacts/problem

class Contacts(object):
    def __init__(self):
        self.names = {}
    #add name
    def add_name(self, name):
        hashed_name = [name[:i+1] for i, char in enumerate(name)]
        for partial_name in hashed_name:
            self.names[partial_name] = self.names.get(partial_name, 0) + 1 
    #find partial
    def find_partial(self, partial):
        return self.names.get(partial, 0)


n = int(input().strip())
contact_list = Contacts()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        contact_list.add_name(contact)
    if op == "find":
        print(contact_list.find_partial(contact))
