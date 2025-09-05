from pyscript import display

restaurant_name = 'Euro Restaurant'  # String
owner_name = 'James Mamauag'  # String
year_established = 'Since 2025'  # String
product_names = ['Chicken Parm with Ravioli', 'Ratatouille', 'Fish and Chips', 'Macaroons', 'Panna Cotta']  # List
menu_prices = {
    'Chicken Parm with Ravioli': '234 pesos',
    'Ratatouille':'310 pesos',
    'Fish and Chips':'256 pesos','Macaroons':'300 pesos',
    'Panna Cotta':'215 pesos'
}  # Dictionary

display(restaurant_name, target="name")

display(f'Owned by: {owner_name}', target='title')

display(year_established, target='title')

display(product_names[0], target="product1")
display(menu_prices['Chicken Parm with Ravioli'], target="price1")

display(product_names[1], target="product2")
display(menu_prices['Ratatouille'], target="price2")

display(product_names[2], target="product3")
display(menu_prices['Fish and Chips'], target="price3")

display(product_names[3], target="product4")
display(menu_prices['Macaroons'], target="price4")

display(product_names[4], target="product5")
display(menu_prices['Panna Cotta'], target="price5")

# Reference: Codes from w3schools.com
# For context: I named my restaurant "Euro Restaurant" is because I want to make a menu that has European cuisine in general like Italian, French, Greece, etc.