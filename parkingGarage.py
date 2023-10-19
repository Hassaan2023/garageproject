class ParkingGarage:
    def __init__(self, max_spaces):
        self.max_spaces = max_spaces
        self.tickets = [i for i in range(1, max_spaces + 1)]
        self.parking_spaces = [i for i in range(1, max_spaces + 1)]
        self.current_ticket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parking_spaces.pop(0)
            self.current_ticket[ticket] = {'paid': False, 'space': space}
            print(f"Take your ticket. Your parking space is {space}.")
        else:
            print("Sorry, the parking garage is full. No more tickets available.")

    def payForParking(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_ticket:
            if not self.current_ticket[ticket]['paid']:
                payment = input("Enter your payment amount: ")
                if payment:
                    self.current_ticket[ticket]['paid'] = True
                    print("Thank you for your payment. You have 15 minutes to leave.")
                else:
                    print("Payment not provided. Your ticket is not paid.")
            else:
                print("Your ticket is already paid.")
        else:
            print("Invalid ticket number.")

    def leaveGarage(self):
        ticket = int(input("Enter your ticket number: "))
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]['paid']:
                space = self.current_ticket[ticket]['space']
                self.parking_spaces.append(space)
                self.tickets.append(ticket)
                del self.current_ticket[ticket]
                print("Thank you, have a nice day!")
            else:
                print("Your ticket is not paid. Please pay before leaving.")
        else:
            print("Invalid ticket number. Please check your ticket.")

if __name__ == "__main__":
    garage = ParkingGarage(10)  # Example with 10 parking spaces
    while True:
        print("What would you like to do?")
        print("1. Take Ticket")
        print("2. Pay for Parking")
        print("3. Leave Garage")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            garage.takeTicket()
        elif choice == '2':
            garage.payForParking()
        elif choice == '3':
            garage.leaveGarage()
        elif choice == '4':
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
