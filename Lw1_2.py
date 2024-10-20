# TODO Найдите количество книг, которое можно разместить на дискете
disk_mb=1.44
book_list=100
book_str=50
book_sumbols=25
M_sumbol=4

disk_B=disk_mb*1024*1024
M_book=book_list*book_str*book_sumbols*M_sumbol
S_books=disk_B/M_book

print("Количество книг, помещающихся на дискету:", int(S_books))
