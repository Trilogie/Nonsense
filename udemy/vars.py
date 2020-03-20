a = "    Cisco Switch    "

print(a.index("i"))
print(a.count("i"))
print(a.find("sco"))
print(a.find("xyz"))
print(a.lower())
print(a.upper())
print(a.startswith("C"))
print(a.endswith("h"))
print(a.endswith("q"))
print(a.strip())
print(a.replace(" ", ""))

d = "Cisco,Juniper,HP,Avaya,Nortel"
string = d.split(",")
print(string)

x = "Cisco"
y = " switch"
print(x+y)

print("o" in x)

k = "Cisco model: {2}, {1} WAN Slots, IOS {0}".format("2600XM", 2, 12.4)
print(k)

model = "2600XM"
slots = 4
ios = 12.3

print(f"Cisco Model: {model.lower()}, {slots * 2} WAN Slots, IOS {ios}")

string1 = "O E2 10.110.8.9 [160/5]"
print(string1[::-1])

