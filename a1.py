

def show_menu():
    '''
	Description: Prints the menu as shown in the PDF

	Parameters: No parameters

	Returns: No return value
	'''
    print('=' * 49, '\n', ' ' * 15, 'MY  BAZAAR' + '\n' + '=' * 49, '\n' + 'Hello! Welcome to my grocery store!')
    print('Following are the products available in the shop:')
    print('\n' + '-' * 49, '\n' + 'CODE | DESCRIPTION |   CATEGORY   | COST (Rs)', '\n' + '-' * 49, '\n ',
          '0  | Tshirt      | Apparels     | 500')
    print('  1  | Trousers    | Apparels     | 600', '\n', ' 2  | Scarf       | Apparels     | 250')
    print('  3  | Smartphone  | Electronics  | 20,000', '\n ', '4  | iPad        | Electronics  | 30,000')
    print('  5  | Laptop      | Electronics  | 50,000', '\n ', '6  | Eggs        | Eatables     | 5')
    print('  7  | Chocolate   | Eatables     | 10', '\n ', '8  | Juice       | Eatables     | 100')
    print('  9  | Milk        | Eatables     | 45')
    print('-' * 49)


def get_regular_input():
    '''
	Description: Takes space separated item codes (only integers allowed).
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: No parameters

	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
    print('\n' + '-' * 49, '\n' + 'ENTER ITEMS YOU WISH TO BUY', '\n' + '-' * 49)
    global lp
    tsht = 0
    trsr = 0
    scf = 0
    smtph = 0
    ipd = 0
    lptp = 0
    egg = 0
    chc = 0
    jce = 0
    mlk = 0

    itmcod = input('Enter the item codes (space-separated):')
    itmcod = itmcod.split(" ")
    i = 0
    while i < len(itmcod):

        if itmcod[i] == '0':
            tsht = tsht + 1
        if itmcod[i] == '1':
            trsr = trsr + 1
        if itmcod[i] == '2':
            scf = scf + 1
        if itmcod[i] == '3':
            smtph = smtph + 1
        if itmcod[i] == '4':
            ipd = ipd + 1
        if itmcod[i] == '5':
            lptp += 1
        if itmcod[i] == '6':
            egg += 1
        if itmcod[i] == '7':
            chc += 1
        if itmcod[i] == '8':
            jce += 1
        if itmcod[i] == '9':
            mlk += 1
        i += 1
        lp += 1
    get_regular_input.itmqty = [tsht, trsr, scf, smtph, ipd, lptp, egg, chc, jce, mlk]
    return get_regular_input.itmqty


def get_bulk_input():
    '''
	Description: Takes inputs (only integers allowed) from a bulk buyer.
	For details, refer PDF. Include appropriate print statements to match
	the output with the screenshot provided in the PDF.

	Parameters: No parameters

	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
    print('\n' + '-' * 49, '\n' + 'ENTER ITEM AND QUANTITIES', '\n' + '-' * 49)
    global lp
    tsht = 0
    trsr = 0
    scf = 0
    smtph = 0
    ipd = 0
    lptp = 0
    egg = 0
    chc = 0
    jce = 0
    mlk = 0
    while True:
        x1 = input('Enter code and quantity (leave blank to stop):')
        x1 = x1.split(' ')
        x1.append('')

        if x1[0] == '' or x1[1] == '':
            print('Your order has finalized')
            break

        else:

            itm = x1[0]
            qty = x1[1]
            if itm not in '0123456789' and int(qty) <= 0:
                print('Invalid code and quantity. Try again.')
            elif int(qty) <= 0:
                print('Invalid quantity.Try again.')
            elif itm not in '0123456789':
                print('Invalid code. Try again.')
            else:
                if itm == '0':
                    print('you added', int(qty), 'Tshirts')
                    tsht = tsht + int(qty)
                if itm == '1':
                    print('you added', int(qty), 'Trousers')
                    trsr = trsr + int(qty)
                if itm == '2':
                    print('you added', int(qty), 'Scarfs')
                    scf = scf + int(qty)
                if itm == '3':
                    print('you added', int(qty), 'smartphone')
                    smtph = smtph + int(qty)
                if itm == '4':
                    print('you added', int(qty), 'iPads')
                    ipd = ipd + int(qty)
                if itm == '5':
                    print('you added', int(qty), 'Laptops')
                    lptp += int(qty)
                if itm == '6':
                    print('you added', int(qty), 'Eggs')
                    egg += int(qty)
                if itm == '7':
                    print('you added', int(qty), 'Chocolates')
                    chc += int(qty)
                if itm == '8':
                    print('you added', int(qty), 'Juice')
                    jce += int(qty)
                if itm == '9':
                    print('you added', int(qty), 'Milk')
                    mlk += int(qty)
            lp += 1

    get_bulk_input.itmqty = [tsht, trsr, scf, smtph, ipd, lptp, egg, chc, jce, mlk]
    return get_bulk_input.itmqty


