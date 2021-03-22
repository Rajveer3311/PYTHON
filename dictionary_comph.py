#print count string char
string='rajveer'
count_char={char:string.count(char) for char in string}
print(count_char)

#square value find
square={num:num**2 for num in range(1,11)}
print(square)

#in format form 

square={f'square of {num} is':num**2 for num in range(1,11)}
for i,j in square.items():
    print(f'{i}:{j}')


#if else with comprehension

even_odd={num:('even'if num%2==0 else 'odd')for num in range(1,11)}
print(even_odd)