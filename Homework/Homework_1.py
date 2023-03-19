#declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list, type(my_list))
#afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
my_ascendent_list = sorted(my_list)
print(my_list)
print(my_ascendent_list)
#afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
my_list_reversed = list(reversed(my_ascendent_list))
print(my_list)
print(my_list_reversed)
#afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
my_sliced_list = my_list_reversed[::2]
print(my_list)
print(my_sliced_list)
#afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
my_second_sliced_list = my_list_reversed[1::2]
print(my_second_sliced_list)
#afișează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
print(my_second_sliced_list[0:4:3])








