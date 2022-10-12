from parse.obj_parse import Book, Child, Games, Films

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

    python_course = Child('https://play.google.com/store/apps/category/FAMILY?hl=ru&gl=US')
    python_course.get_html()
    python_course.parse()
    python_course.save("childs.json")


if __name__ == "__main__":
    main()    