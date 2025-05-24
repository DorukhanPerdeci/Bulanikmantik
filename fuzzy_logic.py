import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Girdiler
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
co2 = ctrl.Antecedent(np.arange(300, 2001, 1), 'co2')
people = ctrl.Antecedent(np.arange(0, 11, 1), 'people')
outside_temp = ctrl.Antecedent(np.arange(-10, 41, 1), 'outside_temp')

# Çıktılar
heating = ctrl.Consequent(np.arange(0, 101, 1), 'heating')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Üyelik fonksiyonları
temperature.automf(3)
humidity.automf(3)
co2.automf(3)
people.automf(3)
outside_temp.automf(3)

heating.automf(3)
fan_speed.automf(3)

# Kurallar
rules = [
    ctrl.Rule(temperature['poor'] | humidity['good'] | co2['good'], heating['high']),
    ctrl.Rule(temperature['good'] | people['average'] | co2['average'], heating['average']),
    ctrl.Rule(outside_temp['poor'], heating['high']),
    ctrl.Rule(co2['poor'] | people['good'], fan_speed['high']),
    ctrl.Rule(co2['average'], fan_speed['average']),
    ctrl.Rule(people['poor'], fan_speed['low']),
]

climate_ctrl = ctrl.ControlSystem(rules)
climate_sim = ctrl.ControlSystemSimulation(climate_ctrl)

def compute_outputs(temp, hum, co2_val, ppl, out_temp):
    climate_sim.input['temperature'] = temp
    climate_sim.input['humidity'] = hum
    climate_sim.input['co2'] = co2_val
    climate_sim.input['people'] = ppl
    climate_sim.input['outside_temp'] = out_temp
    climate_sim.compute()
    return climate_sim.output['heating'], climate_sim.output['fan_speed']
