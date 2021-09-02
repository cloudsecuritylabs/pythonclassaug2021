'''
Test various modes
r --> Opens a file for reading only.
rb -->Opens a file for reading only in binary format.
r+ -->Opens a file for reading and writing.
rb+ -->Opens a file for reading and writing in binary format.

w -->Opens a file for writing only.
wb -->Opens a file for writing only in binary format.
w+ -->Opens a file for reading and writing.
wb+ -->Opens a file for reading and writing in binary format.

a -->Opens a file for appending.
ab -->Opens a file for appending in binary format.
a+ -->Opens a file for writing only.
ab+ -->Opens a file for writing only in binary format.
'''
file = open("doesnotexit4.txt", "w+") # read and write
file.write("not again")
file.seek(0)
print(file.read())
file.close()


