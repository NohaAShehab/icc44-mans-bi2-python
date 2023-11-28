
import  json

def get_all_books():
    try:
        filobject = open("bookdata.json", "r")
    except Exception as e:
        print(e)
    else:
        data = filobject.read() # string
        # print(f"data = {data}")
        filobject.close()
        # print(data, len(data))
        data= data.strip('\n')
        if data:
            # get valid python data from string
            file_data = json.loads(data)
            return  file_data
        return []




def save_new_book(bookdata: dict):
    old_data = get_all_books()  # list
    old_data.append(bookdata)
    # print(f"from save new book {bookdata}")

    # convert old_data to valid json string
    valid_data = json.dumps(old_data, indent=2)


    try:
        fileobj = open("bookdata.json", "w")
    except Exception as e:
        return  False
    else:
        # saving the data in the file
        fileobj.write(valid_data)
        fileobj.close()
        return  True



def search_book(bookid):
    all_books = get_all_books()
    for index, book in enumerate(all_books):
        if book['id']==bookid:
            print('found')
            return  index, book
    else:
        print("==== not found =====")
        return False

if __name__ == "__main__":
    data=get_all_books()
    print(data)

