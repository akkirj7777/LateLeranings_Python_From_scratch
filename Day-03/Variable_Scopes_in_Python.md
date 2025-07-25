Variable Scope in Python
Basically from where the variable is accessible or visible

Mainly, there are Global and Local scopes to define variables in programming languages.

example:

```python
name = "Luffy"       # Global Variable

def greet():
    name = "Akshay"  # local variable
    print("Hello", name)

greet()
```

Output:
```
$ python test2.py Hello Akshay
```

- In the above example, we have defined the variable ‘number‘ two times, once globally and again inside ‘greet():‘. But when we run this program, the function by default gives preference to its local variable (name),
which stores the string “Akshay“ and prints the output as ```$ python test2.py Hello Akshay``` even after we have written a global variable as ```name = “Luffy“``` 



Another example:
```python
a = 10    #Global Variable
b = 6

def addition(): 
    a = 5    #local Variable
    b = 5
    print(a + b)

def sub():
    print(a - b)

addition()
sub()

```

```
Output:
$ python test.py
10
4
```

- In the above example, we have defined two functions ```addition():``` and ```sub():```. First function has its own local variables defined as ```a = 5, b = 5``` 
whereas the second function accesses the global variables as ```a = 10, b = 6```.



Lets get more deeper!

see the exapmle below:

```python
def addition():
    a = 10
    b = 5
    print(a + b)
    

def sub():
    print(a - b)


addition()
sub()

```

Output:
```
$ F:/Python/python-for-devops/.venv/Scripts/python.exe f:/Python/python-for-devops/Day-03/test.py
15
Traceback (most recent call last):
  File "f:\Python\python-for-devops\Day-03\test.py", line 12, in <module>
    sub()
  File "f:\Python\python-for-devops\Day-03\test.py", line 8, in sub
    print(a - b)
          ^
NameError: name 'a' is not defined
```

- as we can see, only first function is executed correctly and python threw an error while executing the second function which is ```sub()```, the reason being this function fails to identify the variables as they are not defined in first place where as in first function ```addition()```,
the variables are defined locally and one function cannot access teh variables defined inside the scope of another function.

Note:
If we want to define variables that all functions can access, we should define those variables in the global scope. On the other hand, if we want variables to be available and accessible only within one function, we should define them with a local scope.

- Now to overcome the error in above block of code we will define one more variable ```'c = 10'``` and we will put it inside first function ```addition()```, we will define ```'a'``` and ```'b'``` globally as follows:

```python
a = 10
b = 5

def addition():
    c = 10
    print(a + b + c)
    

def sub():
    print(a - b)


addition()
sub()
```

 output:

```
$ F:/Python/python-for-devops/.venv/Scripts/python.exe f:/Python/python-for-devops/Day-03/test.py
25
5

```
