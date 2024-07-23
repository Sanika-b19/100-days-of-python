import os

# Clears the screen on Windows
os.system('cls')



def bidder(bidding_record):
    highest_bid=0
    winner = ""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner = bidder
    print(f"highest bidder is {winner} with ${highest_bid}")



empty_dict = {}
is_continue = True
while is_continue:
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /________/
                         `'-------'`
                       .-------------.
                     /_______________/
''')
    name = input("Enter your name : ").lower()
    bid = int(input("Enter your bid : "))
    empty_dict[name]=bid

    result = input("Are there more person to bid? [Yes/No] : ").lower()
    if result == 'yes':
        os.system('cls')        
      
    elif result=='no':
        os.system('cls')                
        is_continue = False   
        bidder(empty_dict)    


    