def print_order_details(quantities):
    '''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.

	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.

	Returns: No return value
	'''
    global lp
    print('\n' + '-' * 49, '\n' + 'ORDER DETAILS', '\n' + '-' * 49)
    mts = ['Tshirt', 'Trousers', 'Scarf', 'Smartphone', 'iPad', 'Laptop', 'Eggs', 'Chocolate', 'Juice', 'Milk']
    newmts = []
    qtys = quantities

    if qtys[0] != 0:
        newmts.append(mts[0])
    if qtys[1] != 0:
        newmts.append(mts[1])
    if qtys[2] != 0:
        newmts.append(mts[2])
    if qtys[3] != 0:
        newmts.append(mts[3])
    if qtys[4] != 0:
        newmts.append(mts[4])
    if qtys[5] != 0:
        newmts.append(mts[5])
    if qtys[6] != 0:
        newmts.append(mts[6])
    if qtys[7] != 0:
        newmts.append(mts[7])
    if qtys[8] != 0:
        newmts.append(mts[8])
    if qtys[9] != 0:
        newmts.append(mts[9])
    for h in range(int(lp)):
        newmts.append(" ")
    s = 0
    while s < int(lp):
        if newmts[s] == 'Tshirt':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[0], '=', '500*', qtys[0], '=', 500 * qtys[0])
        if newmts[s] == 'Trousers':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[1], '=', '600*', qtys[1], '=', 600 * qtys[1])
        if newmts[s] == 'Scarf':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[2], '=', '250*', qtys[2], '=', 250 * qtys[2])
        if newmts[s] == 'Smartphone':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[3], '=', '20000*', qtys[3], '=', 20000 * qtys[3])
        if newmts[s] == 'iPad':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[4], '=', '30000*', qtys[4], '=', 30000 * qtys[4])
        if newmts[s] == 'Laptop':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[5], '=', '50000*', qtys[5], '=', 50000 * qtys[5])
        if newmts[s] == 'Eggs':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[6], '=', '5*', qtys[6], '=', 5 * qtys[6])
        if newmts[s] == 'Chocolate':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[7], '=', '10*', qtys[7], '=', 10 * qtys[7])
        if newmts[s] == 'Juice':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[8], '=', '100*', qtys[8], '=', 100 * qtys[8])
        if newmts[s] == 'Milk':
            print('[' + str(s + 1) + ']', newmts[s], '*', qtys[9], '=', '45*', qtys[9], '=', 45 * qtys[9])
        s += 1


def calculate_category_wise_cost(quantities):
    '''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.

	Returns: A 3-tuple of integers in the following format:
	(apparels_cost, electronics_cost, eatables_cost)
	'''

    print('\n' + '-' * 49, '\n' + 'CATEGORY WISE COST', '\n' + '-' * 49)
    a1 = quantities
    appl = a1[0] * 500 + a1[1] * 600 + a1[2] * 250
    elns = a1[3] * 20000 + a1[4] * 30000 + a1[5] * 50000
    etbs = a1[6] * 5 + a1[7] * 10 + a1[8] * 100 + a1[9] * 45

    print('Apparels', '=', appl)
    print('Electronics', '=', elns)
    print('Eatabels', '=', etbs)
    calculate_category_wise_cost.catcost = (appl, elns, etbs)
    return calculate_category_wise_cost.catcost


