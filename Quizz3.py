import requests
import  json
import sqlite3


#გამოვიძახეთ get, headers და status code, არჩევანის საშუალებას ვაძლევთ მომხმარებელს მიიღოს სრული ინფორმაცია ან კონკრეტული ანიმეს შესახებ.
id = ""

# choice = input("რომელი ანიმე გსურთ?: 1)Grave of the Fireflies, 2)Castle in the Sky 3)all(შეიტანე ნებისიერი სხვა რამე)")
# try:
#     if choice == "1":
#         id = "12cfb892-aac0-4c5b-94af-521852e46d6a"
#     elif choice == "2":
#         id = "2baf70d1-42bb-4437-b551-e5fed5a87abe"
#
# except:print("შეიყვანეთ მხოლოდ რიცხვი მაგ(1)")


URL = f"https://ghibliapi.herokuapp.com/films/{id}"
Page = requests.get(URL)


print(Page.text)
# print(Page.status_code)
# print(Page.headers)

#json ფაილის შექმნა და ინფორმაციის შეტანა

json_page = Page.json()
# with open("anime.json","w") as j:
#     json.dump(json_page,j,indent=4)



#ეს გვიგდებს ანიმეების სათაურებსა და ორიგინალ სათაურებს

# for each in json_page:
#     print(each['title']+", "+each['original_title'])



anime_database = sqlite3.connect("anime.sqlite")
c = anime_database.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS anime
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             title VARCHAR(100),
             release_date INTEGER(100),
             director VARCHAR(100))
''')


anime_info = []

for every in json_page:
    title = every["title"]
    release_date = every["release_date"]
    director = every["director"]
    row = []
    row.append(title)
    row.append(release_date)
    row.append(director)
    anime_info.append(row)


c.executemany(''' INSERT INTO anime(title, release_date, director)
                  VALUES (?,?,?)
''',anime_info)

anime_database.commit()
anime_database.close()






