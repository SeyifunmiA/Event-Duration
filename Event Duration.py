hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

amountmins= mins+dura
totalmins=amountmins%60
amounthrs=amountmins//60
totalhrs=hour + amounthrs
newhours=totalhrs%24
print(newhours,":",totalmins, sep="")

