def show():
    print("Tickets:")
    print("1.First Class\n2.Second Class\n3.Third Class")

    fb=0
    sb=0
    tb=0

    while True:
        admit = input("What you prefer? - ")
        if(admit.strip()=='First Class'):

            if(fb<=10):
                print("Yes Available...")
                print("Cost: 170")
                check=input("Are you OK with that: yes or no: ")
                if(check=='yes'):
                    fb=fb+1
                    print("Your seat number:",end="")
                    yield 'A'+str(fb)
                    continue
                else:
                    print("Fine Try with other Class")
                    continue

            else:
                print("Not Available....")
                print("Check for Second Class and Third Ticket")
                continue
            print("\n")

        elif(admit.strip()=='Second Class'):

            if(sb<=20):
                print("Yes Available...")
                print("Cost: 120")
                check = input("Are you OK with that: yes or no: ")
                if (check == 'yes'):
                    sb=sb+1
                    if sb<=10:
                        print("Your seat number:",end="")
                        yield 'B'+str(sb)
                        continue
                    else:
                        print("Your seat number:",end="")
                        yield 'C'+str(sb)

                else:
                    print("Fine Try with other Class")
                    continue

            else:
                print("Not Available....")
                print("Check for First Class and Third Ticket")

            print("\n")

        elif(admit.strip()=='Third Class'):

            if (tb <= 20):
                print("Yes Available...")
                print("Cost: 70")
                check = input("Are you OK with that: yes or no: ")
                if (check == 'yes'):
                    tb = tb + 1
                    if tb <= 10:
                        print("Your seat number:", end="")
                        yield 'D' + str(tb)
                        continue
                    else:
                        print("Your seat number:", end="")
                        yield 'E' + str(tb)

                else:
                    print("Fine Try with other Class")
                    continue
            else:
                print("Not Available....")
                print("Check for First Class and Second Ticket")
                continue

            print("\n")
        else:
            continue

customer=show()
for i in range(50):
    print(customer.__next__())