has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:     #and, or,NOT are logical operators
    print("Eligible for loan")
    
    
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Not eligible")