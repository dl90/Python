# Don Li

# Square Pies
# We need to feed people at a party some square-shaped strawberry pies.
# Create a function called pie_calc which takes has 1 parameter, inputStr, which is a decimal string.
# This string represents the side length, L, of the square-pie in cm. The area of the pie should be 
# computed using the formula A = L*L. Then, assuming that each person needs to eat 100 cm² of pie, 
# compute the number of people it can feed, rounded down to the nearest integer. 
# Example: if inputStr is "17.5", the area will be 306.25 cm², so 3 is the correct output.

# Write your function here
import math

def pie_calc(inputStr):
    L = float(inputStr)
    A = L * L
    return math.trunc(A/100)

# print(pie_calc("17.5"))


# Square Pies - Test1
def test_square_pies_1():
    assert pie_calc("17.5") == 3

# Square Pies - Test2
def test_square_pies_2():
    assert pie_calc("14.375") == 2

# Square Pies - Test3
def test_square_pies_3():
    assert pie_calc("4.875") == 0

# Square Pies - Test4
def test_square_pies_4():
    assert pie_calc("17.75") == 3

# Write a program that reads an integer from input, representing someone's age.
# If the age is 18 or larger, print out You can vote.
# If the age is between 0 and 17 inclusive, print out Too young to vote.
# If the age is less than 0, print out You are a time traveller.

from io import StringIO
input1 = StringIO('-31\n')
input2 = StringIO('4\n')
input3 = StringIO('-1\n')
input4 = StringIO('0\n')
input5 = StringIO('18\n')

def age_checker():
    x = int(input("Enter your age:"))
    if (x >= 18): 
        return("You can vote")
    elif (x >= 0 and x <= 17): 
        return("Too young to vote")
    else: 
        return("You are a time traveller")

# age_checker - Test1
def test_age_checker_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', input1)
    assert age_checker() == "You are a time traveller"

# age_checker - Test2
def test_age_checker_2(monkeypatch):
    monkeypatch.setattr('sys.stdin', input2)
    assert age_checker() == "Too young to vote"

# age_checker - Test3
def test_age_checker_3(monkeypatch):
    monkeypatch.setattr('sys.stdin', input3)
    assert age_checker() == "You are a time traveller"

# age_checker - Test4
def test_age_checker_4(monkeypatch):
    monkeypatch.setattr('sys.stdin', input4)
    assert age_checker() == "Too young to vote"

# age_checker - Test5
def test_age_checker_5(monkeypatch):
    monkeypatch.setattr('sys.stdin', input5)
    assert age_checker() == "You can vote"


################################
# Timbits

# Full Explanation Here:
# https://cscircles.cemc.uwaterloo.ca/6d-design/

# Problem
'''
box // price
1	            $0.20
10 (small box)	$1.99
20 (medium box)	$3.39
40 (large box)	$6.19

timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

# step 3: buy as many large boxes as you can
bigBoxes = int(timbitsLeft / 40)
totalCost = totalCost + bigBoxes * 6.19    # update the total price
timbitsLeft = timbitsLeft - 40 * bigBoxes  # calculate timbits still needed

if timbitsLeft >= 20:                # step 4, can we buy a medium box?
    totalCost = totalCost + 3.39
    timbitsLeft = timbitsLeft - 20
if timbitsLeft >= 10:                # step 5, can we buy a small box?
    totalCost = totalCost + 1.99
    timbitsLeft = timbitsLeft - 20

totalCost = totalCost + timbitsLeft * 20 # step 6
print(totalCost)                         # step 7
'''

# Add your solution here:

def donuts_left():
    timbits_left = int(input("Enter the number of people: "))
    total_cost = 0

    if (timbits_left >= 40):
        big_box = math.trunc(timbits_left / 40)
        timbits_left = timbits_left - big_box * 40
        total_cost = total_cost + big_box * 6.19

    if (timbits_left >= 20):
        middle_box = math.trunc(timbits_left / 20)
        timbits_left = timbits_left - middle_box * 20
        total_cost = total_cost + middle_box * 3.39
    
    if (timbits_left >= 10):
        small_box = math.trunc(timbits_left / 10)
        timbits_left = timbits_left - small_box * 10
        total_cost = total_cost + small_box * 1.99

    if (timbits_left < 10):
        total_cost = total_cost + timbits_left * 0.2
        return total_cost



donuts_left_input1 = StringIO('10\n')
donuts_left_input2 = StringIO('20\n')
donuts_left_input3 = StringIO('40\n')
donuts_left_input4 = StringIO('1\n')
donuts_left_input5 = StringIO('0\n')
donuts_left_input6 = StringIO('39\n')
donuts_left_input7 = StringIO('41\n')
donuts_left_input8 = StringIO('4\n')
donuts_left_input9 = StringIO('45\n')
donuts_left_input10 = StringIO('456\n')
donuts_left_input11 = StringIO('92\n')

# donuts_left - Test1
def test_donuts_left_1(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input1)
    assert donuts_left() == 1.99

# donuts_left - Test2
def test_donuts_left_2(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input2)
    assert donuts_left() == 3.39

# donuts_left - Test3
def test_donuts_left_3(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input3)
    assert donuts_left() == 6.19

# donuts_left - Test4
def test_donuts_left_4(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input4)
    assert donuts_left() == 0.2

# donuts_left - Test5
def test_donuts_left_5(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input5)
    assert donuts_left() == 0.0

# donuts_left - Test6
def test_donuts_left_6(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input6)
    assert donuts_left() == 7.18

# donuts_left - Test7
def test_donuts_left_7(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input7)
    assert donuts_left() == 6.390000000000001

# donuts_left - Test8
def test_donuts_left_8(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input8)
    assert donuts_left() == 0.8

# donuts_left - Test9
def test_donuts_left_9(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input9)
    assert donuts_left() == 7.19

# donuts_left - Test10
def test_donuts_left_10(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input10)
    assert donuts_left() == 71.28

# donuts_left - Test11
def test_donuts_left_11(monkeypatch):
    monkeypatch.setattr('sys.stdin', donuts_left_input11)
    assert donuts_left() == 14.770000000000001