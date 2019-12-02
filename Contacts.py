# pylint: disable=no-value-for-parameter
import click

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
    phoneNumber = click.prompt('Phone number')
    email = click.prompt('Email address')

    click.echo('\n--- New Contact Added Successfully ---')
    click.echo(firstName + ' ' + lastName + '\n' + companyName + '\n' + address + '\n' + phoneNumber + '\n' + email)

@click.command()
def showContacts():
    click.echo('--- All Contacts ---')
    click.echo('todo')

@click.command()
def searchContacts():
    click.echo('--- Search Contacts ---')
    click.echo('todo')

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
