import exchangelib
from getpass import getpass


password = getpass()

cred = exchangelib.Credentials("jonathan.wyss@santismail.ch",password)


config = exchangelib.Configuration(server="outlook.office.com",credentials=cred)

acc = exchangelib.Account("jonathan.wyss@santismail.ch",credentials=cred,autodiscover=True,config=config)

for item in account.inbox.all().order_by("-datetime_received")[:100]:
    print(item.subject)
