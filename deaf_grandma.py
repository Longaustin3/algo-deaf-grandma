def deaf_grandma():
    # track the number of times user says goobye
    goodbye_counter = 0

    # initiate conversation with grandma
    response = input("HEY KID!\n")

    # continue talking to grandma so long as user has not said goobye twice
    while goodbye_counter < 2:
        #increase goodbye counter for each goodbye and break the loop when it hits 2
        if response == "GOODBYE!" and goodbye_counter == 1:
                print("LATER SKATER!")
                goodbye_counter += 1
                break
        if response == "GOODBYE!" and goodbye_counter == 0:
                response = input("LEAVING SO SOON?\n")
                goodbye_counter += 1
        # if there is no response
        if response == "":
            response == input("WHAT?!\n")
        # if the response is in all uppercase
        elif response.upper() == response:
            response = input("NO, NOT SINCE 1946!\n")
        # any other conditions that include lowercase letters
        else:
            response = input("SPEAK UP KID!\n")
        
deaf_grandma()
