rrno = input("Enter RR number: ")
name = input("Enter customer name: ")
prevread = int(input("Enter the previous reading: "))
curred = int(input("Enter the current readings: "))

# print("These are the units according to that price is there")
# print(" 000 - 100 -------- 5 Rs.")
# print(" 101 - 200 -------- 10 Rs.")
# print(" 201 - 300 -------- 15 Rs.")
# print(" 301 - 400 -------- 20 Rs.")
# print(" 400 >     -------- 25 Rs.")

if curred>prevread:
    unit= curred - prevread
    # print(unit)

slb1 = int(input("Enter rate of slab1: "))
slb2 = .5* slb1 + 10
slb3 = .6* slb2 + 15
slb4 =.7* slb3 + 20
slb5 =.8* slb4 + 25


if unit >= 0 and unit <= 100:
    total = unit*slb1
    # print("Total unit: ", unit, "units","& Total bill: ", total, "Rs.")

elif unit >= 100 and unit <=200:
    total = unit*slb1+(unit-100)*10
    # print("Total unit: ", unit, "units","& Total bill: ", total, "Rs.")

elif unit >= 200 and unit <=300:
    total = unit*slb1+(unit-100)*slb2+(unit-200)*slb3
    # print("Total unit: ", unit, "units","& Total bill: ", total, "Rs.")


elif unit >= 300 and unit <=400:
    total = unit*slb1+(unit-100)*slb2+(unit-200)*slb3+(unit-300)*slb4
    # print("Total unit: ", unit, "units","& Total bill: ", total, "Rs.")

else:
    total = unit*5+(unit-100)*slb2+(unit-200)*slb3+(unit-300)*slb4+ (unit-400)*slb5   
    # print("Total unit: ", unit, "units","& Total bill: ", total, "Rs.")
print("==============CSPTCL BILL==================")
print("RR no : ", rrno)
print("Customer name: ", name)
print("Rate of slab: ", slb1)
print("Unit used: ", unit, "units")
print("Total bill: ", total, "Rs.")