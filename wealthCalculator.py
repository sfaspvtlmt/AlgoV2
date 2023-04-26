

Riyaaz = 3200000

Rishee = 1240000

AnkitBhaiya = 0

Arush = 800000

NewClient =2000000

Return = 10
i =1
months =12



    
while (i<=months):
    
    
    Riyaaz = Riyaaz*(1+0.008*Return)
    
    Rishee = Rishee*(1+0.007*Return)
    
    NewClient = NewClient*(1+0.007*Return)
    
    # AnkitBhaiya = AnkitBhaiya*(1+0.000*Return)
    
    Arush = Arush*(1+0.01*Return) + Riyaaz * (0.002*Return) + Rishee * (0.003*Return) + NewClient*(0.003*Return) 
    
    print()
    print()
    
    print("Month: "+str(i))
    print()
    
    print("Riyaaz: " + str(round(Riyaaz/100000,2)) +"Lakhs ")
    print()
    
    print("Rishee: " + str(round(Rishee/100000,2)) + "Lakhs ")
    print()

    print("Ankit Bhaiya: " + str(round(AnkitBhaiya/100000,2)) +"Lakhs ")
    print()

    print("Arush: " + str(round(Arush/100000,2)) +"Lakhs ")
    print()

    print("New Client: " + str(round(NewClient/100000,2)) +"Lakhs ")
    
    i = i+1