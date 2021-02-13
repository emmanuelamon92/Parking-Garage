#class for all things tickets
class ticket:
    def __init__(self):   
        self.ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
    currentTicket = {'Paid' : True, 'Unpaid' : False}
    pass


#class for all things parking
class parking:
    def __init__(self):
        self.spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return self.spaces
    pass


class garage:
    def __init__(self):
        pass
    def takeTicket(self, ticket, spaces):
        #decrease the tickets available by 1
        ticket = ticket()
        return ()
        for i in range(len(ticket)):
            del ticket[0]
            return f'Your ticket is ticket {ticket[0]}! Please park safely!'

        #decrease the amount of spaces available by 1
        pass

    #should update currentTicket dictionary
    def payForParking(self, user_input):
        self.user_input = 6
        if user_input == True:
            print('Your ticket has been paid! Please leave within 15 minutes')
            #???
        pass

    def leaveGarage(self);
    #if ticket paid in full or currentTicket is true(must call ticket)
        if currentTicket == True:
            print ("Thank you, have nice day!")
        else:
            payForParking()
            #increase by one
        pass


class main:
    def run(self):
        mygarage = garage()
        while True

            choice = input ("Would you like to get a ticket, pay, or leave?").lower()
            
            if choice == "ticket":
                mygarage.takeTicket()

            elif choice == "pay":

            elif choice == "leave":

            else:
                "invalid responce"
            clear_output()


            ticket = ticket()
            parking = parking()
            garage = garage()
            user_input = True

# currentTicket { 1: { "paid": False}
# }
# once they pay it will look like

# currentTicket { 1: { "paid": True}

# and for every ticket/space taken it will update with the key (which is going to be our ticket number) and the value 
# (that is going to be another dictionary with the key"paid" and the value of True or False)

# once we add stuff it will look like this

# currentTicket { 1:{"paid": False}, 2:{"paid": True}, 3:{"paid": False}}

# CristinaGradinaruToday at 10:41 AM
# so to access the value true or false we will need a function that does " if currentDict[int(choice)]["paid"] = True then print("Your ticked was 
# paid! Have a nice day or something ") elif : currentDict[int(choice)]["paid"] = False then print("Your ticket was not paid. Please pay for your 
# ticket." else: print("Oops wrong choice. Seems like this ticket is still available")