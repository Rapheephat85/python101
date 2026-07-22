# print('Nuber\tSquare')
# print('-----------------')
# for number in range(1,13) :
#     Square =number**2
#     print(number, '\t', Square)
    
print('kph\tmph')
print('-----------------')
for kph in range(60, 131, 10) :
    mph = kph * 0.6214
    print(kph, '\t', mph)
    
print('mph\tkph')
print('-----------------')
for mph in range(60, 131, 10) :
    kph = mph / 0.6214
    print(mph, '\t', kph)
    