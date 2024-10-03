#Python Alıştırmalar

#Görev 1
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
C = 23 < 19
l = [1, 2, 3, 4]
d = {"Name": "Jake", "Age": 27, "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(C))
print(type(l))
print(type(d))
print(type(t))
print(type(s))

#Görev 2
text = "The goal is to turn data into information, and information into insight."
text_upper = text.upper()
text_replaced = text_upper.replace(",", " ").replace(".", " ")
text_split = text_replaced.split()
print(text_split)

#Görev 3
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

eleman_sayisi = len(lst)
print(f"Eleman sayısı: {eleman_sayisi}")

ilk_eleman = lst[0]
onuncu_eleman = lst[10]
print(f"Sıfırıncı eleman: {ilk_eleman}, Onuncu eleman: {onuncu_eleman}")

sub_list = lst[0:4]
print(f"Oluşturulan alt liste: {sub_list}")

lst.pop(8)
print(f"Sekizinci indeksteki eleman silindikten sonra liste: {lst}")

lst.append("X")
print(f"Yeni eleman eklendikten sonra liste: {lst}")

lst.insert(8, "N")
print(f"Sekizinci indekse 'N' eklendikten sonra liste: {lst}")

#Görev 4
my_dict = {
    'Christian': ["America", 18],
    'Daisy': ["England", 12],
    'Antonio': ["Spain", 22],
    'Dante': ["Italy", 25]
}

keys = my_dict.keys()
print(f"Keys: {keys}")

values = my_dict.values()
print(f"Values: {values}")

my_dict['Daisy'][1] = 13
print(f"Daisy'nin yaşını 13 olarak güncelledikten sonra dictionary: {my_dict}")

my_dict['Ahmet'] = ["Turkey", 24]
print(f"Ahmet'i dictionary'e ekledikten sonra dictionary: {my_dict}")

my_dict.pop('Antonio')
print(f"Antonio'yu dictionary'den sildikten sonra dictionary: {my_dict}")

#Görev 5
l = [2, 13, 18, 93, 22]


def func(numbers):
    even_list = []
    odd_list = []

    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list


even_list, odd_list = func(l)

print(f"Çift sayılar: {even_list}")
print(f"Tek sayılar: {odd_list}")

#Görev 6
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler[:3],1):
    print(f"Mühendislik Fakültesi {i}. öğrenci: {ogrenci}")

for i, ogrenci in enumerate(ogrenciler[3:],1):
    print(f"Tıp Fakültesi {i}. öğrenci: {ogrenci}")

#Görev 7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for d_kodu, k, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {k} olan {d_kodu} kodlu dersin kontenjanı {kont} kişidir.")

#Görev 8
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume_kontrol(k1, k2):
    if k1.issuperset(k2):
        ortak_elemanlar = k1.intersection(k2)
        return ortak_elemanlar
    else:
        fark = k2.difference(k1)
        return fark

sonuc = kume_kontrol(kume1, kume2)
print(sonuc)