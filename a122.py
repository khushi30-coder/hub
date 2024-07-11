#1.slicing
print("   :__________START PROGRAM________________:")
print("1:_____________________________________:")
x=lambda a:a[2:4]
print(x("[welcome ]"))
print("2:_____________________________________:")
#2.strip()
x=lambda a:a.strip()
print(x(" [python ]"))
print("3:_____________________________________:")
#3.lstrip()
x=lambda a:a.lstrip()
print(x(" [java] "))
print("4:_____________________________________:")
#4.rstrip()
x=lambda a:a.rstrip()
print(x(" [css ]"))
#5.strip()
print("5:_____________________________________:")
x=lambda a:a.strip('#')
print(x(" [##my world##]"))
print("6:_____________________________________:")
#6.swapcase
x=lambda a:a.swapcase()
print(x(" [my world]"))
print("7:_____________________________________:")
#7.replace
x=lambda a,old,new:a.replace(old,new)
print(x("[hello world","hello","khushi]"))
print("8:_____________________________________:")
#8.lower
x=lambda a:a.lower()
print(x(" [my world]"))
print("9:_____________________________________:")
#9.upper
x=lambda a:a.upper()
print(x("[my name]"))
print("10:_____________________________________:")
#10.reverse
x=lambda a:a[::-1]
print(x("[css]"))
print("11:_____________________________________:")
#11.strip()
x=lambda a:a.strip("comw")
print(x("[ my. world.com]"))
print("12:_____________________________________:")
#12.lstrip()
x=lambda a:a.lstrip("khushi")
print(x(" [khushi:my name]"))
print("13:_____________________________________:")
#13.join()
x=lambda a:a.join(s)
print(" [my", "world]")
print("14:_____________________________________:")
#14.split()
x=lambda a:a.split()
print(x("[ my name is khushi]"))
print("15:_____________________________________:")
#15.rsplit()
x=lambda a:a.rsplit()
print(x(" [my name is khushi]"))
print("16:_____________________________________:")
#16.capitalize()
x=lambda a:a.capitalize()
print(x(" [life is beautiful]"))
print("17:_____________________________________:")
#17.islower()
x=lambda a:a.islower()
print(x("[ LOVE YOURSELF]"))
print("18:_____________________________________:")
#18.isUPPER()
x=lambda a:a.isupper()
print(x(" [LOVE YOURSELF]"))
print("19:_____________________________________:")
#19.isalpha()
x=lambda a:a.isalpha()
print(x(" [python]"))
print("20:_____________________________________:")
#20.isnumeric()
x=lambda a:a.isnumeric()
print(x("[ javascript 678]"))
print("21:_____________________________________:")
#21.isalnum()
x=lambda a:a.isalnum()
print(x(" [khushi-10]"))
print("22:_____________________________________:")
#22.count()
x=lambda a:a.count("h")
print(x("[hi khushi] "))
print("23:_____________________________________:")
#23.startswith()
x=lambda a:a.startswith("hi")
print(x("[hi khushi]"))
print("24:_____________________________________:")
#24.endswith()
x=lambda a:a.endswith("u")
print(x(" [hru]"))
print("25:_____________________________________:")
#25.center()
x=lambda a:a.center(40,"-")
print(x(" [keep it up]"))
print("26:_____________________________________:")
#26.ljust()
x=lambda a:a.ljust(40,"-")
print(x(" [my life]"))
print("27:_____________________________________:")
#27.rjust()
x=lambda a:a.rjust(40,"-")
print(x(" [my life]"))
print("28:_____________________________________:")
#28.zfill()
x=lambda a:a.zfill(2)
print(x(" [39]"))
print("29:_____________________________________:")
#29.removeprefix()
x=lambda a:a.removeprefix("css:")
print(x("css:java:python"))
print("30:_____________________________________:")
#30.removesuffix()
x=lambda a:a.removesuffix("python")
print(x("css:java:python"))
print("31:_____________________________________:")
#31.partition()
x=lambda a:a.partition("is")
print(x(" [my name is khushi]"))
print("32:_____________________________________:")
#32.find()
x=lambda a:a.find("a")
print(x(" [be happy]"))
print("33:_____________________________________:")
#33.rfind()
x=lambda a:a.rfind("a")
print(x("[be happy always]"))
print(":_____________________________________:")


































