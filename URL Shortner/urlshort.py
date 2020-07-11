import pyshorteners

url = input("Enter url : \n")

print("Url after processing : ",pyshorteners.Shortener().tinyurl.short(url))