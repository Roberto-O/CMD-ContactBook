# pylint: disable=no-value-for-parameter
import click
import client
import sqlite3

#database = 'contacts.db'

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

    task = (2, firstName, lastName, companyName, address, phoneNumber, email)
    client.createContact(task)

@click.command()
def showContacts():
    click.echo('--- All Contacts ---')
    click.echo('todo')

@click.command()
def searchContacts():
    i = 0
    click.echo('--- Search Contacts - Select Number Option ---')
    option = click.prompt('1 - Search by last name\n2 - Search by first name\n3 - Search by full name\n4 - Search by company\n5 - Search by address\n6 - Search by phone number\n7 - Return to main menu\n')
    if(option == '1'):
        input = click.prompt('Enter Last Name')
        rows = client.searchByLast(input)
        for row in rows:
            print(i + '. ' + row)
            i += 1
    elif(option == '2'):
        input = click.prompt('Enter First Name')
        rows = client.searchByFirst(input)
        if(len(rows) == 1):
            for row in rows:
                print(str(i) + '. ' + str(row))
                i += 1
            numContact = click.prompt("Select contact number from list")
            print(client.testSearch())
    elif(option == '3'):
        input_l = click.prompt('Enter Last Name')
        input_f = click.prompt('Enter First Name')
        rows = client.searchByFull(input_l, input_f)
        for row in rows:
            print(i + '. ' + row)
            i += 1
    elif(option == '4'):
        input = click.prompt('Enter Company Name')
        rows = client.searchByCompany(input)
        for row in rows:
            print(row)
    elif(option == '5'):
        input = click.prompt('Enter Address')
    
    

@click.command()
def removeContact():
    click.echo('--- Remove Contact ---')
    toRemoveFN = click.prompt('Enter first name of contact')
    toRemoveLN = click.prompt("Last name")
    if click.confirm('Are you sure you want to remove this contact?'):
        click.echo('Contact removed.')
    else:
        click.echo('Contact was not removed.')

@click.command()
def updateContact():
    click.echo('--- Update Contact ---')
    toUpdate = click.prompt('Enter first name of contact')
    click.echo('todo')
    click.echo('Contact updated.')
