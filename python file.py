

difficulty = int(input('how difficult is this task on a scale of 1-5?:'))
if difficulty >5:
    print('difficulty must be on a scale of 1-5!')
elif difficulty <1:
    print('difficulty must be on a scale of 1-5!')    
elif difficulty >=3:
    print('uhm good luck')
elif difficulty <=2:
    print('ur good man dw')

urgency = int(input('how urgent is this task? on a scale of 1-3:'))
if urgency == 3:
    print('URGENT GO DO YOUR WORK RUN')
elif urgency == 2:
    print('okay dont procrastinate on it too much')
elif urgency == 1:
    print('do your important tasks first, but dont forget about this one')
else: 
    print('urgency must be on a scale of 1-3! try again')


difficulty = int(input('how difficult is this task on a scale of 1-5?:'))
if difficulty >5:
    print('secret third option!')
    shop = int(input('do you want to go to the shop? 1=yes, 2=no'))
    if shop == 1:
        print('1. you have chosen to go to the shop')
    elif shop == 2:
        print('2. no shop')
    else:
        print('input not valid why does it say this')
elif difficulty <1:
    print('difficulty must be on a scale of 1-5!')    
elif difficulty >=3:
    print('uhm good luck')
elif difficulty <=2:
    print('ur good man dw')   