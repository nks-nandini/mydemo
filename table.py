#n=int(input("enter number:"))
#i=1
# while(i<=10):
#   print(f"{n} x {i}={n*i}")
#   i+=1
nums=[1,4,9,16,25,36,49,81,100]
idex=0
while(idex<len(nums)):
  print(nums[idex])
  idex+=1

# heros=["spideman","ironman","thor"]
# count=0
# while(count<len(heros)):
#   print(heros[count])
#   count+=1

find=int(input("enter the num:"))
j=0
square=[1,4,9,16,25,36,49,64,81,100]
if find  in square:
    print("value found",find)
else:
    print("value not in the list")
j+=1

list=["nanidni",20,"solanki"]
print(len(list))
print(type("nandini"))
print(list.remove(20))
print(list)

set={1,2,3,4,5,6,1,2,3}
print(type(set))
print(set.add(12))
print(set)
set.remove(2)
print(set)

list2=["nanidni","didu","solanki"]
for i in range(len(list2)):
  print(list2[i])

ls = ["a", "b" , "c"]
ls2 = [1, 2, 3]

ls.append(ls2)

print(ls)
