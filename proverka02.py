
# 1. Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 

# a=int(input("a = "))
# b=int(input("b = "))

# for i in range (a,b+1):
#     print (i)

# 2. А және В екі бүтін сандар берілген.
#  А<B болса, өсу ретімен немесе басқаша жағдайда кему ретімен А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# a=int(input("a = "))
# b=int(input("b = "))
# if a<b:
#     for i in range (a,b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

# 3. Екі бүтін А және В саны берілген, A>B.
#  А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз. Бұл тапсырмада if операторынсыз орындай аласыз. 
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')

# 4.Үстел ойыны үшін 1-ден N-ге дейінгі сандары бар карталар пайдаланылады.Бір карта жоғалады.
#  Қалған карталардың сандарын білу арқылы оны табыңыз. 
# N саны берілген, содан кейін N − 1 қалған карталардың саны (1-ден N-ге дейінгі әртүрлі сандар).
#  Бағдарлама жоғалған картаның нөмірін көрсетуі керек. 
# def missing_card(N, cards):
#     return sum(range(1, N + 1)) - sum(cards)

# N = int(input("Карталар санын енгізіңіз: "))
# cards = [int(input("Карта нөмірін енгізіңіз: ")) for i in range(N - 1)]
# print("Жетіспейтін карта: ", missing_card(N,cards))




def Turlendiru(soilem):
    upper_count = 0
    lower_count = 0
    
    for char in soilem:
        if char.isupper():
            upper_count = upper_count+1
        elif char.islower():
            lower_count = 1 +lower_count
            
    if upper_count > lower_count:
        return soilem.upper()
    else:
        return soilem.lower()

soilem = str(input("soilem zhaz : "))
turlengen_s = Turlendiru(soilem)
print(turlengen_s) 
