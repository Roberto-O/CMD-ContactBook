# pylint: disable=no-value-for-parameter
import click
import client

@click.command()
def help():
    click.clear()
    click.echo('Available commands are:')
    click.echo('newContact\nshowContacts\nsearchContacts\nremoveContact\nupdateContact')

@click.command()
def newContact():
    click.echo('--- New Contact ---')

    firstName = click.prompt('First name')
    lastName = click.prompt('Last name')
    companyName = click.prompt('Company name')
    address = click.prompt('Address')
    phoneNumber = click.prompt('Phone number (format: (xxx) xxx-xxxx)') #Validity Check Needed
    email = click.prompt('Email address')

    click.echo('\n--- New Contact Added Successfully ---')
    click.echo(firstName + ' ' + lastName + '\n' + companyName + '\n' + address + '\n' + phoneNumber + '\n' + email)

    createTask = (1, firstName, lastName, companyName, address, phoneNumber, email)
    client.createContact(createTask)

@click.command()
def showContacts():
    click.echo('--- All Contacts ---')
    click.echo('todo')

@click.command()
def searchContacts():
    click.echo('--- Search Contacts - Select Number Option ---')
    option = click.prompt('1 - Search by last name\n2 - Search by first name\n3 - Search by full name\n4 - Search by company\n5 - Search by address\n6 - Search by phone number\n7 - Return to main menu\n')
    if(option == '1'):
        input = click.prompt('Enter Last Name')
        rows = client.searchByLast(input)
        for row in rows:
            print(row)
    elif(option == '2'):
        input = click.prompt('Enter First Name')
        client.searchByFirst(input)
    elif(option == '3'):
        input_l = click.prompt('Enter Last Name')
        input_f = click.prompt('Enter First Name')
        client.searchByFull(input_l, input_f)
    elif(option == '4'):
        input = click.prompt('Enter Company Name')
        client.searchByCompany(input)
    elif(option == '5'):
        input = click.prompt('Enter Address')
    elif(option == '6'):
        input = click.prompt('Enter Phone Number (xxx) xxx-xxxx')
    elif(option == '7'):
        help()
    #Ask after it has found the contact wheter they want to update or delete the contact
    if click.confirm('Would you like to update this contact?'):
        updateContact(1) #1 is placeholder
    if click.confirm('Would you like to delete this contact?'):
        removeContact(1) #1 is a placeholder

def removeContact(id):
    removeTask = id
    client.removeContact(removeTask)
    click.echo('Contact Removed.')

def updateContact(id):
    click.echo('--- Update Contact ---')
    click.echo('What would you like to update?')
    option = click.prompt('1 - Last name\n2 - First name\n3 - Company\n4 - Address\n5 - Phone number\n6 - Email\n')
    if(option == '1'):
        newLName = click.prompt('Enter New Last Name')
        updateLNTask = (newLName, id)
        client.updateLastName(updateLNTask)
    elif(option == '2'):
        newFName = click.prompt('Enter New First Name')
        updateFNTask = (newFName, id)
        client.updateFirstName(updateFNTask)
    elif(option == '3'):
        newCompName = click.prompt('Enter New Company Name')
        updateCompTask = (newCompName, id)
        client.updateCompany(updateCompTask)
    elif(option == '4'):
        newAddr = click.prompt('Enter New Address')
        updateAddrTask = (newAddr, id)
        client.updateAddr(updateAddrTask)
    elif(option == '5'):
        newNumber = click.prompt('Enter New Phone Number (xxx) xxx-xxxx ')
        updateNumTask = (newNumber, id)
        client.updateNum(updateNumTask)
    elif(option == '6'):
        newEmail = click.prompt('Enter New Email')
        updateEmailTask = (newEmail, id)
        client.updateEmail(updateEmailTask)
    click.echo('Contact updated.')
