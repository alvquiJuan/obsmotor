import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
delta_T = ctrl.Antecedent(np.arange(0, 45, 1), 'delta_T')
condition = ctrl.Consequent(np.arange(0, 100, 1), 'condition')

#Trapezoidal/triangular rules for antecedent, the fuzzy set names are the same for 
# automatic membership functions
delta_T['good']=fuzz.trapmf(delta_T.universe, [0, 0,0.5, 1])
delta_T['decent']=fuzz.trapmf(delta_T.universe, [0, 0.5, 9,10])
delta_T['average']=fuzz.trapmf(delta_T.universe, [9, 10, 19,20])
delta_T['mediocre']=fuzz.trapmf(delta_T.universe, [19, 20, 39,40])
delta_T['poor']=fuzz.trapmf(delta_T.universe, [39, 40, 45,45])

#Automatic triangular rules for consequent, it divides in five groups
condition.automf(5)

#Simple conditional rules "IF antecedent THEN consequence
rule1 = ctrl.Rule(delta_T['good'], condition['good'])
rule2 = ctrl.Rule(delta_T['decent'], condition['decent'])
rule3 = ctrl.Rule(delta_T['average'], condition['average'])
rule4 = ctrl.Rule(delta_T['mediocre'], condition['mediocre'])
rule5 = ctrl.Rule(delta_T['poor'], condition['poor'])

motor_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4, rule5])

#simulation for the motor condition
motor = ctrl.ControlSystemSimulation(motor_ctrl)

#interactive (manual) testing ask for ambient and motor temperatures
#computes delta, and gives motor condition
ambient_T=input("enter ambient temperature")
motor_T=input("enter motor temperature")
raw_delta=float(motor_T)-float(ambient_T)
processed_delta=np.clip(raw_delta,0,45)

motor.input['delta_T'] = processed_delta



motor.compute()

print (motor.output['condition'])
condition.view(sim=motor)

a=input("press something to continue...")
