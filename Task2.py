# # Kitab magazasindaki kitablarin melumatlarini bir yere yigib cap edin

books = {}
for i in range(2): # Burda 2 vermekde meqsedim evvelce 2 kitab yaradilsin daha sonra icinde dovr edib datalari ala bilek formal xarakter dasiyir
    category_Name = input("Kateqoriya adını daxil edin:")
    book_name = input("Kitabın adını daxil edin:")
    book_price = int(input("Kitabın qiymətini daxil edin:"))
    book_page = int(input("Kitabın səhifə sayını daxil edin:"))
    book_genre = input("Kitabın janrını daxil edin:")

    books.update({
        category_Name: {
            'name': book_name,
            'price': book_price,
            'page': book_page,
            'genre': book_genre
        }
    })
print(books)    

category_Name = input("Istediyiniz kitabin kateqoriya adını daxil edin:")
book=books[category_Name]
print(book)
print( f"Axtardiginiz {category_Name} kateqoriya aid olan kitab:{book['name']}in qiymeti {book['price']} sehife sayi {book['page']} janri isə {book['genre']}")
