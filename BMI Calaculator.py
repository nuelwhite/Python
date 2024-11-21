''' This Script is a Python script to calculate the Body Mass INdex of a person.
BMI is a measurement of a person's leanness or corpulence based on their height and weight, and is intended to quantify tissue mass. It is widely used as a general indicator of whether a person has a healthy body weight for their height. Specifically, the value obtained from the calculation of BMI is used to categorize whether a person is underweight, normal weight, overweight, or obese depending on what range the value falls between. These ranges of BMI vary based on factors such as region and age, and are sometimes further divided into subcategories such as severely underweight or very severely obese. Being overweight or underweight can have significant health effects, so while BMI is an imperfect measure of healthy body weight, it is a useful indicator of whether any additional testing or action is required.

This is the World Health Organization's (WHO) recommended body weight based on BMI values for adults. It is used for both men and women, age 20 or older.

Classification	BMI range - kg/m2
Severe Thinness	< 16
Moderate Thinness	16 - 17
Mild Thinness	17 - 18.5
Normal	18.5 - 25
Overweight	25 - 30
Obese Class I	30 - 35
Obese Class II	35 - 40
Obese Class III	> 40

'''

# brief intro to the user
print('Hello, Welcome to the BMI calculator!!')
print('Please make sure you have your weight in kilogram, and your height in meters.')
print('*********************************')


# take user name
name = input('Please Enter your name: ')

# take user's weight:
weight = float(input('Enter your weight in Pounds: '))

# take user's height in Inches
height = float(input('Enter your height in inches: '))

# The formula is given as (weight x 703) / (height x height)
BMI = weight / (height * height)
print(round(BMI, 2))

# conditional statements to check the category of the user per the BMI

if BMI < 16:
        print(name, ', you are Severe Thinness')
elif 16 <= BMI < 17:
        print(name, ', you are Moderate Thinness')
elif 17 <= BMI < 18.5:
        print(name, ', you are Mild Thinness')
elif 18.5 <= BMI < 25:
        print(name, ', you are Normal')
elif 25 <= BMI < 30:
        print(name, ', you are Overweight')
elif 30 <= BMI < 35:
        print(name, ', you are Obese Class I')
elif 35 <= BMI < 40:
        print(name, ', you are Obese Class II')
else:  #BMI >= 40
        print(name, ', you are Obese Class III')

