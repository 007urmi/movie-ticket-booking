from Operation import Movie

row = int(input('Enter the number of rows:\n'))
seats = int(input("Enter the number of seats in each row:\n"))
while(True):
    ch = input("1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked Tickets User Info\n0. Exit\n")
    if ch == "1":
        c1 = Movie()
        c1.show_seats(row,seats)

    if ch == "2":
        c2 = Movie()
        c2.buy_ticket(row,seats)

    if ch == "3":
        c3 = Movie()
        c3.show_statistics(row,seats)

    if ch == "4":
        c4 = Movie()
        c4.show_booked_ticket()

    if ch == "0":
        c5 = Movie()
        c5.exit_method()
        break
