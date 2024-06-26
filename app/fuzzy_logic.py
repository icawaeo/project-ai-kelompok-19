# fuzzy_logic.py

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_reminder_intensity(time_unused_days):
    # Define fuzzy variables
    time_unused = ctrl.Antecedent(np.arange(0, 101, 1), 'time_unused')
    reminder_intensity = ctrl.Consequent(np.arange(0, 101, 1), 'reminder_intensity')

    # Define fuzzy membership functions
    time_unused['sebentar'] = fuzz.trimf(time_unused.universe, [0, 0, 30])
    time_unused['cukup lama'] = fuzz.trimf(time_unused.universe, [20, 50, 80])
    time_unused['lama sekali'] = fuzz.trimf(time_unused.universe, [60, 100, 100])

    reminder_intensity['rendah'] = fuzz.trimf(reminder_intensity.universe, [0, 0, 30])
    reminder_intensity['sedang'] = fuzz.trimf(reminder_intensity.universe, [20, 50, 80])
    reminder_intensity['tinggi'] = fuzz.trimf(reminder_intensity.universe, [60, 100, 100])

    # Define fuzzy rules
    rule1 = ctrl.Rule(time_unused['sebentar'], reminder_intensity['rendah'])
    rule2 = ctrl.Rule(time_unused['cukup lama'], reminder_intensity['sedang'])
    rule3 = ctrl.Rule(time_unused['lama sekali'], reminder_intensity['tinggi'])

    # Create control system
    reminder_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    reminder = ctrl.ControlSystemSimulation(reminder_ctrl)

    # Input the value
    reminder.input['time_unused'] = time_unused_days

    # Compute the result
    reminder.compute()
    return reminder.output['reminder_intensity']
