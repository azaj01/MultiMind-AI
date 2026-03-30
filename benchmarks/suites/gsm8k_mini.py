"""GSM8K Mini — 50 multi-step math reasoning problems.

Curated subset covering 2-step to 5-step arithmetic, fractions,
percentages, and word problems. Each has a deterministic numeric answer.

Used for Axis 1: comparing off vs medium vs hard thinking modes.
"""

from __future__ import annotations

SUITE_NAME = "gsm8k_mini"
SCORE_TYPE = "exact_numeric"

QUESTIONS: list[dict[str, str]] = [
    # --- 2-step problems (1-10) ---
    {
        "id": "gsm-01",
        "question": "A baker makes 48 cupcakes in the morning and 32 cupcakes in the afternoon. If each box holds 8 cupcakes, how many boxes does the baker need?",
        "expected": "10",
    },
    {
        "id": "gsm-02",
        "question": "Maria has 120 stickers. She gives 15 stickers to each of her 6 friends. How many stickers does Maria have left?",
        "expected": "30",
    },
    {
        "id": "gsm-03",
        "question": "A train travels at 60 miles per hour. How far does it travel in 3 hours and 30 minutes?",
        "expected": "210",
    },
    {
        "id": "gsm-04",
        "question": "Tom buys 3 notebooks at $4 each and 2 pens at $1.50 each. How much does he spend in total?",
        "expected": "15",
    },
    {
        "id": "gsm-05",
        "question": "A garden has 5 rows of flowers with 12 flowers in each row. If 8 flowers die, how many flowers are left?",
        "expected": "52",
    },
    {
        "id": "gsm-06",
        "question": "Sarah reads 25 pages per day. If a book has 175 pages, how many days will it take her to finish the book?",
        "expected": "7",
    },
    {
        "id": "gsm-07",
        "question": "A parking lot has 4 levels with 30 spaces on each level. If 78 spaces are occupied, how many spaces are available?",
        "expected": "42",
    },
    {
        "id": "gsm-08",
        "question": "Jake earns $12 per hour. He works 8 hours on Monday and 6 hours on Tuesday. How much does he earn in total?",
        "expected": "168",
    },
    {
        "id": "gsm-09",
        "question": "A recipe calls for 2 cups of flour for 24 cookies. If you want to make 60 cookies, how many cups of flour do you need?",
        "expected": "5",
    },
    {
        "id": "gsm-10",
        "question": "There are 200 students in a school. 55% of them are girls. How many boys are there?",
        "expected": "90",
    },

    # --- 3-step problems (11-25) ---
    {
        "id": "gsm-11",
        "question": "Lisa buys 4 shirts at $18 each and gets a 25% discount on the total. She also pays $5 for shipping. How much does she pay in total?",
        "expected": "59",
    },
    {
        "id": "gsm-12",
        "question": "A factory produces 250 toys per day. After a 20% increase in production, how many toys does it produce in a 5-day work week?",
        "expected": "1500",
    },
    {
        "id": "gsm-13",
        "question": "Mark has $500. He spends 30% on rent, then spends $50 on groceries. How much money does he have left?",
        "expected": "300",
    },
    {
        "id": "gsm-14",
        "question": "A pool is filled at a rate of 15 gallons per minute. If the pool holds 900 gallons and it's already 1/3 full, how many minutes will it take to fill it completely?",
        "expected": "40",
    },
    {
        "id": "gsm-15",
        "question": "Emma scores 85, 92, and 78 on three tests. She needs an average of 85 across all four tests. What score does she need on the fourth test?",
        "expected": "85",
    },
    {
        "id": "gsm-16",
        "question": "A store sells apples for $2 per pound and oranges for $3 per pound. If you buy 4 pounds of apples and 3 pounds of oranges, and have a $5 coupon, how much do you pay?",
        "expected": "12",
    },
    {
        "id": "gsm-17",
        "question": "A car travels 180 miles using 6 gallons of gas. If gas costs $3.50 per gallon, how much does it cost to drive 300 miles?",
        "expected": "35",
    },
    {
        "id": "gsm-18",
        "question": "There are 36 students in a class. 1/4 are absent. Of those present, 2/3 brought their textbooks. How many students brought their textbooks?",
        "expected": "18",
    },
    {
        "id": "gsm-19",
        "question": "A restaurant serves 120 customers on Friday and 80% more on Saturday. On Sunday, they serve half of Saturday's count. How many total customers did they serve over the three days?",
        "expected": "444",
    },
    {
        "id": "gsm-20",
        "question": "A phone plan costs $45 per month plus $0.10 per text message. If John sends 250 texts in January, what is his bill for that month?",
        "expected": "70",
    },
    {
        "id": "gsm-21",
        "question": "Helen bakes 3 batches of cookies with 24 cookies each. She decorates 1/4 of them with sprinkles and 1/3 of the remainder with chocolate chips. How many cookies have no decoration?",
        "expected": "36",
    },
    {
        "id": "gsm-22",
        "question": "A farmer harvests 840 kg of wheat. He keeps 15% for seeds, sells 60% of the remainder, and donates the rest. How many kg does he donate?",
        "expected": "285.6",
    },
    {
        "id": "gsm-23",
        "question": "Two cyclists start from the same point. One rides north at 12 mph and the other rides south at 8 mph. After 2.5 hours, how far apart are they?",
        "expected": "50",
    },
    {
        "id": "gsm-24",
        "question": "A company has 150 employees. They hire 20% more in Q1, then 10 employees leave in Q2. How many employees does the company have after Q2?",
        "expected": "170",
    },
    {
        "id": "gsm-25",
        "question": "A rectangle's length is 3 times its width. If the perimeter is 64 cm, what is the area of the rectangle?",
        "expected": "192",
    },

    # --- 4-step problems (26-40) ---
    {
        "id": "gsm-26",
        "question": "A store has a 'buy 2 get 1 free' deal on shirts costing $25 each. If Mike buys 7 shirts, how much does he pay after a 10% loyalty discount on the total?",
        "expected": "112.5",
    },
    {
        "id": "gsm-27",
        "question": "A water tank has 1000 liters. On day 1, 20% is used. On day 2, 25% of the remaining water is used. On day 3, 100 liters are added. How many liters are in the tank after day 3?",
        "expected": "700",
    },
    {
        "id": "gsm-28",
        "question": "Sam earns $15/hour for the first 40 hours and $22.50/hour for overtime. If he works 52 hours in a week and pays 20% in taxes, how much is his take-home pay?",
        "expected": "696",
    },
    {
        "id": "gsm-29",
        "question": "A school orders 500 pencils at $0.30 each and 200 erasers at $0.50 each. They get a 15% bulk discount on the total order. Shipping is $12. What is the final cost?",
        "expected": "224.5",
    },
    {
        "id": "gsm-30",
        "question": "In a class of 40 students, 60% pass the math test, 75% pass the English test, and 50% pass both. How many students failed both tests?",
        "expected": "6",
    },
    {
        "id": "gsm-31",
        "question": "A tree grows 2 feet per year. It is currently 10 feet tall and was planted 3 years ago. After 5 more years, it will be cut to half its height. How tall will it be after cutting?",
        "expected": "10",
    },
    {
        "id": "gsm-32",
        "question": "A baker uses 3 eggs per cake and 2 eggs per batch of muffins. She has 50 eggs. If she makes 8 cakes first, how many batches of muffins can she make with the remaining eggs?",
        "expected": "13",
    },
    {
        "id": "gsm-33",
        "question": "A shop sells T-shirts for $20 and jeans for $45. During a sale, T-shirts get 30% off and jeans get 20% off. If someone buys 3 T-shirts and 2 pairs of jeans, how much do they save compared to the original prices?",
        "expected": "36",
    },
    {
        "id": "gsm-34",
        "question": "A library has 5000 books. 40% are fiction, 35% are non-fiction, and the rest are reference books. If they donate 10% of each category, how many books remain in total?",
        "expected": "4500",
    },
    {
        "id": "gsm-35",
        "question": "A jogger runs 3 laps around a 400m track, rests for 5 minutes, then runs 2 more laps. Her first 3 laps took 8 minutes and last 2 laps took 6 minutes. What was her average speed in meters per minute for the running time only?",
        "expected": "142.86",
    },
    {
        "id": "gsm-36",
        "question": "A company's revenue was $80,000 in January. It grew by 10% in February, dropped by 5% in March, and grew by 15% in April. What was the revenue in April (rounded to the nearest dollar)?",
        "expected": "96140",
    },
    {
        "id": "gsm-37",
        "question": "Three friends split a dinner bill. The food costs $84, tax is 8%, and they leave a 20% tip on the pre-tax amount. If they split everything equally, how much does each person pay?",
        "expected": "35.84",
    },
    {
        "id": "gsm-38",
        "question": "A farmer plants corn in a field that is 120m long and 80m wide. Each plant needs 0.5 square meters. If 5% of the seeds fail to grow, how many corn plants actually grow?",
        "expected": "18240",
    },
    {
        "id": "gsm-39",
        "question": "A tank is 3/4 full with 450 liters of water. Water drains at 5 liters per minute and fills at 3 liters per minute simultaneously. How long (in minutes) until the tank is half full?",
        "expected": "75",
    },
    {
        "id": "gsm-40",
        "question": "A store marks up items by 50% from cost, then offers a 20% sale. If the sale price of a jacket is $60, what was the original cost to the store?",
        "expected": "50",
    },

    # --- 5-step problems (41-50) ---
    {
        "id": "gsm-41",
        "question": "A school has 600 students. 1/3 join the science club, 1/4 of the science club also join the math club, and 50% of those in both clubs go on a field trip. If each field trip ticket costs $15, what is the total ticket cost?",
        "expected": "375",
    },
    {
        "id": "gsm-42",
        "question": "Emily invests $2000 at 5% annual simple interest. After 3 years, she withdraws half the total amount (principal + interest). She reinvests the remaining amount for 2 more years at 4% simple interest. How much does she have at the end of 5 years?",
        "expected": "1262",
    },
    {
        "id": "gsm-43",
        "question": "A pizzeria sells small pizzas for $8, medium for $12, and large for $16. On Monday they sell 20 small, 30 medium, and 15 large. Tuesday's sales are 50% higher across all sizes. What is the combined revenue for both days?",
        "expected": "1710",
    },
    {
        "id": "gsm-44",
        "question": "A warehouse has 3 sections. Section A has 400 items, Section B has 250 items, and Section C has 350 items. 10% of A, 20% of B, and 15% of C are defective. Defective items are returned at $2 each. Good items are sold at $8 each. What is the total revenue minus returns?",
        "expected": "6750",
    },
    {
        "id": "gsm-45",
        "question": "A car rental costs $40/day plus $0.25/mile. Insurance is $15/day. If you rent for 5 days and drive 800 miles, then get a 10% loyalty discount on the entire bill, how much do you pay?",
        "expected": "427.5",
    },
    {
        "id": "gsm-46",
        "question": "A charity walk has 200 participants. Each person walks 5 km. Sponsors pledge $3 per km for the first 50 walkers, $2 per km for the next 100, and $1.50 per km for the rest. What is the total amount pledged?",
        "expected": "2125",
    },
    {
        "id": "gsm-47",
        "question": "A company buys 1000 widgets at $5 each. They pay 8% import tax. Shipping costs $500. They sell each widget for $12 but give a 10% discount on orders over 100 widgets. If they sell 800 widgets (all in one order), what is their profit?",
        "expected": "3140",
    },
    {
        "id": "gsm-48",
        "question": "A cyclist rides uphill at 10 km/h for 2 hours, then downhill at 30 km/h for 1 hour. She rests for 30 minutes, then rides on flat ground at 20 km/h for 1.5 hours. What is her average speed (in km/h) for the entire journey including rest time?",
        "expected": "16",
    },
    {
        "id": "gsm-49",
        "question": "A bookstore has 3 shelves. Shelf 1 has 45 books priced at $10, Shelf 2 has 30 books at $15, and Shelf 3 has 25 books at $20. During a sale, Shelf 1 gets 20% off, Shelf 2 gets 30% off, and Shelf 3 gets no discount. If all books sell, what is the total revenue?",
        "expected": "1175",
    },
    {
        "id": "gsm-50",
        "question": "A family's monthly income is $6000. They spend 30% on rent, 15% on food, 10% on transport, and 5% on utilities. Of the remaining amount, they save 60% and spend the rest on entertainment. How much do they spend on entertainment per month?",
        "expected": "960",
    },
]
