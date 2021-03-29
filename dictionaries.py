customer = {
    "name" : "Bidesh Biswas",
    "age" : 25,
    "is_verified": True
}
customer["name"] = "Bidesh Biswas Biki" #name updated
customer["birthdate"] = "April 30 1996"
print(customer["name"])
print(customer["birthdate"])

####

phone = input("Phone: ")

digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)