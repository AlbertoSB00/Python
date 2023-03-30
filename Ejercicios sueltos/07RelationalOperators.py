"""

Program: 07RelationalOperators.py
Author: Alberto Sánchez Barona
Date: 29/09/2022
Description: Examples of use of relational operators

"""

# Relational operators are used to make comparison between data, typically 2 operands.
# The result of a comparison is a logical or boolean datatype.
# True or False.

# op1 == op2 -> Equal operator. True if two operands are equal. False otherwise.
my_age = 21
my_cousing_age = 22
result = my_age == my_cousing_age
print("Is my cousing as old like me?", result)

# A very common error is to omit one =. In this case there's no a syntax error.
result = my_age = my_cousing_age
print("Is my cousing as old like me?", result)
print(type(result))

# We can use different datatype operands.
my_weight = 110.54
your_weight = 80
result = my_weight == your_weight
print("Am I as fat like you?", result)

# We can use variables, literals and, in general, expressions.
result = my_age * 2 == your_weight - 10

# op1 != op2 -> Not equal operator. True if two operands are different. False otherwise.
password = "abcd1234@"
pass_user = input("Enter your password: ")
result = password != pass_user
print("Are the passwords different?", result)

result = my_age != my_cousing_age
print("Is my cousing as old like me?", result)

# op1 > op2 -> Greater than operator. True if op1 in grater than op2. False otherwise.
my_age = 21
my_cousing_age = 22
result = my_age > my_cousing_age
print("Am I older than my cousing?", result)

minimun_wage = 1000
my_salary = int(input("Enter your salary: "))
result = my_salary > minimun_wage
print("Do I earn more money than the minimum wage?", result)

# op1 >= op2 -> Greater or equal operator. True if op1 is greater or equal than op2. False otherwise.
result = my_salary >= minimun_wage
print("Do I earn at minimum the minimum wage?", result)

# op1 < op2 -> Lower than operator. True if op1 is lower than op2. False otherwise.
result = my_salary < minimun_wage
print("Do I earn less than the minimum wage?", result)

# op1 <= op2 -> Lower or equal operator. True if op1 is lower or equal than op2. False otherwise.
result = my_salary <= minimun_wage
print("Do I earn at maximum the minimum wage?", result)

# Problems when we compare strings.
# The comparison of strings is character by character. It begins with the first character . If they are equal
# it continues with the following character. So until it finds a different character in both strings.
# To decide if a character is equal, grater or lower than another one, it uses the unicode code.
s1 = "aa"
s2 = "ab"
print("Are alike?", s1 == s2)
print("Are different?", s1 != s2)

s2 = "a"
print("Are alike?", s1 == s2)
print("Are different?", s1 != s2)

s1 = "Zapping"
s2 = "Above"
print("Are s1 greater s2?", s1 > s2)

s1 = "ábaco"
s2 = "above"
print("Are s1 greater s2?", s1 > s2)

print("Unicode code")
print(ord("a"), end=" ")
print(ord("z"), end=" ")
print(ord("á"))
