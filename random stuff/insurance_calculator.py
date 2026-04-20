# Using a formula that estimates a person’s yearly insurance costs, 
# investigate how different factors such as age, sex, BMI, etc. affect the prediction



# create the initial variables below
age = 28
#0 for female, 1 for male*
sex = 0
#individual’s body mass index
bmi = 26.2
#number of children the individual has
num_of_children = 3
#0 for a non-smoker, 1 for a smoker
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370*bmi + 425*num_of_children+24000*smoker-12500

print(f"This persons insurance cost is ${insurance_cost} dollars.")
# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370*bmi + 425*num_of_children+24000*smoker-12500
change_in_insurance_cost = insurance_cost-new_insurance_cost 

print("\n")
print(f"The change in cost of insurance after increasing the age by 4 years is ${change_in_insurance_cost} dollars")

# BMI Factor
age = 28
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370*bmi + 425*num_of_children+24000*smoker-12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("\n")
print(f"The change in cost of insurance after increasing the bmi by 4 years is ${change_in_insurance_cost} dollars")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370*bmi + 425*num_of_children+24000*smoker-12500
change_in_insurance_cost = new_insurance_cost - insurance_cost

print("\n")
print(f"The change in cost of insurance after increasing the gender by 4 years is ${change_in_insurance_cost} dollars")

# Extra Practice

smoker = 1
num_of_children += 4


new_insurance_cost = 250 * age - 128 * sex + 370*bmi + 425*num_of_children+24000*smoker-12500
change_in_insurance_cost = new_insurance_cost - insurance_cost


print("\n")
print(f"The change in cost of insurance after increasing the children by 4 and becoming a smoker is ${change_in_insurance_cost} dollars")