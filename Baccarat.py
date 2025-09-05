import tkinter as tk
from PIL import Image, ImageTk 
import random
from PIL import ImageEnhance

class baccarat:
    def __init__(self):
        # Making initial variables
        self.window = None
        # Makes starting balance $2500
        self.balance = 2500
        self.bet = 0
        self.deck = None
        self.card_labels = []
        # Dealer and user card count totals
        self.user_card_count = 0
        self.dealer_card_count = 0
        # Counts how many cards have been flipped
        self.cards_flipped = 0
        # Number of flips needed before deciding a winner
        self.max_flips = 4
        # Which side the cards go on
        self.user_side = None
        self.dealer_side = None
        # Tracks user and dealer third cards
        self.user_third_card = None
        self.dealer_third_card = None
        self.user_third_flipped = False

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
        self.red_chip_button = tk.Button(chip_frame, text="$5", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.red_chip)
        self.red_chip_button.image = photo
        self.red_chip_button.pack(side="left", padx=10)

        # Adds green chip image
        image = Image.open(casino_chip_images[1])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds green chip button
        self.green_chip_button = tk.Button(chip_frame, text="$25", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black",command=self.green_chip)
        self.green_chip_button.image = photo
        self.green_chip_button.pack(side="left", padx=10)

        # Adds blue chip image
        image = Image.open(casino_chip_images[2])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds blue chip button
        self.blue_chip_button = tk.Button(chip_frame, text="$100", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.blue_chip)
        self.blue_chip_button.image = photo
        self.blue_chip_button.pack(side="left", padx=10)

        # Adds yellow chip image
        image = Image.open(casino_chip_images[3])
        image = image.resize((100, 100)) 
        photo = ImageTk.PhotoImage(image)
        # Adds yellow chip button
        self.yellow_chip_button = tk.Button(chip_frame, text="$250", font=('Times New Roman', 30), compound="center", image=photo, bg="green", borderwidth=0, fg="black", command=self.yellow_chip)
        self.yellow_chip_button.image = photo
        self.yellow_chip_button.pack(side="left", padx=10)

        # Adds clear bet option button
        self.clear_bet_button = tk.Button(chip_frame, text="Clear Bet", font=('Times New Roman', 20), bg="grey", fg="black", command = self.clear_bet)
        self.clear_bet_button.pack(side="left", padx=10)
    
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
        # Disabling betting buttons
        self.red_chip_button.config(state="disabled")
        self.green_chip_button.config(state="disabled")
        self.blue_chip_button.config(state="disabled")
        self.yellow_chip_button.config(state="disabled")
        self.clear_bet_button.config(state="disabled")
        # Making sure the third card variables are correct
        self.cards_flipped = 0
        self.max_flips = 4 
        self.thirds_checked = False
        self.third_cards_pending = False
        self.user_third_flipped = False
        # Making sure the cards appear on the correct side
        self.user_side, self.dealer_side = ('left','right') if user_card_side==1 else ('right','left')
        # Makes a new deck
        self.make_deck()
        # Defining both user and dealer hands
        self.user_cards = [[],[]]
        self.dealer_cards = [[],[]]

        # Adding cards to both player and dealer hand
        for i in range(2):
            idx = random.randrange(len(self.deck[0]))
            card = self.deck[0][idx]
            self.user_cards[0].append(card)
            self.user_cards[1].append(self.deck[1][idx])
            self.deck[0].remove(card)
            self.deck[1].remove(self.deck[1][idx])

        for i in range(2):
            idx = random.randrange(len(self.deck[0]))
            card = self.deck[0][idx]
            self.dealer_cards[0].append(card)
            self.dealer_cards[1].append(self.deck[1][idx])
            self.deck[0].remove(card)
            self.deck[1].remove(self.deck[1][idx])

        # Showing both player and dealer cards when flipped
        for front_image in self.user_cards[1]:
            self.show_card(front_image, self.user_side, initial=True)
        for front_image in self.dealer_cards[1]:
            self.show_card(front_image, self.dealer_side, initial=True)
        

    def show_card(self, front_image_path, side, steps=15, delay=50, initial=False, is_third_card=False):
        # Making image path for back of card
        back_image_path = r"C:\Users\matth\Desktop\PNG-cards-1.3\card back black.png"
        pil_back = Image.open(back_image_path).resize((100, 145))
        back_img = ImageTk.PhotoImage(pil_back)
        # Resizing and enhancing back of card image
        pil_front = Image.open(front_image_path).resize((100, 145))
        enhancer = ImageEnhance.Brightness(pil_front)
        # Making label for each back of card image
        label = tk.Label(self.window, image=back_img, bg="green")
        label.image = back_img
        label.pack(side=side, padx=10, pady=10)
        self.card_labels.append(label)
        
        # Method to flip cards
        def flip(event, step=0):
            if step > steps:
                # Keeps track of how many cards have been flipped
                self.cards_flipped += 1
                
                # Checks to see if user has flipped their third card
                if is_third_card and side == self.user_side:
                    self.user_third_flipped = True
                    # If dealer has a third card waiting, show it now
                    if hasattr(self, 'dealer_third_card') and self.dealer_third_card:
                        self.show_card(self.dealer_third_card, self.dealer_side, is_third_card=True)
                        self.dealer_third_card = None
                
                # Checks to see if all cards have been flipped
                if self.cards_flipped == self.max_flips:
                    # Checks if third card is needed 
                    if not hasattr(self, "thirds_checked") or not self.thirds_checked:
                        # Makes sure only one more card can be given to either the user or dealer
                        self.thirds_checked = True  

                        user_total = self.calculate_counts(self.user_cards)
                        dealer_total = self.calculate_counts(self.dealer_cards)

                        # Checks if the user or dealer get a natural 8 or 9
                        if user_total in (8, 9) or dealer_total in (8, 9):
                            self.determine_winner()
                            return

                        extra_flips = 0

                        # Checks if user needs a third card
                        if user_total <= 5 and len(self.user_cards[0]) == 2:
                            idx = random.randrange(len(self.deck[0]))
                            card = self.deck[0][idx]
                            self.user_cards[0].append(card)
                            self.user_cards[1].append(self.deck[1][idx])
                            self.deck[0].remove(card)
                            self.deck[1].remove(self.deck[1][idx])
                            self.show_card(self.user_cards[1][-1], self.user_side, is_third_card=True)
                            extra_flips += 1

                            # Updates the users total count
                            user_total = self.calculate_counts(self.user_cards)

                        # Checks if banker needs a third card
                        dealer_draw = False
                        # If user did not draw a third card
                        if len(self.user_cards[0]) == 2:  
                            if dealer_total <= 5:
                                dealer_draw = True
                        # If user did draw a third card
                        else:  
                            user_third = self.user_cards[0][2]
                            pt_val = 0 if user_third[0] in ['J','Q','K'] else 1 if user_third[0] == 'A' else user_third[0]
                            if dealer_total <= 2: dealer_draw = True
                            elif dealer_total == 3 and pt_val != 8: dealer_draw = True
                            elif dealer_total == 4 and pt_val in [2,3,4,5,6,7]: dealer_draw = True
                            elif dealer_total == 5 and pt_val in [4,5,6,7]: dealer_draw = True
                            elif dealer_total == 6 and pt_val in [6,7]: dealer_draw = True

                        if dealer_draw and len(self.dealer_cards[0]) == 2:
                            idx = random.randrange(len(self.deck[0]))
                            card = self.deck[0][idx]
                            self.dealer_cards[0].append(card)
                            self.dealer_cards[1].append(self.deck[1][idx])
                            self.deck[0].remove(card)
                            self.deck[1].remove(self.deck[1][idx])
                            
                            # Store dealer third card but don't show it yet
                            self.dealer_third_card = self.dealer_cards[1][-1]
                            extra_flips += 1
                            
                        # Updates the total number of flips needed to end the game
                        if extra_flips > 0:
                            self.max_flips += extra_flips
                        else:
                            # If no third card is drawn, end the game
                            self.determine_winner()
                    else:
                        # If third cards have been drawn, end the game
                        self.determine_winner()

                return

            # flipping card animation
            bright_img = ImageTk.PhotoImage(enhancer.enhance(step / steps))
            label.configure(image=bright_img)
            label.image = bright_img
            self.window.after(delay, flip, event, step + 1)

        label.bind("<Button-1>", flip)


    def determine_winner(self):
        # adds up user and dealer counts
        self.user_card_count = self.calculate_counts(self.user_cards)
        self.dealer_card_count = self.calculate_counts(self.dealer_cards)
        # Checking to see who wins
        if self.user_card_count > self.dealer_card_count:
            self.update_message("User Wins")
            self.balance += self.bet
        elif self.user_card_count < self.dealer_card_count:
            self.update_message("Dealer Wins")
            self.balance -= self.bet
        else:
            self.update_message("Tie")
        # Resetting player bet and balance
        self.bet = 0
        self.update_balance("Balance: $" + str(self.balance))
        self.update_bet("Bet: $" + str(self.bet))

        # Resetting game after 3 seconds
        self.window.after(3000, self.reset)


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
        # Enabling betting buttons
        self.red_chip_button.config(state="normal")
        self.green_chip_button.config(state="normal")
        self.blue_chip_button.config(state="normal")
        self.yellow_chip_button.config(state="normal")
        self.clear_bet_button.config(state="normal")
        # Updating player bet and balance
        self.update_bet("Bet: $" + str(self.bet))
        self.update_message("")

        # Reset flip logic
        self.cards_flipped = 0
        self.max_flips = 4
        self.thirds_checked = False
        self.third_cards_pending = False
        self.user_third_flipped = False
        self.dealer_third_card = None

        self.window.update_idletasks()

    def clear_card_images(self):
        # Clears all card images on screen
        for label in self.card_labels:
            label.destroy()
        self.card_labels.clear()
   


d1 = baccarat()

d1.setup_window()






