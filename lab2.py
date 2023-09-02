(b) Factorial and Binomial Co-effi cient
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
# Finding factorial using functions (recursive)
if n == 0 or n == 1:
return 1
else:
return n * fact(n-1)
n_minus_r = fact(n-r)
r_fact = fact(r)
print("Factorial: ", fact(n))
def fact(n):
print("Binomial Co-efficient: ", fact(n)/(n_minus_r*r_fact))
Enter the value of n: 5Enter the value of r: 3Factorial: 120Binomial Co-efficient: 10.0
(a) Fibonacci Series
# Fibonacci using functions (recursive)
n =
int
(
input
(
"Enter the value of n: "
))
def
fibonacci
(
n
):
if
n <
2
:
return
1
return
fibonacci(n
-1
) + fibonacci(n
-2
)
print
(
0
, end =
' '
)
for
i
in
range
(n -
1
):
print
(fibonacci(i), end =
' '
)
Enter the value of n: 150 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# Alternate method
n =
int
(
input
(
"Enter the value of n: "
))
a =
0
b =
1
count =
0
if
n <=
0
:
print
(
"Please enter a valid integer"
)
elif
n ==
1
:
print
(
"Fibonacci series upto 1"
)
print
(a)
else:
