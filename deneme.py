
def precedence(op):# öncelik tanımlıyorum
     
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/' or op == '%' or op == '**' or op== ' // 'or op == '<' or op == '>' or op== ' ==':
        return 2
    return 0
 
def applyOp(a, b, op):#  operationları tanımlıyorum
     
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    if op == '%': return a % b
    if op == '//': return a // b
    if op == '**': return a ** b
    if op == '>' : return a > b
    if op == '<' : return a < b
    if op == '==': return a == b

# Function that returns value of
# expression after evaluation.
def evaluate(info): # değerlendirmeden sonra fonksiyonun değerini döndüren ifade
     
    values = [] #int değerleri tutuan array

    ops = [] #operation değerlerini tutuan array

    
    i = 0
     
    while i < len(info): #info represents the values while operations being done
         
        # Current info is a whitespace, skip it.
        if info[i] == ' ':
            i += 1
            continue
         
        # Current info is an opening brace, push it to 'ops'
        elif info[i] == '(':
            ops.append(info[i])
         
        # Current token is a number, push it to stack for numbers.
        elif info[i].isdigit():
            val = 0
             
            # There may be more than one digits in the number.
            while (i < len(info) and
                info[i].isdigit()):
             
                val = (val * 10) + int(info[i]) 
                i += 1
             
            values.append(val)
             
            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  info position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
            i-=1
         
        # Closing brace encountered, solve entire brace.

        
        elif info[i] == ')':
         
            while len(ops) != 0 and ops[-1] != '(':
             
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # pop opening brace.
            ops.pop()
         
        # Current token is an operator.
        else:
         
            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while (len(ops) != 0 and
                precedence(ops[-1]) >
                   precedence(info[i])):
                         
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                 
                values.append(applyOp(val1, val2, op))
             
            # Push current token to 'ops'.
            ops.append(info[i])
         
        i += 1
     
    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:
         
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
                 
        values.append(applyOp(val1, val2, op))
     
    # Top of 'values' contains result,
    # return it.
    return values[-1]
 
# Driver Code

with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

 
for elm in range(len(lines)):

 print(evaluate(lines[elm]))
    
            