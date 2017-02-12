# -*- encoding: utf-8 -*-

print ("Pozdravljeni tukaj lahko pretvorite kilometre v milje")

km = int(raw_input("Vnesite število kilomterov: "))

milje = km * 0.62137
print(milje)
vprasaj = raw_input("Ali želite nadaljevati da/ne?")

while vprasaj == "da":
    km = int(raw_input("Vnesite ponovno število: "))
    milje = km * 0.62137
    print(milje)
    vprasaj = raw_input("Ali želite nadaljevati da/ne?")
if  vprasaj == "ne":
    print "Nasvidenje"