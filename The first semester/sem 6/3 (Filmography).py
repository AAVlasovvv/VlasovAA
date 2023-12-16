from tkinter import *
from tkinter import ttk
import random
import pandas as pd
top = pd.read_csv('imdb_top_250.csv')
top_genres_list = list(top['Genre'])
# print(top_genres_list)
top_genres_list_dirty = list(top['Genre'])
# print(top_genres_list_dirty)
# попробуйте посмотреть промежуточный результат в film_list
#print(film_genres_list)

complex_genres = [] # будем хранить составные жанры, чтобы потом их удалить
for film_genre in top_genres_list:
    genres = film_genre.split(' | ') # разберем каждый составной жанр на составляющие
    if len(genres) > 1: # если попался составной жанр
        for genre in genres: # то пройдемся по всем элементарным жанрам фильма
            top_genres_list.append(genre) # и добавим их
        complex_genres.append(film_genre)
# обратите внимание, что мы не можем в процессе итерации через for удалять элементы, поскольку это собьет итератор. Можете посмотреть, к чему это приведет, написав вместо complex_genres.append(film_genre) сразу film_genres_list.remove(film_genre)

for genre in complex_genres:
    top_genres_list.remove(genre) # удалим все составные жанры из списка жанров

genres_set = list(set(top_genres_list)) # чтобы сделать из этого set! теперь здесь лежат все уникальные элементарные жанры
# print(genres_set)

top_films_list = list(top['Title'])
# print(top_films_list)
#
# print(top_genres_list_dirty)

A = [[i] for i in top_genres_list_dirty]

for i in range(0, len(A)):
    A[i] = A[i][0].split(' | ')
# print(A)
B = [[] for _ in range(len(genres_set))]
# print(B)
for i in range(0, len(genres_set)):
    for j in range(0, len(top_films_list)):
        if str(genres_set[i]) in A[j]:
            B[i].append(top_films_list[j])
# print(B)

choice_film = dict(zip(genres_set, B))

# f = input()
# print(choice_film[f])
# print(random.choice(choice_film[f]))








def choicing_film(*args):
    try:
        value = str(Genre.get())
        selected_film.set(random.choice(choice_film[value]))
    except ValueError:
        pass

# Создадим основное окно приложения
root = Tk()
root.title("Filmography")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

Genre = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=Genre)
feet_entry.grid(column=2, row=1, sticky=(W, E))

selected_film = StringVar()
ttk.Label(mainframe, textvariable=selected_film).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Найди фильм", command=choicing_film).grid(column=2, row=3, sticky=W)

# косметические подписи, обратите внимание на расположение
ttk.Label(mainframe, text="Введите жанр фильма:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Фильм, который вы можете посмотреть: ").grid(column=1, row=2, sticky=E)


# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# сразу помещает курсор ввода в поле feet_entry
feet_entry.focus()
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось calculate
root.bind("<Return>", choicing_film)

# циклим наше окно
root.mainloop()

