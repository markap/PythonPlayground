
NUMBERS_STR = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
           "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
           "Seventeen", "Eighteen", "Nineteen"]
NUMBERS = [len(i) for i in NUMBERS_STR]


SECOND_DIGITS_STR = ["Null", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
          "Seventy", "Eighty", "Ninety", "hundred"]
SECOND_DIGITS = [len(i) for i in SECOND_DIGITS_STR]

HUNDRED = len("hundred")
AND = len("and")
ONETHOUSAND = len("onethousand")

# a small array for later cache
# but I guess there is not a real permonance gain, because the calculation so straightforward
twosignnumbers_lookup = dict([(k, v) for k,v in enumerate(NUMBERS)])

def split_number(n):
    if n <= 19 : return NUMBERS[n]
    if n <= 99: 
        second_value = n / 10
        value = SECOND_DIGITS[second_value]
        if n % 10 != 0: value += NUMBERS[n - second_value * 10]
        twosignnumbers_lookup[n] = value
        return value
    if n <= 999:
        third_value = n / 100
        value = HUNDRED + NUMBERS[third_value]
        if n % 100 != 0: 
            value += AND + twosignnumbers_lookup[n - third_value * 100]
        return value
    return ONETHOUSAND



    
LIMIT = 1000
print sum([split_number(i) for i in range(1, LIMIT +1)])
        
        
                            
  
    
    


