#Task- Istifadəçinin daxil etdiyi ifadəni tərsinə çevirib ekrana yazın

text=input("Ifadənizi daxil edin:")
 # 1ci yol
print(text[::-1])

# 2-ci yol
reversed = ''.join(reversed(text))
print(reversed)  
