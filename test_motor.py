import fuzzy_motor as fm

ta=22.5 #constant ambient temperature
tms=[20.5,22.5,33.5,43.5,53.5,63.5,73.5] #test cases (from better to worse)
print ("============= Test results at 22.5 ambient temperature ===============")
my_motor=fm.Thermal_fuzzy_motor()
for tm in tms:
    print ("Motor temp: " ,tm, "status: ",my_motor.compute_status(tm,ta) )
