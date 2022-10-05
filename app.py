from parse.obj_parse import Book, Games, Films

def main():
    python_course = Book('https://play.google.com/store/books?hl=ru&gl=US')
    python_course.get_html()
    python_course.parse()
    python_course.save('books.json')

    python_course = Games('https://play.google.com/store/games?hl=ru&gl=US')
    python_course.get_html()
    python_course.parse()
    python_course.save('games.json')

    python_course = Films('https://play.google.com/store/movies?hl=ru&gl=US')
    python_course.get_html()
    python_course.parse()
    python_course.save("films.json")


if __name__ == "__main__":
    main()    