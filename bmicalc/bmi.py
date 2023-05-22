#bmi calcuator Imperial and metric
import imperial_calculator as ic
import metric_calculator as mc

imperial_or_metric = input("For imperial press 'I', for metric press 'M'. ").lower()



if imperial_or_metric == 'i':
    try:
        imp_weight = float(input("Please enter your weight in pounds. "))
        imp_height = float(input("Please enter your height in feet. "))
        bmi = ic.impbmi_calc(imp_weight, imp_height)
    except (ValueError, ZeroDivisionError):
        print("Invalid input! Please try again.")
    else:
        if 18.5 >= bmi <= 25:
            print("Your bmi is %g.\nYou are within the ideal weight range." %bmi)
        elif bmi > 25:
            print("Your bmi is %g.\nYou are overweight. You should see a doctor." %bmi)
        elif bmi < 18.5:
            print("Your bmi is %g.\nYou are underweight. You should see a doctor." %bmi)

elif imperial_or_metric == 'm':
    try:
        met_weight = float(input("Please enter your weight in kilograms. "))
        met_height = float(input("Please enter your height in centimeters. "))
        bmi = mc.metricbmi_calc(met_weight,met_height)
    except (ValueError, ZeroDivisionError):
        print("Invalid input! Please try again.")
    else:
        if 18.5 >= bmi <= 25:
            print("Your bmi is %g.\nYou are within the ideal weight range." % bmi)
        elif bmi > 25:
            print("Your bmi is %g.\nYou are overweight. You should see a doctor." % bmi)
        elif bmi < 18.5:
            print("Your bmi is %g.\nYou are underweight. You should see a doctor." % bmi)