# pickling  
        #  we can convert python object to byte Stream
        # dump() and dumps()

# unpickling 
        # we can convert byte stream to python object 
        # load() and loads()

import pickle ,os 

l1 = [10,20,30]

pd = pickle.dumps(l1)

# print(pd)

upd = pickle.loads(pd)

# print(upd)

filename = input("Enter file name : ")

if os.path.exists(filename):
    print("File exists")
else :
    open(filename, "x")

l1 = [10,20,30]
f1 = open(filename, "wb")
pickle.dump(l1, f1 )

f1.close()

print("operation complted")