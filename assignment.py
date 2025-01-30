def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return(f"My name is {name} and I am {age} years old")

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return("Greater")
    elif number < 10:
        return("Lesser")
    else:
        return("Equal")

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    result = 0
    while n>0:
        result += n
        n -= 1
    return(result)
    # for num in range(n):
    #     result += num+1
    # return(result)

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    return (sum(numbers), max(numbers), min(numbers))

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    return_students=[]
    for name, score in students_dict.items():
        if score > 80:
            return_students.append(name)
    
    return(return_students)

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    return (set(list1) & set(list2))


def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    result_dict = {}
    result_dict['sum'] = a+b
    result_dict['difference'] = a-b
    result_dict['product'] = a*b
    try:
        result_dict['quotient'] = a/b
    except:
         result_dict['quotient'] = None
    return(result_dict)

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    result_dict = {}
    result_dict['and'] = x and y
    result_dict['or'] = x or y
    result_dict['not_x'] = not x
    return(result_dict)

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    result_dict = {}
    result_dict['and'] = a & b
    result_dict['or'] = a | b
    result_dict['xor'] = a ^ b
    return(result_dict)