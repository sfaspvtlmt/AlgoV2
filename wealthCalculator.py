

Riyaaz = 0

Rishee = 1231000

AnkitBhaiya = 0

Arush = 520000

NewClient =8750000

Return = 20

i =1

months =6



    
while (i<=months):
    
    
    Riyaaz = Riyaaz*(1+0.005*Return)
    
    Rishee = Rishee*(1+0.007*Return)
    
    NewClient = NewClient*(1+0.007*Return)
    
    
    Arush = Arush*(1+0.01*Return) + Riyaaz * (0.005*Return) + Rishee * \
        (0.003*Return) + NewClient*(0.003*Return)

    # Arush*(1+0.01*Return) + 
    
    print()
    print()
    
    print("Month: "+ str(i))
    print()
    
    print("Riyaaz: " + str(round(Riyaaz/100000,2)) +" Lakhs ")
    print()
    
    print("Rishee: " + str(round(Rishee/100000,2)) + " Lakhs ")
    print()

    print("Ankit Bhaiya: " + str(round(AnkitBhaiya/100000,2)) +" Lakhs ")
    print()

    print("Arush: " + str(round(Arush/100000,2)) +" Lakhs ")
    print()

    print("New Client: " + str(round(NewClient/100000,2)) +" Lakhs ")
    
    i = i+1