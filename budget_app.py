# Define categories
CATEGORIES = ['Gas', 'Food', 'Entertainment', 'Clothing', 'Bills']

# Initialize totals
totals = {category: 0 for category in CATEGORIES}
total_spent = 0

# Function to add a purchase
def add_purchase():
    global total_spent
    cost = float(input('Enter the cost of the item: '))
    print('Select a category for this item:')
    for i, category in enumerate(CATEGORIES):
        print(f'{i+1}. {category}')
    category_choice = int(input('Enter the number of the category: ')) - 1
    category = CATEGORIES[category_choice]
    totals[category] += cost
    total_spent += cost

# Main loop
while True:
    add_purchase()
    continue_choice = input('Would you like to add another item? (yes/no): ')
    if continue_choice.lower() not in ['yes', 'y']:
        break

# Calculate percentages and print totals
print('\nTotal spent: $' + str(total_spent))
for category, total in totals.items():
    percentage = (total / total_spent) * 100 if total_spent > 0 else 0
    print(f'{category}: ${total} ({percentage:.2f}%)')
