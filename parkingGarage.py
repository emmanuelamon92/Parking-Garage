# from IPython.display import clear_output

class Garage:
    
    def __init__(self):
        self.currentTickets = {}
  
    def tickets(self):
        self.currentSpaces = 10
        self.tickets=[1,2,3,4,5,6,7,8,9,10]


    def takeTicket(self):
        print("\nim in takeTicket")
        
        
        for i in range(len(self.tickets)):
            for key, value in self.currentTickets.items():
                if self.current.spaces>0:
                    self.currentTickets[self.tickets[0]]={"paid": False}
                    print(f'\nYour ticket is ticket #{self.tickets[0]}! Please park safely!')
                    del self.tickets[0]
                    self.current.spaces -=1
                else:
                    print('No more spaces available')
            return self.tickets
                
    def payForParking(self):
        print(f"\nim in payForParking")
        
        user_input = int(input("What is your ticket number? "))
        if  self.currentTickets[user_input] == {"paid": False}:
            print("Your ticket has been paid! Please leave within 15 minutes ")
            return self.currentTickets[user_input] == {"paid": True}
        else: 
            print("There is no such ticket in use. This ticket is still available!")
       

    def leaveGarage(self, ticket_input):
        self.ticket_input= ticket_input

        if self.currentTickets[int(self.ticket_input)]["paid"] == True:
            self.tickets.append(ticket_input)
            del self.currentTicket[ticket_input]
            self.currentSpaces+=1
        
            print("Your ticket was paid! Have a nice day!")
            
            
        elif self.currentTickets[int(ticket_input)]["paid"] == False:
            print("Your ticket was not paid. Please pay for your ticket.") 
            return self.payForParking()         
        else:
            print("Oops wrong choice. Seems like this ticket is still available")
            

class main:

    def run(self):
        mygarage = Garage()
        while True:

            choice = input(f"\nWelcome to SuperLot! These are the spaces currently available: {sorted(mygarage.tickets)}"
                           "\nWould you like to get a ticket, pay, or leave? ").lower()
            
            if choice == "ticket":
                mygarage.takeTicket()

            elif choice == "pay":
        
                if mygarage.currentTickets == {}:
                   print("There are no tickets to be paid")
                else:
                    mygarage.payForParking()
                
            elif choice == "leave":
                
                if mygarage.currentTickets == {}:
                    print("No ticket was issued. Type in \"ticket\" to get a ticket" )
                else:
                    ticket_input = int(input("What is your ticket number? "))
                    mygarage.leaveGarage(ticket_input)
            else:
                print(f"\nIt seems that '{choice}' is not a valid input. Please make sure you type 'ticket', 'pay', or 'leave'.")

#               clear_output()
            

testing = main()
testing.run()
              
# testing = Garage()
# testing.tickets()