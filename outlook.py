import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").getNamespace("MAPI")

inbox = outlook.getDefaultFolder(6).Folders

messages = inbox[0].Items

for i in range(len(messages)):
    message = messages.Item(i+i)
    print(message)
