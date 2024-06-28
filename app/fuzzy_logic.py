import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definisikan variabel input
time_since_last_use = ctrl.Antecedent(np.arange(0, 11, 1), 'time_since_last_use')
reminder_ignored = ctrl.Antecedent(np.arange(0, 11, 1), 'reminder_ignored')

# Definisikan variabel output
reminder_urgency = ctrl.Consequent(np.arange(0, 11, 1), 'reminder_urgency')

# Definisikan fungsi keanggotaan untuk setiap variabel input
time_since_last_use['low'] = fuzz.trimf(time_since_last_use.universe, [0, 0, 5])
time_since_last_use['medium'] = fuzz.trimf(time_since_last_use.universe, [0, 5, 10])
time_since_last_use['high'] = fuzz.trimf(time_since_last_use.universe, [5, 10, 10])

reminder_ignored['low'] = fuzz.trimf(reminder_ignored.universe, [0, 0, 5])
reminder_ignored['medium'] = fuzz.trimf(reminder_ignored.universe, [0, 5, 10])
reminder_ignored['high'] = fuzz.trimf(reminder_ignored.universe, [5, 10, 10])

# Definisikan fungsi keanggotaan untuk variabel output
reminder_urgency['low'] = fuzz.trimf(reminder_urgency.universe, [0, 0, 5])
reminder_urgency['medium'] = fuzz.trimf(reminder_urgency.universe, [0, 5, 10])
reminder_urgency['high'] = fuzz.trimf(reminder_urgency.universe, [5, 10, 10])

# Definisikan aturan fuzzy
rule1 = ctrl.Rule(time_since_last_use['high'] & reminder_ignored['high'], reminder_urgency['high'])
rule2 = ctrl.Rule(time_since_last_use['medium'] & reminder_ignored['medium'], reminder_urgency['medium'])
rule3 = ctrl.Rule(time_since_last_use['low'] & reminder_ignored['low'], reminder_urgency['low'])

# Buat sistem kontrol
reminder_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
reminder_sim = ctrl.ControlSystemSimulation(reminder_ctrl)

def calculate_reminder_urgency(last_use_hours, ignored_times):
    reminder_sim.input['time_since_last_use'] = last_use_hours
    reminder_sim.input['reminder_ignored'] = ignored_times
    reminder_sim.compute()
    return reminder_sim.output['reminder_urgency']
