from parse.book_parse import HW

def main():
    python_course = HW('https://play.google.com/store/books?hl=ru&gl=US')
    python_course.get_html()
    python_course.parse()
    python_course.save('res.json')


if __name__ == "__main__":
    main()    