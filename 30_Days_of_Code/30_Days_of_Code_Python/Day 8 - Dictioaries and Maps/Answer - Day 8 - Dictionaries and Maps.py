# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    total_no_of_entries = int(input())
    phone_book = {}

    for i in range(total_no_of_entries):
        name,phone_number = input().split()
        phone_book[name] = phone_number

    while 'True':
        try:
            search_name = str(input())

            if search_name in phone_book:
                print(str(search_name)+"="+str(phone_book[search_name]))
            else:
                print("Not found")
        except EOFError:
            break
