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

@click.command()
def showContacts():
    click.echo('--- All Contacts ---')
    click.echo('todo')

@click.command()
def searchContacts():
    click.echo('--- Search Contacts - Select Number Option ---')
    option = click.prompt('1 - Search by last name\n2 - Search by first name\n3 - Search by full name\n4 - Search by company\n5 - Search by address\n6 - Search by phone number\n7 - Return to main menu')
    if(option == '1'):
        input = click.prompt('Enter Last Name')
        client.searchByLast(input)
    elif(option == '2'):
        input = click.prompt('Enter First Name')
        client.searchByFirst(input)
    

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

