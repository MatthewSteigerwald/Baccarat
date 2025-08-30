import tkinter as tk
from PIL import Image, ImageTk 
import random
from PIL import ImageEnhance

class baccarat:
    def __init__(self):
        # Making initial variables
        self.window = None
        self.balance = 2500
        self.bet = 0
        self.deck = None
        self.card_labels = []
        self.user_card_count = 0
        self.dealer_card_count = 0
    

    def setup_window(self):
        # Making a window
        self.window = tk.Tk()
        self.window.title("Baccarat Game")
        self.window.geometry("1500x1000")
        self.window.configure(bg="green")
        # Showing all buttons
        self.show_buttons()
        # Adding labels for the users message, bet, and balance
        self.message_label = tk.Label(self.window, text="" , font=('Times New Roman', 50), bg="green", fg="black")
        self.message_label.place(x=600, y=400)
        self.balance_label = tk.Label(self.window, text="Balance: $" + str(self.balance), font=('Times New Roman', 30), bg="green", fg="black")
        self.balance_label.place(x=20, y=20)
        self.bet_label = tk.Label(self.window, text="Bet: $" + str(self.bet), font=('Times New Roman', 30), bg="green", fg="black")
        self.bet_label.place(x=20, y=80)
        # Adding labels for the player and banker
        self.player_label = tk.Label(self.window, text="Player", font=('Times New Roman', 30), bg="green", fg="black")
        self.player_label.place(x=20, y=340)
        self.banker_label = tk.Label(self.window, text="Banker", font=('Times New Roman', 30), bg="green", fg="black")
        self.banker_label.place(x=1300, y=340)
        # Opening the window
        self.window.mainloop()


    def show_buttons(self):
        # Making a frame for the buttons
        button_frame = tk.Frame(self.window, bg="green")
        button_frame.pack(pady=20)
        # Player Button
        self.player_button = tk.Button(button_frame, text="Player", font=('Times New Roman', 20), bg="grey", fg="black",command=lambda: self.run_game(1))
        self.player_button.pack(side="left", padx=10)
        # Banker Button
        self.banker_button = tk.Button(button_frame, text="Banker", font=('Times New Roman', 20), bg="grey", fg="black", command=lambda: self.run_game(2))
        self.banker_button.pack(side="left", padx=10)

        # Making a frame for the chips
        chip_frame = tk.Frame(self.window, bg="green")
        chip_frame.pack(side="bottom", anchor="se", padx=20, pady=20)
        # Making an array of poker chip images
        casino_chip_images = [r"C:\Users\matth\Desktop\Python\Chips\pokerchip1.png", 
                            r"C:\Users\matth\Desktop\Python\Chips\pokerchip2.png",
                            r"C:\Users\matth\Desktop\Python\Chips\pokerchip3.png", 
                            r"C:\Users\matth\Desktop\Python\Chips\pokerchip4.png"]
        # Adds red chip image
        image = Image.open(casino_chip_images[0])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds red chip button
        red_chip_button = tk.Button(chip_frame, text="$5", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.red_chip)
        red_chip_button.image = photo
        red_chip_button.pack(side="left", padx=10)

        # Adds green chip image
        image = Image.open(casino_chip_images[1])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds green chip button
        red_chip_button = tk.Button(chip_frame, text="$25", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black",command=self.green_chip)
        red_chip_button.image = photo
        red_chip_button.pack(side="left", padx=10)

        # Adds blue chip image
        image = Image.open(casino_chip_images[2])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds blue chip button
        red_chip_button = tk.Button(chip_frame, text="$100", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.blue_chip)
        red_chip_button.image = photo
        red_chip_button.pack(side="left", padx=10)

        # Adds yellow chip image
        image = Image.open(casino_chip_images[3])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds yellow chip button
        red_chip_button = tk.Button(chip_frame, text="$250", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.yellow_chip)
        red_chip_button.image = photo
        red_chip_button.pack(side="left", padx=10)

        # Adds clear bet option button
        clear_bet_button = tk.Button(chip_frame, text="Clear Bet", font=('Times New Roman', 20), bg="grey", fg="black", command = self.clear_bet)
        clear_bet_button.pack(side="left", padx=10)
    
    def make_deck(self):
        # Making an array for each card rank
        ranks = [2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6,
                7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10,
                'J','J','J','J', 'Q','Q','Q','Q', 'K','K','K','K', 'A','A','A','A']
        # Making an array for each card suit
        suits = ['C','D','H','S'] * 13
        # Making an array containing each card image
        card_images = [r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\2_of_spades.png",
                r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\3_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\4_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\5_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\6_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\7_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\8_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\9_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_diamonds.png",r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\10_of_spades.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\jack_of_spades2.png",
                r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\queen_of_spades2.png",
                r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_clubs2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_diamonds2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_hearts2.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\king_of_spades2.png", 
                r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_clubs.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_diamonds.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_hearts.png", r"C:\Users\matth\Desktop\PNG-cards-1.3\ace_of_spades2.png"
                ]
        # Combine ranks and suits with images
        self.deck = [list(zip(ranks, suits)), card_images]

    def red_chip(self):
        # Adds 5 to the users bet
        if self.bet <= self.balance - 5:
            self.bet += 5
            self.update_bet("Bet: $" + str(self.bet))
    def green_chip(self):
        # Adds 25 to the users bet
        if self.bet <= self.balance - 25:
            self.bet += 25
            self.update_bet("Bet: $" + str(self.bet))
    def blue_chip(self):
        # Adds 100 to the users bet
        if self.bet <= self.balance - 100:
            self.bet += 100
            self.update_bet("Bet: $" + str(self.bet))
    def yellow_chip(self):
        # Adds 250 to the users bet
        if self.bet <= self.balance - 250:
            self.bet += 250
            self.update_bet("Bet: $" + str(self.bet))
        
    def update_balance(self, text):
        # Function to change the balance output in the window
        self.balance_label.config(text=text)

    def update_message(self, text):
        # Function to change the message output in the window
        self.message_label.config(text=text)
    def update_bet(self, text):
        # Function to change the bet output in the window
        self.bet_label.config(text=text)

    def clear_bet(self):
        # Makiing a function to clear the users bet
        self.bet = 0
        self.update_bet("Bet: $" + str(self.bet))

    def run_game(self, user_card_side):
        # Disabling player and banker buttons
        self.player_button.config(state="disabled")
        self.banker_button.config(state="disabled")
        # Making sure the cards appear on the correct side
        if user_card_side == 1:
            user_side = 'left'
            dealer_side = 'right'
        elif user_card_side == 2:
            user_side = 'right'
            dealer_side = 'left'

        self.make_deck()
        # Defining both user and dealer hands
        self.user_cards = [[],[]]
        self.dealer_cards = [[],[]]
        # Adding cards to both player and dealer hand
        for i in range(2):
            card_index = random.randrange(len(self.deck[0]))
            card = self.deck[0][card_index]
            self.user_cards[0].append(card)
            self.user_cards[1].append(self.deck[1][card_index])
            self.deck[0].remove(card)
            self.deck[1].remove(self.deck[1][card_index])
        for i in range(2):
            card_index = random.randrange(len(self.deck[0]))
            card = self.deck[0][card_index]
            self.dealer_cards[0].append(card)
            self.dealer_cards[1].append(self.deck[1][card_index])
            self.deck[0].remove(card)
            self.deck[1].remove(self.deck[1][card_index])

        # Showing in the window the users hand
        self.show_cards_window(self.user_cards[1][0], user_side)
        self.show_cards_window(self.user_cards[1][1], user_side)
        # Showing in the window the dealrs hand
        self.show_cards_window(self.dealer_cards[1][0], dealer_side)
        self.show_cards_window(self.dealer_cards[1][1], dealer_side)

        # Adding up the card counts for user and dealer hands
        self.user_card_count = self.calculate_counts(self.user_cards)
        self.dealer_card_count = self.calculate_counts(self.dealer_cards)

        # Printing user and dealer card counts
        print(self.user_card_count)
        print(self.dealer_card_count)

        # Working out the logic for each possability
        if (self.user_card_count == 9 and self.user_card_count != self.dealer_card_count):
            pass
        elif (self.dealer_card_count == 9 and self.user_card_count != self.dealer_card_count):
            pass
        elif (self.user_card_count == 8 and self.user_card_count != self.dealer_card_count):
            pass
        elif (self.dealer_card_count == 8 and self.user_card_count != self.dealer_card_count):
            pass
        else:
            if (self.user_card_count <= 5):
                # Adding another card to the users hand
                card_index = random.randrange(len(self.deck[0]))
                card = self.deck[0][card_index]
                self.user_cards[0].append(card)
                self.user_cards[1].append(self.deck[1][card_index])
                self.deck[0].remove(card)
                self.deck[1].remove(self.deck[1][card_index])
                self.user_card_count = self.calculate_counts(self.user_cards)
                print(self.user_card_count)
                self.window.after(3000, lambda: self.show_cards_window(self.user_cards[1][2], user_side))
                if (self.dealer_card_count > -1 and self.dealer_card_count < 3):
                    # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(5000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))

                elif(self.dealer_card_count == 3 and self.user_card_count != 8):
                    # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(5000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))
                elif(self.dealer_card_count == 4 and self.user_card_count > 1 and self.user_card_count < 8):
                   # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(5000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))
                elif(self.dealer_card_count == 5 and self.user_card_count > 3 and self.user_card_count < 8):
                    # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(5000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))
                elif(self.dealer_card_count == 6 and self.user_card_count > 5 and self.user_card_count < 8):
                    # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(5000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))
            else:
                # Adding another card to the dealers hand
                    card_index = random.randrange(len(self.deck[0]))
                    card = self.deck[0][card_index]
                    self.dealer_cards[0].append(card)
                    self.dealer_cards[1].append(self.deck[1][card_index])
                    self.deck[0].remove(card)
                    self.deck[1].remove(self.deck[1][card_index])
                    self.dealer_card_count = self.calculate_counts(self.dealer_cards)
                    print(self.dealer_card_count)
                    self.window.after(3000, lambda: self.show_cards_window(self.dealer_cards[1][2], dealer_side))
        # Checking to see who won
        if self.user_card_count > self.dealer_card_count:
            self.window.after(5000, lambda: self.update_message("User Wins"))
            self.balance += self.bet
        elif self.user_card_count < self.dealer_card_count:
            self.window.after(5000, lambda: self.update_message("Dealer Wins"))
            self.balance -= self.bet
        else:
            self.window.after(5000, lambda: self.update_message("Tie"))
        # Updating player bet and balance
        self.bet = 0
        self.window.after(5000, lambda: self.update_balance("Balance: $" + str(self.balance)))
        self.window.after(5000, lambda: self.update_bet("Bet: $" + str(self.bet)))
        self.window.after(5000, lambda: self.window.after(3000, lambda: self.reset()))

        

        

    def show_cards_window(self, image_path, side, steps=15, delay=50):
        # Load and resize the image
        pil_image = Image.open(image_path).resize((100, 145))
        enhancer = ImageEnhance.Brightness(pil_image)

        # Create a label 
        img = ImageTk.PhotoImage(enhancer.enhance(0))
        label = tk.Label(self.window, image=img, bg="green")
        label.image = img
        label.pack(side=side, padx=10, pady=10)
        self.card_labels.append(label)

        # Adding in animation for cards to fade in
        def animate(step=0):
            if step > steps:
                return
            bright_img = ImageTk.PhotoImage(enhancer.enhance(step / steps))
            label.configure(image=bright_img)
            label.image = bright_img
            self.window.after(delay, animate, step + 1)
        animate()

    def calculate_counts(self, hand):
        # Sets total equal to zero
        total = 0
        for card in hand[0]:
            rank = card[0]
            # If face card, add 0
            if rank in ['J', 'Q', 'K']:
                total = total
            # If ace, add 1
            elif rank == 'A':
                total += 1
            else:
            # Adds all other values
                total += rank
     
        return total % 10
    
    def reset(self):
        # Resetting game
        self.bet = 0
        self.deck = None
        self.user_card_count = 0
        self.dealer_card_count = 0
        # Getting rid of cards on screen
        self.clear_card_images()
        # Enabling player and banker buttons
        self.player_button.config(state="normal")
        self.banker_button.config(state="normal")

        # Updating player bet and balance
        self.update_bet("Bet: $" + str(self.bet))
        self.update_message("")

        self.window.update_idletasks()

    def clear_card_images(self):
        # Clears all card images on screen
        for label in self.card_labels:
            label.destroy()
        self.card_labels.clear()
   


d1 = baccarat()
d1.setup_window()