def get_discount(cost, discount_rate):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS.
	This function must be used whenever you are calculating discounts.

	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''

    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the discounted category-wise price, if applicable.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'

	Returns: A 3-tuple of integers in the following format:
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
	'''
    print('\n' + '-' * 49, '\n' + 'DISCOUNTS', '\n' + '-' * 49)
    dsct1 = 0
    dsct2 = 0
    dsct3 = 0
    discounted_apparels_cost = apparels_cost
    discounted_electronics_cost = electronics_cost
    discounted_eatables_cost = eatables_cost
    if apparels_cost >= 2000:
        dsct1 = get_discount(apparels_cost, 0.1)
        discounted_apparels_cost = apparels_cost - dsct1
        print('[APPAREL]', 'Rs', apparels_cost, '-', dsct1, '= Rs', apparels_cost - dsct1)
    if electronics_cost >= 25000:
        dsct2 = get_discount(electronics_cost, 0.1)
        discounted_electronics_cost = electronics_cost - dsct2
        print('[ELECTRONICS]', 'Rs', electronics_cost, '-', dsct2, '= Rs', electronics_cost - dsct2)
    if eatables_cost >= 500:
        dsct3 = get_discount(eatables_cost, 0.1)
        discounted_eatables_cost = eatables_cost - dsct3
        print('[EATABLES]', 'Rs', eatables_cost, '-', dsct3, '= Rs', eatables_cost - dsct3)
    print('TOTAL DISCOUNT =', dsct3 + dsct1 + dsct2)
    print('TOTAL COST =', discounted_apparels_cost + discounted_electronics_cost + discounted_eatables_cost)
    calculate_discounted_prices.dic_cost = (
    discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)
    return calculate_discounted_prices.dic_cost


def get_tax(cost, tax):
    '''
	Description: This is a helper function. DO NOT CHANGE THIS.
	This function must be used whenever you are calculating discounts.

	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.

	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'

	Returns: A 2-tuple of integers in the following format:
	(total_cost_including_tax, total_tax)
	'''
    print('\n' + '-' * 49, '\n' + 'TAX', '\n' + '-' * 49)
    acwt = apparels_cost + get_tax(apparels_cost, 0.1)
    ecwt = electronics_cost + get_tax(electronics_cost, 0.15)
    etcwt = eatables_cost + get_tax(eatables_cost, 0.05)
    print('[APPAREL]', 'Rs', apparels_cost, '*', '0.10 =', get_tax(apparels_cost, 0.10))
    print('[ELECTRONICS]', 'Rs', electronics_cost, '*', '0.15 =', get_tax(electronics_cost, 0.15))
    print('[EATABLES]', 'Rs', eatables_cost, '*', '0.05 =', get_tax(eatables_cost, 0.05))
    calculate_tax.total_cost_including_tax = acwt + ecwt + etcwt
    calculate_tax.total_tax = get_tax(apparels_cost, 0.10) + get_tax(electronics_cost, 0.15) + get_tax(eatables_cost,
                                                                                                       0.05)
    calculate_tax.tup0 = (calculate_tax.total_cost_including_tax, calculate_tax.total_tax)
    print('TOTAL TAX = Rs', calculate_tax.total_tax)
    print('TOTAL COST = Rs', calculate_tax.total_cost_including_tax)

    return calculate_tax.tup0


def get_coupon_code(cost1):
	'''
	Description: Calculates the coupon discount on the desired inputted cost
	Parameters: take one integer parameter cost1, where cost1 is the total cost after applying taxes on it
	Returns: Returns the coupon discount on the desired cost(if available)
	Note:this is a helper function.
	'''
	if cost1 >= 25000 and cost1<50000:
		dst = 0.25 * cost1
		dst = min(dst, 5000)
	else:
		dst = 0.5 * cost1
		dst = min(dst, 10000)
	return dst


def apply_coupon_code(total_cost):
    '''
	Description: Takes the coupon code from the user as input (case-sensitive).
	For details, refer the PDF. Include appropriate print statements to match
	the output with the screenshot provided in the PDF.

	Parameters: The total cost (integer) on which the coupon is to be applied.

	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
    print('\n' + '-' * 49, '\n' + 'COUPON CODE', '\n' + '-' * 49)

    def abc(total_cost):
        cpcd = input('Enter coupon code (else leave blank):')
        abc.total_coupon_discount = 0
        abc.total_cost_after_coupon_discount = total_cost
        if cpcd == 'HELLE25':
            if total_cost >= 25000:
                abc.total_coupon_discount = get_coupon_code(total_cost)
                abc.total_cost_after_coupon_discount = total_cost - abc.total_coupon_discount
                print('[HELLE25]', 'min(5000,Rs', total_cost, '* 0.25)', '= Rs', abc.total_coupon_discount)
                print('\nTOTAL COUPON DISCOUNT = Rs', abc.total_coupon_discount)
                print('TOTAL COST = Rs', abc.total_cost_after_coupon_discount)
            else:
                print(
                    'Coupon code failed,the minimum amount for availing this coupon is 25000, please enter the coupon code again')
                abc(total_cost)
        elif cpcd == 'CHILL50':
            if total_cost >= 50000:
                abc.total_coupon_discount = get_coupon_code(total_cost)
                abc.total_cost_after_coupon_discount = total_cost - abc.total_coupon_discount
                print('[CHILL50]', 'min(10000,Rs', total_cost, '* 0.50)', '= Rs', abc.total_coupon_discount)
                print('\nTOTAL COUPON DISCOUNT = Rs', abc.total_coupon_discount)
                print('TOTAL COST = Rs', abc.total_cost_after_coupon_discount)
            else:
                print(
                    'Coupon code failed,the minimum amount for availing this coupon is 50000, please enter the coupon code again')
                abc(total_cost)
        elif cpcd == '':
            print('\nNo coupon code applied.')
            print('\nTOTAL COUPON DISCOUNT = Rs', abc.total_coupon_discount)
            print('TOTAL COST = Rs', abc.total_cost_after_coupon_discount)
        else:
            print('Invalid coupon code. Try again')
            abc(total_cost)
        return 0

    abc(total_cost)
    tup2 = (abc.total_cost_after_coupon_discount, abc.total_coupon_discount)
    return tup2


def main():
    '''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate
	print statements to match the output with the screenshots provided in the PDF.

	Parameters: No parameters

	Returns: No return value
	'''
    show_menu()

    while True:
        ans1 = input('\nWould you like to buy in bulk? (y or Y / n or N): ')
        if ans1 == 'y' or ans1 == 'Y':
            get_bulk_input()
            print_order_details(get_bulk_input.itmqty)
            calculate_category_wise_cost(get_bulk_input.itmqty)
            break
        elif ans1 == 'n' or ans1 == 'N':
            get_regular_input()
            print_order_details(get_regular_input.itmqty)
            calculate_category_wise_cost(get_regular_input.itmqty)

            break
    calculate_discounted_prices(calculate_category_wise_cost.catcost[0], calculate_category_wise_cost.catcost[1],
                                calculate_category_wise_cost.catcost[2])
    calculate_tax(calculate_discounted_prices.dic_cost[0], calculate_discounted_prices.dic_cost[1],
                  calculate_discounted_prices.dic_cost[2])
    apply_coupon_code(calculate_tax.tup0[0])
    print('\nThank you for visiting!')


lp = 0

if __name__ == '__main__':
    main()















