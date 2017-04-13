#/usr/bin/python
#Simple Code By MrPheles
import re

mastercard = '(?:\D|^)(5[1-5][0-9]{2}(?:\ |\-|)[0-9]{4}(?:\ |\-|)[0-9]{4}(?:\ |\-|)[0-9]{4})(?:\D|$)'
visa = '(?:\D|^)(4[0-9]{3}(?:\ |\-|)[0-9]{4}(?:\ |\-|)[0-9]{4}(?:\ |\-|)[0-9]{4})(?:\D|$)'
amex = '(?:\D|^)((?:34|37)[0-9]{2}(?:\ |\-|)[0-9]{6}(?:\ |\-|)[0-9]{5})(?:\D|$)'


print """
   ____              _ _ _      ____              _   ____       _            _             
  / ___|_ __ ___  __| (_) |_   / ___|__ _ _ __ __| | |  _ \  ___| |_ ___  ___| |_ ___  _ __ 
 | |   | '__/ _ \/ _` | | __| | |   / _` | '__/ _` | | | | |/ _ \ __/ _ \/ __| __/ _ \| '__|
 | |___| | |  __/ (_| | | |_  | |__| (_| | | | (_| | | |_| |  __/ ||  __/ (__| || (_) | |   
  \____|_|  \___|\__,_|_|\__|  \____\__,_|_|  \__,_| |____/ \___|\__\___|\___|\__\___/|_|   
                                            Coded By MrPheles                   """

arquivo = raw_input("txt file: ")

with open(arquivo, "r") as f:
    for line in f:
	cc = line.rstrip('\n')
        mastercard_check = re.search(mastercard,cc, re.IGNORECASE)
        visa_check = re.search(visa,cc, re.IGNORECASE)
        amex_check = re.search(amex,cc, re.IGNORECASE)
        if mastercard_check:
            print mastercard_check.group() + " ==> Mastercard"
        elif visa_check:
            print visa_check.group() + " ==> visa"
        elif amex_check:
            print amex_check.group() + " ==> amex"
        else:
            print cc + " ==> Not Found"
