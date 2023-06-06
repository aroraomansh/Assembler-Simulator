import sys

reg_codes = {"R0":"000","R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110", "FLAGS": "111"}
reg_codes_rev = {"000" : "R0","001" : "R1", "010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}
reg = {"R0" : 0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS": "N"}

Type_A = {"add": '00000', "sub": '00001', "mul": '00110', "xor": '01010', "or": '01011', "and": '01100'}
Type_B = {"movi":"00010","ls":"01001","rs":"01000"}
Type_C = {"mov": '00011', "div": '00111', "not": '01101', "cmp": '01110'}
Type_D = {"store":"00101","load":"00100"}
Type_E = ["01111","11100","11101","11111"]
vars = {}
PC = 0

def overflow(n):
    if n > 65536:
        return True
    elif n < 0:
        return True
    return False

def bitcon(n, num_bits):
    return bin(n).replace("0b", "").zfill(num_bits)

def not_op(n):
    ans = ''
    a = bin(n)[2:]
    for i in a:
        if i == '0':
            ans += '1'
        else:
            ans += '0'
            
    return int(ans,2)

def add(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] + reg[reg2]
        if(overflow(reg[reg1])):
            reg[reg1] = 0
            reg["FLAGS"] = 'V'

def sub(n): 
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] - reg[reg2]
        if(overflow(reg[reg1])):
            reg[reg1] = 0
            reg["FLAGS"] = 'V'

def mul(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] * reg[reg2]
        if(overflow(reg[reg1])):
            reg[reg1] = 0
            reg["FLAGS"] = 'V'

def xor(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] ^ reg[reg2]
    
def or_(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] | reg[reg2]

def and_(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg1] & reg[reg2]

def jmp(s):
    val = s[-7:]
    global PC
    PC = int(val,2)

def jlt(s):
    if reg["FLAGS"] == 'L':
        val = s[-7:]
        global PC
        PC = int(val,2)

def jgt(s):
    if reg["FLAGS"] == 'G':
        val = s[-7:]
        global PC
        PC = int(val,2)

def je(s):
    if reg["FLAGS"] == 'E':
        val = s[-7:]
        global PC
        PC = int(val,2)
        
def mov(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = reg[reg2]

def div(n):
    reg3_code = n[10:13]
    reg4_code = n[13:]
    l = list(reg_codes.values())
    if reg3_code in l and reg4_code in l:
        reg3 = [k for k, v in reg_codes.items() if v == reg3_code][0]
        reg4 = [k for k, v in reg_codes.items() if v == reg4_code][0]
        if reg[reg4] != 0:
            reg["R0"] = reg[reg3] // reg[reg4]
            reg["R1"] = reg[reg3] % reg[reg4]
        else:
            reg["R0"] = 0
            reg["R1"] = 0

def bitwise_not(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        reg[reg1] = not_op(reg[reg2])  

def cmp(n):
    reg1_code = n[10:13]
    reg2_code = n[13:]
    l = list(reg_codes.values())
    if reg1_code in l and reg2_code in l:
        reg1 = [k for k, v in reg_codes.items() if v == reg1_code][0]
        reg2 = [k for k, v in reg_codes.items() if v == reg2_code][0]
        if reg[reg1] == reg[reg2]:
            reg["FLAGS"] = 'E'  #  equal flag
        elif reg[reg1] < reg[reg2]:
            reg["FLAGS"] = 'L'  #  less than flag
        else:
            reg["FLAGS"] = 'G'  #  greater than flag

def movi(s):
    reg_id = reg_codes_rev[s[6:9]]
    val = int(s[9:],2)
    reg[reg_id] = val
    # print(reg_id)
    # print(val)

def rs(s):
    reg_id = reg_codes_rev[s[6:9]]
    val = int(s[9:],2)
    reg[reg_id] = reg[reg_id] >> val

def ls(s):
    reg_id = reg_codes_rev[s[6:9]]
    val = int(s[9:],2)
    reg[reg_id] = reg[reg_id] << val

def load(s):
    reg_id = reg_codes_rev[s[6:9]]
    mem = s[9:]
    reg[reg_id] = vars[mem] 

def store(s):
    reg_id = reg_codes_rev[s[6:9]]
    mem = s[9:]
    vars[mem] = reg[reg_id]

# Type A
def type_A(s):
    if s[0:5] == Type_A["add"]:
        add(s)
    elif s[0:5] == Type_A["sub"]:
        sub(s)
    elif s[0:5] == Type_A["mul"]:
        mul(s)
    elif s[0:5] == Type_A["xor"]:
        xor(s)
    elif s[0:5] == Type_A["or"]:
        or_(s)
    elif s[0:5] == Type_A["and"]:
        and_(s)

# Type C
def type_C(s):
    if s[0:5] == Type_C["mov"]:
        mov(s)
    elif s[0:5] == Type_C["div"]:
        div(s)
    elif s[0:5] == Type_C["not"]:
        bitwise_not(s)
    elif s[0:5] == Type_C["cmp"]:
        cmp(s)

# Type E
def type_E(s):
    if s[0:5] == "01111":
        jmp(s)
    elif s[0:5] == "11100":
        jlt(s)
    elif s[0:5] == "11101":
        jgt(s)
    elif s[0:5] == "11111":
        je(s)

# Type B
def type_B(s):
    if s[0:5] == Type_B["movi"]:
        movi(s)
    elif(s[0:5] == Type_B['ls']):
        ls(s)
    elif(s[0:5] == Type_B['rs']):
        rs(s)

# Type D
def type_D(s):
    if s[0:5] == Type_D["store"]:
        store(s)
    elif s[0:5] == Type_D["load"]:
        load(s)

l = []
for i in sys.stdin:
    l.append(i.strip())

while l[PC][0:5] != "11010":
    # print(i)
    type_B(l[PC])
    type_C(l[PC])
    type_E(l[PC])
    type_D(l[PC])
    print(bitcon(PC,7),end = "        ")
    # print(bin(PC)[2:],end = " ")
    for i in reg.values():
        if i == 'V':
            print("0000000000001000")
        elif i == 'L':
            print("0000000000000100")
        elif i == 'G':
            print("0000000000000010")
        elif i == 'E':
            print("0000000000000001")
        elif i == "N":
            print("0000000000000000")
        else:
            print(bitcon(i,16),end = " ")
    # print(*reg.values())
    PC+= 1

print(bitcon(PC,7),end = " ")
for i in reg.values():
    if i == 'V':
        print("0000000000001000")
    elif i == 'L':
        print("0000000000000100")
    elif i == 'G':
        print("0000000000000010")
    elif i == 'E':
        print("0000000000000001")
    elif i == "N":
        print("0000000000000000")
    else:
        print(bitcon(i,16),end = "        ")

# Memory Dump
lines = 0
for i in l:
    print(i)
    lines+= 1
for i in vars.values():
    print(bitcon(i,16))
    lines += 1
for i in range(128 - lines):
    print(bitcon(0,16))
