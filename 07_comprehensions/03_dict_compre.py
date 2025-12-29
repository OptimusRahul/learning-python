tea_prices_inr = {
    "Masala Chai": 10,
    "Iced Lemon Tea": 15,
    "Green Tea": 12,
    "Iced Peach Tea": 18,
    "Ginger Chai": 14,
}

tea_price_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}
print(tea_price_usd)