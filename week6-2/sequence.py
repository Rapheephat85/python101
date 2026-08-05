# colors = ["red ", "blue","green","yellow","purple"]
#                  #  len = colore [-2]
# second_to_last_color = colors [-2]    
# print(f"second to last color: {second_to_last_color}")



# shapes = ["circle", "square", "triangle","rectangle","hexagon"]
# shapes[1] = "ellipse"
# shapes[3] = "pentagon"
# print(f"modified shapes: {shapes}")




# fruits = ["apple", "banana", "cherry"]
# more_fruits = ["mango","pineapple"]
# for fruit in more_fruits:
#     fruits.append(fruit)
# print(f"fruits after append: {fruits}")





# berryies = ["raspberry","blackbarry"]
# berryies.insert(1,"strawbeey")
# berryies.insert(2,"bluebarry")
# print(f"barryies after insert: {berryies}")





# fruits_with_duplicates = ["apple", "banana", "apple", "charry","apple","kiwi"]
# while "apple" in fruits_with_duplicates:
#     fruits_with_duplicates.remove("apple")
# print(f"fruits after remove:{fruits_with_duplicates}")




animals = ["cat", "dog","rabbit", "hamter","dog","parrot"]
first_dog_index = animals.index("dog")
print(f"The first occurrence of 'dog' is at index:{first_dog_index}")


second_dog_index = animals.index("dog",first_dog_index +1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")











