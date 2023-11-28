from inputs_module import  askforname, askfornum, generate_id
from filehandler import  save_new_book, get_all_books, search_book


def create_book():
    bookname = askforname("please enter your book name: ")
    pages = askfornum("please enter number of pages: ")
    # print(bookname, pages)
    id = generate_id()
    bookdata = {"id":id,
        "name": bookname, "pages": pages}
    # print(bookdata)
    save_new_book(bookdata)

def find_book():
    id = askfornum("please enter book id: ")
    book = search_book(id)
    print(book)

def mainmenu():
    while True:
        print("----------------------------------")
        choice = input("""please enter n for new, l for list,"
                       f find book, e for exit: """)
        if choice=='n':
            create_book()
        elif choice=='l':
            books=get_all_books()
            print(books)
        elif choice=='f':
            find_book()

        elif choice=='e':
            exit()
        else:
            print("please enter valid choice")


if __name__ =='__main__':
    mainmenu()