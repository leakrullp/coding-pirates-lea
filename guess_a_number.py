import random

def guess_number():
    # Pick a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Jeg tænker på et tal mellem 1 og 100.")
    
    while True:
        try:
            guess = int(input("Gæt et tal: "))
            attempts += 1
            
            if guess < secret_number:
                print("For lavt! Prøv igen.")
            elif guess > secret_number:
                print("For højt! Prøv igen.")
            else:
                print(f"🎉 Rigtigt! Tallet var {secret_number}.")
                print(f"Du var {attempts} forsøg om at gætte det.")
                break
        except ValueError:
            print("Du skal skrive et rigtigt tal.")

# Run the game
guess_number()
