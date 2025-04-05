import sys

# Create a list of those who have not seen your promotional email yet. The list will be sent to the call center to reach those people
# clients - recipients        call_center

# Create a list of the participants who are not your clients. You will send them an introductory email about your products
# participants - clients                    potential_clients

# Create a list of the clients who did not participate in the event. You will send them a link to the video and slides of the event
# clients - participants                    loyalty_program

def get_result_list(operation : str) -> list:
    # your clients’ email accounts
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

    # the participants in your most recent event (some of them were your clients)
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

    # clients who viewed your most recent promotional email
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    sclients = set(clients)
    sparticipants = set(participants)
    srecipients = set(recipients)

    if operation == "call_center":
        return list(sclients.difference(srecipients))
    elif operation == "potential_clients":
        return list(sparticipants.difference(sclients))
    else:   # loyalty_program
        return list(sclients.difference(sparticipants))




if __name__ == "__main__": 
    arguments = sys.argv[1:]
    operations = ("call_center", "potential_clients", "loyalty_program")
    if len(arguments) == 1:
        if arguments[0] not in operations:
            raise Exception("Wrong operation :(")
        else:
            print(get_result_list(arguments[0]))