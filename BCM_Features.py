class BCM:
    def __init__(self):
        self.voltage = 12
        self.Power_Mode = "Awake"
        self.CAnoe = "Canoe started"
        self.DrL = "DRL ON"
        self.Drl_output1 = "DRL LH activated"
        self.Drl_output2 = "DRL RH activated"
        self.Head_lamp = "Head_Lamp is off"
        self.Position_Lamp = "Position Lamp is off"
        self.Headlamp_switch = 0
        self.position_lamp_switch = 0
        self.Turn_Indicator_switch = 0
        self.frequency_Hazard  = 0
        self.frequency_turnIndicator = 0
    def head_lamp_activation(self, Headlamp_switch):
        self.Headlamp_switch = Headlamp_switch
        if self.Headlamp_switch == "ON":
            print("---------------------Head Lamp activation-----------------------")
            print("Head Lamp activated")
            print("DRL turned OFF")
        else:
            print("---------------------Head Lamp deactivation-----------------------")
            print("Head Lamp is not activated")
    def Position_Lamp_activation(self, position_lamp_switch):
        self.position_lamp_switch = position_lamp_switch
        if self.Power_Mode == "Active" and self.voltage == 12:
            if self. position_lamp_switch =="ON":
                    print("---------------------Position Lamp activation-----------------------")
                    print("position lamp activated")
                    print("DRL turned off")
        
            else:
                print("---------------------Position Lamp deactivation-----------------------")
                print("position lamp deactivated")
        else:
            print("--------------------------------Position Lamp---------------------------------")
            print(f"Position lamp is not activated check the voltage and power mode\nPower_mode :{self.Power_Mode}\nVoltage= {self.voltage} V\n ")
    def show_status(self):
        print("---------------------Initial condition-------------------------------")
        print("Voltage:", self.voltage,"V")
        print("Canoe status:", self.CAnoe)
        print("DRL Telltale:", self.DrL)
        print("DRL state:", self.Drl_output1)
        print("DRL state:", self.Drl_output2)
    def Power_Mode1(self, New_Power_Mode):
        self.Power_Mode = New_Power_Mode 
        print("Current Power mode:",self.Power_Mode)
        
Bcm1 = BCM()
Bcm1.show_status()
New_Power_Mode = input("Enter the Current Power_Mode: ")
Bcm1.Power_Mode1(New_Power_Mode)
print("----Headlamp Input command------")
Bcm1.head_lamp_activation(str(input("Head_lamp_Switch(Input): ")))
print("------Position Lamp Input Command----------")
Bcm1.Position_Lamp_activation(str(input("Position_Lamp_switch(Input): ")))

class LECU(BCM):
    def __init__(self,bcm):
        self.bcm = bcm
        super().__init__()
        
        self.frequency_turnIndicator = 0
        self.frequency_Hazard = 0
        # self.voltage =12
        # self.Power_Mode = "Run"
    
    def Turn_Indicator_frequency(self,frequency_turnIndicator,frequency_Hazard):
        self.frequency_turnIndicator= frequency_turnIndicator
        self.frequency_Hazard = frequency_Hazard
       
    
    def Turn_Indicator(self,Turn_Indicator_Switch):
        
        self.Turn_Indicator_Switch = Turn_Indicator_Switch
        if self.Power_Mode in ["Active", "Run", "Transport drive", "Transport drive Run"] and self.voltage == 12:
            if self.Turn_Indicator_Switch == "ON":
                print("Turn Indicator is turned ON with",self.frequency_turnIndicator,"ms")
            else:
                print("Turn Indicator is not turned ON")
        else:
                print("Check the turn indicator powermode and voltage")
    
Lecu1 = LECU(Bcm1)
Lecu1.Power_Mode1(New_Power_Mode)
FreqTurn = int(input(f"Enter the Turn_Indicator_frequency: " ))
FreqHazard = int(input(f"Enter the Hazard frequency: "))
Lecu1.Turn_Indicator_frequency(FreqTurn,FreqHazard)
print("LECU Power Mode:", Lecu1.Power_Mode)
print("LECU Voltage:", Lecu1.voltage)
Lecu1.Turn_Indicator(str(input("Enter the Turn_Indicator_Input:")))

    
