'''File Operions - Actions that can perform on files
      Read - For reading the data inside the file
      write - For overwriting the previous content
      append - For adding into the previous content

opening the fiile..
    Syntax - open(pathoffile,mode)'''

   # 1. First Method -- This method is used to open but it won't close the file after use. File must close after the code exucution
# file = (open("/Users/prasanthinavolu/Desktop/Python/Sample",'r'))
# print(file)
# file.close()
# print(file.closed())

'''Or
Syntx - with open(pathoffile,mode) as file:
But in second method using with it automatically closes the file
'''

# with open("/Users/prasanthinavolu/Desktop/Python/Sample",'r') as name_of_file:
#  print(name_of_file)
# print(name_of_file.closed) #This is used to check weather the file is closed or not

''' Reading:
        1.read - Will read the complete content in the file at a time.
        2.readline - It will read the content 1 line at a time
        3.readlines - It will read all the content in the file but line by line and output will be return as list'''

# with open("/Users/prasanthinavolu/Desktop/Python/Sample",'r') as name_of_file:
 # print(name_of_file.read())
 # print(name_of_file.readline())
 # print(name_of_file.readlines())
 # file = name_of_file.read()
 # for i in file:
 #   if 'python' in i:
 #    print(file)


''' Writing - it is overwrite the date with new content :
    1.Write - it is used to write the line in given file, if file not presents it is going to create the file and write the line
    2.Writelines'''
# with open("/Users/prasanthinavolu/Desktop/Python/Sample",'w') as name_of_file:
#  name_of_file.write("We are using write here \n")
#  name_of_file.writelines(["We are here to enjoy ur fcking lifes \n","In life everything want to be limited \n"])
#
#
# '''append - New Data is going to add to the previous data it is not going to overwrite the data
#            1.Write()
#            2.Writelines()'''
# with open("/Users/prasanthinavolu/Desktop/Python/Sample", 'a') as name_of_file:
#  name_of_file.write("append is going to add the data \n")
#  name_of_file.writelines(["We are here to enjoy ur fcking lifes \n", "In life everything want to be limited \n"])


''' How to perform CSV files
               csv - Command seperated value
                      reader
                      writer
                      appending
                      
 reader:'''
import csv
with open("/Users/prasanthinavolu/Desktop/Python/asdf.csv","r") as file:
 reader = csv.reader(file) # reader is an iterable
 print(reader)
 for i in reader:
  print(i[0]) #it goes with index of list
  print(i[1])
  print(i[3])
  if "Guru" in i:
   print(i[2])
  if i[3].startswith('9'):
   print(i)

'''writer:'''
with open("/Users/prasanthinavolu/Desktop/Python/asdf.csv","w") as file:
 writer = csv.writer(file)
 writer.writerow(['emp_Id', 'emp_name', 'emp_age', 'emp_mobile'])
 writer.writerow(['1','Guru', '22', '9941828081']) #For single use writerow is used
 writer.writerows([['2','Sai','23','9966048998'],['3','Prasanth','24','2177909726']])

'''append:'''
with open("/Users/prasanthinavolu/Desktop/Python/asdf.csv","a") as file:
 writer = csv.writer(file)
 writer.writerow(['4','Raghu', '25', '9550208020']) #For single use writerow is used
 writer.writerows([['5','Ma','25','2172181024'],['6','Bujjji','24','2177909726']])


