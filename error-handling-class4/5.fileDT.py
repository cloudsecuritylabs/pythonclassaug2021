import datetime

myfile = open("myfile_class.txt","r+")

print(myfile.name)
print(myfile.mode)

myfile.write("Hello 2 \r\n")
myfile.write("\n")
myfile.close()

myfile.write("\n")

#
# myfile = open("myfile_class.txt","r")
# print(myfile.read())
# myfile.close()
#
# # yourfile = open("yourfile.txt", "w")
# # for i in range(5):
# #     yourfile.write(str(i)) # test
# # yourfile.close()
#
#
# date = datetime.datetime.now()
# print("\n",date.time())