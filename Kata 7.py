from time import sleep

user_input = ''
planetas = []

while user_input.lower() != 'done':
    
    if user_input:
        planetas.append(user_input)
    user_input = input("Enter a new planet, or done when done: ") 

#print(planetas)


for i in planetas:
    print(i)


"""countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1) #espera 1 segundo

print("Blast off!!")"""