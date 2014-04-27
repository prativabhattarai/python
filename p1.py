def convert_to_celsius(fahrenheit):
    ''' ( number) -> number
    Return the number of celsius degrees equivalent to fahrenheit degree

    >>> convert_to_celsius (32)
    0
    >>> convert_to_celsius (212)
    100
    '''
    celcius = (fahrenheit - 32)*5/9;
    return celcius;

def convert_to_fahrenheit(celsius):
    
    '''( number) -> number
    return the number of celsius degrees equivalent to fahrenheir degree

    >>> convert_to_fahrenheit(0)
    32
    >>> convert_to_fahrenheit(100)
    212
    '''
    fahrenheit= (celsius*9/5 + 32); 
    return fahrenheit;

print("celcius: 0, Fahrenheit: ",convert_to_fahrenheit(0));
print("celcius: 100, fahrenheit: ",convert_to_fahrenheit(100));

kkkjjj
                                            

