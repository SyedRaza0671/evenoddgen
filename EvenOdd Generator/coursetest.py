odd_number_count = 0
even_number_count = 0

user_input_initial = int(input("Enter the initial value : "))
user_input_final = int(input("Enter the max value : "))

for i in range(user_input_initial,user_input_final+1) :
    
    if i%2==0 :
        print(i, "is an even number")
        even_number_count+=1
    else :
        print(i, "is an odd number")
        odd_number_count+=1
    i = i+1

print("Even numbers passed :",even_number_count)
print("Odd numbers count : ",odd_number_count)
user_input = "null"
while user_input != "exit" :
    user_input = input("Wating for end command : ")
