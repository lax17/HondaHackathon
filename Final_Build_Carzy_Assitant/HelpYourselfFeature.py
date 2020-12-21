from utils import prepare_voice_output
from constants import *
from capture_stealer import capture_stealer

def Warning_with_Suggestion(MeterIndicator_LowFuel_GAS_status,SecurityAlarm,MeterIndicator_Engine_Failure, MeterIndicator_PowerSystem_Failure):
    print(MeterIndicator_LowFuel_GAS_status)
    if MeterIndicator_LowFuel_GAS_status == "ON":
        prepare_voice_output(MeterIndicator_LowFuel_GAS)
    if SecurityAlarm == "ON":
        capture_stealer()
    if MeterIndicator_Engine_Failure == "ON":
        prepare_voice_output(MeterIndicator_Engine_Failure_Status)




