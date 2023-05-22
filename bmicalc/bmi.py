#bmi calcuator Imperial and metric
import imperial_calculator as ic
import metric_calculator as mc

imperial_or_metric = input("For imperial press 'I', for metric press 'M'. ").lower()

if imperial_or_metric == 'i':
    ic.impbmi_calc()

elif imperial_or_metric == 'm':
    mc.metricbmi_calc()