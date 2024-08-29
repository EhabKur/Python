'''
print("Hello Python"); print("Hello 2 Python")
if True:
     print("hello python")
#----------------------6-----------------------
# تحديد نوع البيانات 
x = 10 ; print(type(x))   # <class 'int'>
y = "Hello"  ; print(type(y))  # <class 'str'>                             
z = [1, 2, 3] ; print(type(z))  # <class 'list'>
print(type(100.08))           # <class 'float'>
print(type( (1,2,6,3,8,9)))    #<class 'tuple'>
print( type(  { "one":1 , "two" :2 , "three" :3 })) # <class 'dict'>
print(type(2==2))               #<class 'bool'>

#--------------------7--------------------------------------
# -- Variables --
# Syntax => [Variable Name] [Assignment Operator] [Value]
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore --> x = d ; y=R
# [2] You Cannot With Num Or Special Characters  --> 100 = d ; # =R
# [3] Can Include (0-9) Or Underscore --> 
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------

name = "Ehabelo Kur" ; print(name)  # Virable is Single Word => Normal
myName = "Ehabelo Kur" ; print(myName) # Virable is Two Words => camelCase
my_name = "Ehabelo Kur" ;print(my_name)  # Virable is Two Words => snake_case
# 52 = "dfgdfg" ; print(52)  --> nicht richtig formuliert
x_Ariha = 86 ; print (x_Ariha)
# x-Ariha = 86 ; print (x-Ariha) --> nicht richtig formuliert -->
# Stadt = 'KALI'; print (stadt) --> nicht richtig formuliert--> the letter should be exactly like you defindet it. 
#________________________8______________________________________
# ---------------

# -- Variables --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution
# --------------------------------------------------------
# Reserved Words
help("keywords") # --> يعطي كل الكلمات المحجوزة بلغة البرمجة  
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

#___________________________________9____________________________________

# ----------------------------
# Escape Sequences Characters


# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------
print("Hello\b World") # \b  # Will Remove o    => Back Space
print("Hello \
I Love \
Python")    #  بالكود عند النزول لسطر جديد فلا يقبل ذلك الا بالاشارة المائلة => Escape New Line + \
print("I Love Back Slash \\") # Escape Back Slash # باك سلاش مرتين لتظهر بالطباعة واحدة 
print('I Love Single Quote \'Test\' ')  # Escape Single Quote
print("I Love Double Quotes \"Test\" ")  # Escape Double Quotes
print("Hello World\nSecond Line")   # للبداية من سطر جديد اي كبس انتر # Line Feed Character 
print("123456\rAbcd") # بعدد الاحرف بعد سلاش ار  تحذف من النص السابق و تستعيض بهم # Carriage Return
print("Hello\tPython")  # Horizontal Tab
print("\x45\x68\x61\x62")  #  \x??    #طباعة اي شيء باعتماد الهكس  # Character Hex Value
# رابط لكل كاراكتر بلغة الهكس          https://www.ibm.com/docs/en/ste/11.0.0?topic=maps-hex-decimal-symbol-values
#___________________________________10____________________________________
'''
