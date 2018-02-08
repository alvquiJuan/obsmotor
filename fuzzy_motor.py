import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
temperature = ctrl.Antecedent(np.arange(0, 45, 1), 'temperature')

temperature['normal']=fuzz.trimf(temperature.universe, [0, 0, 1])
temperature['leve']=fuzz.trapmf(temperature.universe, [0, 1, 9,10])
temperature['moderado']=fuzz.trapmf(temperature.universe, [9, 10, 19,20])
temperature['grave']=fuzz.trapmf(temperature.universe, [19, 20, 39,40])
temperature['crítico']=fuzz.trapmf(temperature.universe, [39, 40, 45,45])


temperature.view()
a=input("press something to continue...")
