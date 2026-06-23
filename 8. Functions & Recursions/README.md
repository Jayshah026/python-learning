## Functions

- A function is a block of code which will perform a specific task. 
- It can be reused again and again. 

```python

Syntax (Function definition) : 

def function_name():
    // Code

- Now whenever we want to use this block of code we will call the function and it will execute and we will get an answer.

Calling a function (Function call):

def function_name():
    // Code

function_name() // This will call the function and now we can do the task as we want. 

```

- This is how a function works.

- There are two types of function type : 
1. Default function or pre-defined function that we can use directly.
2. User-Defined function that we can create as we need.

- Here in the function we can pass the arguments and when we call it just put the value in the function where we have pass the arguments accordingly by which we can get the output. 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Recursion 

- A block of code calling it self again and again in order to get an output. 
- This method to call itself is called Recursion. 

Ex : Factorial 

- Let's assume that we want the factorial of value n. 
- Here n = 5. 
- For factorial the formula is... n * factorial(n - 1)
- When we apply here n = 5 and n - 1 = 4.
- Now here n = 4 and n - 1 = 3. 
- Now here n = 3 and n - 1 = 2.
- And at the end n = 2 and n - 1 = 1. 
- Here the formula will stop because here for factorial(1) of factorial(0) = 1. 

- Now at the end factorial(5) = 5 * 4 * 3 * 2 * 1 = 120.

- This is how recursion works.