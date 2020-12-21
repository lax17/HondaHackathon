import pandas as pd
from HelpYourselfFeature import Warning_with_Suggestion
import time
car_data = pd.read_csv("carprobe.csv")

class Car:
    def __init__(self):
        self.car_sleep = 3
        for index, car_insta in car_data.head(2).iterrows():
            if not self.car_sleep:
                print("Making Car Sleep for 3 seconds so instance of a Car Completes the Journey.....")
                time.sleep(3)
            self.mo_id = car_insta["mo_id"]
            self.Aircon_ACStatus_Front = car_insta["properties/L/Aircon_ACStatus_Front"]
            self.Aircon_AirRecirculationMode = car_insta["properties/L/Aircon_AirRecirculationMode"]
            self.Aircon_FanStatus_Front =  car_insta["properties/L/Aircon_FanStatus_Front"]
            self.Aircon_Mode_DR = car_insta["properties/L/Aircon_Mode_DR"]
            self.Aircon_RemoteControl_Status = car_insta["properties/L/Aircon_RemoteControl_Status"]
            self.Aircon_TemperatureSetting_DR = car_insta["properties/L/Aircon_TemperatureSetting_DR"]
            self.Aircon_TemperatureSetting_ValueType =  car_insta["properties/L/Aircon_TemperatureSetting_ValueType"]
            self.Brake_ParkingBrake = car_insta["properties/L/Brake_ParkingBrake (IG1PullUp)"]
            self.MeterIndicator_ABS =  car_insta["properties/L/MeterIndicator_ABS"]
            self.MeterIndicator_AutoStop_Amber = car_insta["properties/L/MeterIndicator_AutoStop_Amber"]
            self.MeterIndicator_BATT =  car_insta["properties/L/MeterIndicator_BATT"]
            self.MeterIndicator_Brake_Amber =  car_insta["properties/L/MeterIndicator_Brake_Amber"]
            self.MeterIndicator_Brake_Red =  car_insta["properties/L/MeterIndicator_Brake_Red"]
            self.MeterIndicator_CruiseControl=  car_insta["properties/L/MeterIndicator_CruiseControl"]
            self.MeterIndicator_CruiseMain =  car_insta["properties/L/MeterIndicator_CruiseMain"]
            self.MeterIndicator_DoorOpen =  car_insta["properties/L/MeterIndicator_DoorOpen"]
            self.MeterIndicator_ECO =  car_insta["properties/L/MeterIndicator_ECO"]
            self.MeterIndicator_EPS =  car_insta["properties/L/MeterIndicator_EPS"]
            self.MeterIndicator_Engine_Failure =  car_insta["properties/L/MeterIndicator_Engine_Failure"]
            self.MeterIndicator_FrontFog =  car_insta["properties/L/MeterIndicator_FrontFog"]
            self.MeterIndicator_HeadlightControl_Failure =  car_insta["properties/L/MeterIndicator_HeadlightControl_Failure"]
            self.MeterIndicator_Headlight_High =  car_insta["properties/L/MeterIndicator_Headlight_High"]
            self.MeterIndicator_Headlight_Small =  car_insta["properties/L/MeterIndicator_Headlight_Small"]
            self.MeterIndicator_LowFuel_GAS= car_insta["properties/L/MeterIndicator_LowFuel_GAS"]
            self.MeterIndicator_Oil_Pressure= car_insta["properties/L/MeterIndicator_Oil_Pressure"]
            self.MeterIndicator_ParkingSensor_Amber= car_insta["properties/L/MeterIndicator_ParkingSensor_Amber"]
            self.MeterIndicator_PowerSystem_Failure= car_insta["properties/L/MeterIndicator_PowerSystem_Failure"]
            self.MeterIndicator_SRS= car_insta["properties/L/MeterIndicator_SRS"]
            self.MeterIndicator_Seatbelt= car_insta["properties/L/MeterIndicator_Seatbelt"]
            self.MeterIndicator_Seatbelt_RC= car_insta["properties/L/MeterIndicator_Seatbelt_RC"]
            self.MeterIndicator_Seatbelt_RL= car_insta["properties/L/MeterIndicator_Seatbelt_RL"]
            self.MeterIndicator_Seatbelt_RR= car_insta["properties/L/MeterIndicator_Seatbelt_RR"]
            self.MeterIndicator_SmartEntry= car_insta["properties/L/MeterIndicator_SmartEntry"]
            self.MeterIndicator_SportMode= car_insta["properties/L/MeterIndicator_SportMode"]
            self.MeterIndicator_TEMP_Cold_Hot= car_insta["properties/L/MeterIndicator_TEMP_Cold_Hot"]
            self.MeterIndicator_TEMP_Hot= car_insta["properties/L/MeterIndicator_TEMP_Hot"]
            self.MeterIndicator_TPMS_DWS= car_insta["properties/L/MeterIndicator_TPMS_DWS"]
            self.MeterIndicator_VSA_Act= car_insta["properties/L/MeterIndicator_VSA_Act"]
            self.MeterIndicator_Washer_Empty= car_insta["properties/L/MeterIndicator_Washer_Empty"]
            self.RemoteEngineStarter_PowerMode= car_insta["properties/L/RemoteEngineStarter_PowerMode"]
            self.SeatBeltReminder_DR= car_insta["properties/L/SeatBeltReminder_DR"]
            self.SeatBeltReminder_RC= car_insta["properties/L/SeatBeltReminder_RC"]
            self.SeatBeltReminder_RL= car_insta["properties/L/SeatBeltReminder_RL"]
            self.SeatBeltReminder_RR= car_insta["properties/L/SeatBeltReminder_RR"]
            self.SeatbeltStatus_DR= car_insta["properties/L/SeatbeltStatus_DR"]
            self.SecurityAlarm= car_insta["properties/L/SecurityAlarm"]
            self.EngineCoolantTemp= car_insta["properties/O/EngineCoolantTemp"]
            self.FuelLevel= car_insta["properties/O/FuelLevel"]
            self.FuelLevelRaw= car_insta["properties/O/FuelLevelRaw"]
            self.VehicleInteriorTemperature= car_insta["properties/O/VehicleInteriorTemperature"]
            self.ccMainSw= car_insta["properties/O/ccMainSw"]
            self.distanceToEmpty= car_insta["properties/O/distanceToEmpty"]
            self.engineRpm= car_insta["properties/O/engineRpm"]
            self.fuelMode= car_insta["properties/O/fuelMode"]
            self.fuelRatio= car_insta["properties/O/fuelRatio"]
            self.ignitionOnTime= car_insta["properties/O/ignitionOnTime"]
            self.meterIndicatorLowFuel= car_insta["properties/O/meterIndicatorLowFuel"]
            self.odometer= car_insta["properties/O/odometer"]
            self.seatBeltStatus= car_insta["properties/O/seatBeltStatus"]
            self.tcuAcc= car_insta["properties/O/tcuAcc"]
            self.tcuAccuracy= car_insta["properties/O/tcuAccuracy"]
            self.tcuBatteryVoltage= car_insta["properties/O/tcuBatteryVoltage"]
            self.tcuIgnitionStatus= car_insta["properties/O/tcuIgnitionStatus"]
            self.tripEndTime = car_insta["properties/O/tripEndTime"]
            self.tripStartLat= car_insta["properties/O/tripStartLat"]
            self.tripStartLong= car_insta["properties/O/tripStartLong"]
            self.tripStartTime= car_insta["properties/O/tripStartTime"]
            self.tripStatus= car_insta["properties/O/tripStatus"]
            self.road_type= car_insta["road_type"]
            self.speed =  car_insta["speed"]
            print("Car Started with below Properties.........................")
            print("\n",self.mo_id ,self.Aircon_ACStatus_Front ,self.Aircon_AirRecirculationMode ,
                self.Aircon_FanStatus_Front,
                self.Aircon_Mode_DR ,
                self.Aircon_RemoteControl_Status ,
                self.Aircon_TemperatureSetting_DR ,
                self.Aircon_TemperatureSetting_ValueType ,
                self.Brake_ParkingBrake ,
                self.MeterIndicator_ABS ,
                self.MeterIndicator_AutoStop_Amber ,
                self.MeterIndicator_BATT,
                self.MeterIndicator_Brake_Amber,
                self.MeterIndicator_Brake_Red ,
                self.MeterIndicator_CruiseControl,
                self.MeterIndicator_CruiseMain,
                self.MeterIndicator_DoorOpen ,
                self.MeterIndicator_ECO,
                self.MeterIndicator_EPS,
                self.MeterIndicator_Engine_Failure ,
                self.MeterIndicator_FrontFog ,
                self.MeterIndicator_HeadlightControl_Failure ,
                self.MeterIndicator_Headlight_High ,
                self.MeterIndicator_Headlight_Small ,
                self.MeterIndicator_LowFuel_GAS,
                self.MeterIndicator_Oil_Pressure,
                self.MeterIndicator_ParkingSensor_Amber,
                self.MeterIndicator_PowerSystem_Failure,
                self.MeterIndicator_SRS,
                self.MeterIndicator_Seatbelt,
                self.MeterIndicator_Seatbelt_RC,
                self.MeterIndicator_Seatbelt_RL,
                self.MeterIndicator_Seatbelt_RR,
                self.MeterIndicator_SmartEntry,
                self.MeterIndicator_SportMode,
                self.MeterIndicator_TEMP_Cold_Hot,
                self.MeterIndicator_TEMP_Hot,
                self.MeterIndicator_TPMS_DWS,
                self.MeterIndicator_VSA_Act,
                self.MeterIndicator_Washer_Empty,
                self.RemoteEngineStarter_PowerMode,
                self.SeatBeltReminder_DR,
                self.SeatBeltReminder_RC,
                self.SeatBeltReminder_RL,
                self.SeatBeltReminder_RR,
                self.SeatbeltStatus_DR,
                self.SecurityAlarm,
                self.EngineCoolantTemp,
                self.FuelLevel,
                self.FuelLevelRaw,
                self.VehicleInteriorTemperature,
                self.ccMainSw,
                self.distanceToEmpty,
                self.engineRpm,
                self.fuelMode,
                self.fuelRatio,
                self.ignitionOnTime,
                self.meterIndicatorLowFuel,
                self.odometer,
                self.seatBeltStatus,
                self.tcuAcc,
                self.tcuAccuracy,
                self.tcuBatteryVoltage,
                self.tcuIgnitionStatus,
                self.tripEndTime ,
                self.tripStartLat,
                self.tripStartLong,
                self.tripStartTime,
                self.tripStatus,
                self.road_type,
                self.speed)
            Warning_with_Suggestion(self.MeterIndicator_LowFuel_GAS)
            self.car_sleep = None

Car()
