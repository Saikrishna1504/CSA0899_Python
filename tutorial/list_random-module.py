# Lists
n = [1,2,3,4,5] // int data type
names = ["sai","krishna","ram"] // string
mixed_list = [1,"sai",True,1010,"krish"] // different types of data also possible in lists

// Index always starts from 0.(count starts from 0 in programming)
print (n) ---> [1,2,3,4,5]
print(n[3]) ---> 4
print(n[9]) ---> End up with index error
print(len(n)) ---> 5 
print(n[-1]) ---> 5

# List slicing
n = [10,0,-1,7]
print(n[0:4]) // print(n[:]) // print(n[0:]) ---> [10,0,-1,7]
print(n[1:3]) ---> [0,-1] // here 1 is index and 3 is len(asscending order)
print(n[:3]) ---> [1,2,3] // it print upto len
print(n[0:4:2]) ---> [10,3,5]  // third element refers to skipping of numbers

# pre-defined functions
n = [1,5,3,6,-2,3]
n.sort()  // accending order and we can't include sort in print statemnt.mix_list can't be used with sort
n.reverse() // reverse of a list
print(n) 
print(min(n)) // minimum number will be printed
print(max(n)) // max number will be printed
n.append(89) ---> [1,5,3,6,-2,3,89] //  will be added into last element of list
n.insert(3,69) ---> [1,5,3,69,-2,3,89] // here 2 is index where we want to insert 
n.extend([4,6,98,75]) ---> [1,5,3,6,-2,3,4,6,98,75] // can extend the list ,more than one element
n[2] = 53 ---> [1,5,53,6,-2,3] // replace element at particular index
n[1:3] = [23,65] ---> [1,23,65,6,-2,3] // multiple elemenets at once amd here 3 is len asuaul
n.remove(5) ---> [1,3,6,-2,3] // nukes the value from it
n.remove(3) ---> [1,5,6,-2,3] // we have two 3's .so, it nuked first occurance
n.pop() ---> [1,5,3,6,-2] // nukes last element
n.pop(2) ---> [1,5,6,-2,3] // nuke by using index with pop commands








