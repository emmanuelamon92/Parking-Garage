# Start Your Code here
 from IPython.display import clear_output

class Garage:
    
    
#     def __init__(self):
#         print("\nim in __init__"
#         self.currentTickets = {}
         
        
#     def tickets(self):
#         self.currentTicket = []
#         self.currentSpaces = 10
#         self.tickets=[1,2,3,4,5,6,7,8,9,10]

#         for i in range(len(self.tickets)):
#             self.currentTicket.append(self.tickets[0])         
#             self.currentSpaces -= 1
#             del self.tickets[0]
            
#             print (self.tickets)

#     def tickets(self):
#         self.currentSpaces = 11
#         self.tickets=[]

#         for i in range(1, self.currentSpaces):
#             self.tickets.append(i)
#             self.currentSpaces -= 1

#             return (self.tickets)

    def tickets(self):
        self.currentSpaces = 1
        self.tickets=[]

        for i in range(self.currentSpaces, 11):
            self.tickets.append(i)
            self.currentSpaces += 1
    
            return (self.tickets)
            del self.tickets[0]


    def takeTicket(self):
        print("\nim in takeTicket")
#  
#       if self.tickets[0] not in self.currentTickets:
#         self.currentTickets[self.tickets[0]]={"paid": False}
#         print(f'\nYour ticket is ticket #{self.tickets[0]}! Please park safely! This is what\'s in the dictionary {self.currentTickets}')
#         return self.currentTickets    
                
    def payForParking(self):
        print(f"\nim in payForParking")
        
        user_input = int(input("What is your ticket number? "))
        if  self.currentTickets[user_input] == {"paid": False}:
            print("Your ticket has been paid! Please leave within 15 minutes ")
            return self.currentTickets[user_input] == {"paid": True}
        else: 
            print("There is no such ticket in use. This ticket is still available!")
       

    def leaveGarage(self, ticket_input):
        print ("im in leaveGarage")
        self.ticket_input= ticket_input

        if self.currentTickets[int(self.ticket_input)]["paid"] == True:
            self.tickets.append(ticket_input)
            del self.currentTicket[ticket_input]
            
            self.currentSpaces+=1
            
            
            print("Your ticket was paid! Have a nice day!")
            
            #return list of spaces and put ticket_input number back in ticket list.
            
        elif self.currentTickets[int(ticket_input)]["paid"] == False:
            print("Your ticket was not paid. Please pay for your ticket.") 
            return self.payForParking()         
        else:
            print("Oops wrong choice. Seems like this ticket is still available")
            
            
#     def tickets(self):
#         print("\nim in tickets")
        
# #         full_list = [1,2,3,4,5,6,7,8,9,10]
# #         tickets_ = [1,2,3,4,5,6,7,8,9,10]
    
# #             if len(tickets_) == 0:
# #                 tickets_.append(full_list)
# #                 return tickets_
# #             else:
# #                 del tickets_[0]

# #             return print(tickets_)             


class main:

    def run(self):
        mygarage = Garage()
        while True:

#             choice = input(f'\nWelcome to SuperLot! These are the spaces currently available: {mygarage.takeTickets}\nWould you like to get a ticket, pay, or leave?').lower()
            
            choice = input(f"\nWelcome to SuperLot! These are the spaces currently available: {mygarage.tickets}"
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
            

# testing = main()
# testing.run()
              
testing = Garage()
testing.tickets()

