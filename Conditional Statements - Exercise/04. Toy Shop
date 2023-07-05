excursion_price = float(input())

number_of_puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

PUZZLE_PRICE = 2.60
TALKING_DOL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

total_toys = number_of_puzzles + talking_dolls + teddy_bears + minions + trucks

price_for_toys = (number_of_puzzles * PUZZLE_PRICE) + \
                 (talking_dolls * TALKING_DOL_PRICE) + \
                 (teddy_bears * TEDDY_BEAR_PRICE) + \
                 (minions * MINION_PRICE) + \
                 (trucks * TRUCK_PRICE)

if total_toys >= 50:  # discount
    price_for_toys *= 0.75

price_for_toys *= 0.90

if price_for_toys >= excursion_price:
    print(f"Yes! {price_for_toys - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - price_for_toys:.2f} lv needed.")
