uber_black = 2.00
uber_van = 3.50
uber_x = 1.50

def main(choice_car, kilometers, Calculate_cost):
    choice_car = choice_car()
    kilometers = kilometers()
    print(f'Deze rit zal u {Calculate_cost(choice_car, kilometers)} Euro kosten')

def choice_car():
    Choice_car = ""
    while Choice_car not in ['1' , '2' , '3']:
        Choice_car = input(f"welke dienst zou je willen nemen? (1) Uber Black, (2) Uber Van, of (3) Uber X ")
        if Choice_car in '1':
            cost_per_km = uber_black
            break
        elif Choice_car in '2':
            cost_per_km = uber_van
            break
        elif Choice_car in '3':
            cost_per_km = uber_x
            break
        else:
            print(f'Kies 1, 2 of 3')
            continue

    return cost_per_km

def kilometers():
    hoeveel_km = int(input(f"Hoeveel km gaat de rit zijn? "))
    return hoeveel_km

def calculate_cost(cost_per_km, kilometers):
    calculate_cost = kilometers * cost_per_km
    return calculate_cost

main(choice_car, kilometers, calculate_cost)
