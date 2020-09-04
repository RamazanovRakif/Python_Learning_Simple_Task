"""
List,Dict,Tuple

Istənilən proqramlaşdırma dilində data type ən vacib konseptlərdən biridir.
Dəyişənlər müxtəlif tipli məlumatları saxlaya bilir və müxtəlif növlər fərqli şeylər edə bilər.
Pythonda s;ralama işləri üçün nəzərdə tutulmuş data type növlərindən squence types (List,Dict,Tuple) mövcuddur.

1) List 
List data type əslində string məntiqine oxşardı. Yəni 
text="Pragmatech".split() 
elan edersek Pragmatech textini, text=["P","r","a","g","m","a","t","e","c","h"] list formasina salacaqdir

Listler index=>value prinsipine uygun isləyir
"""
# -------------------------------------------------List type-----------------------------------------------------------
myList = ["Salam", 25, True, 23.5]
print(myList[0])  # listimizin 0-cı indexinde Salam sözu yerlesir
print(type(myList))  # type methodu ile listimizin tipini gormus olduq

# bəzi list methodlarına baxaq

# append methodu
# append methodu ile listimizin sonuna istediyimizi elave edirik
myList.append("Pragmatech")
print(myList)

# Clear methodu listimizin icin temizleyir
# copy methodu listimizi copy edib basqa bir list yaradir

# count methodu listimizin icerisindeki eyni olan ifadelerin sayini gosterir
# meselcun: myList=["a",4,3,"a"] burada myList.count() cagirarsaq bize 2 neticesin qaytaracaq. Cunki listimizde 2 a vardir

# Sort methodu listimizi siralama islerine baxir eger listimiz numberlardan ibaret olarsa number uzre siralayacaq stringden ibaret olarsa alfabetik formada siralayacaq

# reverse methodu Listimizin icindeki datalari tersine cevirir
myList.reverse()
print(myList)

# extend methodu listimize yeni bir list daxil etmek isteyende istifade edirik
newList = [4, 9, "AZE"]
myList.extend(newList)
print(myList)

# insert methodu gosterdiyimiz indexden etibaren elave edir
myList.insert(1, "Azerbaycan")
print(myList)

print("*"*100)
# -------------------------------------------Dict type----------------------------------------

"""
Dictionary data type sıralanmamış, dəyişdirilə bilən və indekslənmiş bir kolleksiyadır. Pythonda dict {}-ilə yazılır .

dictler listlerden ferqli olaraq key=>value prinsipile isleyir
myDict={
    "Baku":{
        "number":10
    },
    "Sumqayit":{
        "number":50
}

}

bu dictimizde konkret key value prinsipi gosterilmisdir.Key Number,Value 10,50

Proyektlerde isleyen zaman yerine gore list ve dict istifade etmeye calismaliyiq mentiqle eger biz indexe gore emeliyyatlar aparacayisa onda list yox keye gore emeliyyatlar aparacayiqsa dictlerden istifade olunmalidir


"""
# Dict methodlari_Bəzilərinə baxaq

mydict = {

    "name": "Rakif",
    "age": 22,
    "group": "Covid-1911"


}
#items()-dediyimiz kimi key=> value prinspi oldugu ucun
for key,value in mydict.items():
    print(key,value) # items methodu vasitesile key ve value almis olduq

# items le paralel keys ve values methodlarida movcuddur bu methodlarla ayriliqda key ve value deyerlerini ala bilerik
# clear ve copy methodlari uygun olaraq dicti silmek ve yeni bir dicte copy etmek ucn istifade olunur

#Update methodu

mydict.update({"surname":"Ramazanov"})
print(mydict)

#get methodu
print(mydict.get("name"))

print("*"*100)
# ve s....

#--------------------------------------Tuple type-------------------------------

#Tuple deyisdirile bilinmeyen bi data type novudur. () moterizeler vasitesile yazilir

myTuple=("One","Two","Three")
print(myTuple)
#indexe gore muraciet ede bilirik
print(myTuple[1])

# iki methodu movcuddur count ve index
print(myTuple.index("One")) # indexini oyrene bilirik
 #count methodu dier tiplerdeki kimidir
