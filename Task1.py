
def check_and_sum():
    while True:
        try:
            number = int(input("Eded daxil edin:"))
            summary = 0
            for num in range(number+1):
                summary += num
            print(summary)
        except ValueError:
            print("hahaha mene kelek gelme:))) Ancaq rəqəm və ya ədəd daxil edə bilərsən !..")


check_and_sum()
