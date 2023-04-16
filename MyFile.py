# for testing 
n = None
while n is None:
  try:
    n = int(input("Enter number: "))
  except:
    n = None
    print("ENter valid number")
  
print([i for i in range(n+1) if i % 2 == 0]) # even numebrs 
