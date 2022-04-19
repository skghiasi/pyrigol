import enum 

class FREQUENCY_UNITS(enum.Enum):
    MHZ = 0.001
    KHZ = 1000
    HZ = 1 
    UHZ = 0.000001

class AMPLITUDES(enum.Enum): 
    VPP = 0 
    MVPP = 1 
    VRMS = 2 
    MVRMS = 3
    DBM = 4

class OFFSETS(enum.Enum): 
    V = 0 
    MV = 1 

class HIGH_LEVELS(enum.Enum): 
    V = 0 
    MV = 1

class LOW_LEVELS(enum.Enum): 
    V = 0 
    MV = 1 

class TIME_UNITS(enum.Enum): 
    MS = 0.001 
    KS = 1000 
    S = 1 
    US = 0.000001 
    NS = 0.000000001

class ATTENUATIONS(enum.Enum): 
    _1X = 0 
    _10X = 1 

    def get_string(self): 
        if(self.value == 0): 
            return "1X"
        else: 
            return "10X"

class PULSE_WIDTH_OR_DUTY(enum.Enum): 
    WIDTH = 0
    DUTY = 1

    def get_string(self): 
        return self.name

class COUPLINGS(enum.Enum): 
    AC = 0 
    DC = 1 

    def get_string(self): 
        if(self.value == 0): 
            return "AC"

        else: 
            return "DC"


class GATETIMES(enum.Enum): 
    _1ms = 0 
    _10ms = 1
    _100ms = 2
    _1s = 3
    _10s = 4
    _gt_10s= 5

    def get_string(self): 
        if(self.value == 0): 
            return "USER1"
        elif(self.value == 1): 
            return "USER2"
        elif(self.value == 2): 
            return "USER3" 
        elif(self.value == 3): 
            return "USER4" 
        elif(self.value == 4): 
            return "USER5" 
        elif(self.value == 5): 
            return "USER6"

class ON_OFF(enum.Enum): 
    ON=1 
    OFF=0

    def get_string(self): 
        if(self.value == 0 ): 
            return "OFF"
        elif(self.value == 1): 
            return "ON"


class USERS(enum.Enum): 
    DEFAULT = 0 
    USER1 = 1 
    USER2 = 2
    USER3 = 3
    USER4 = 4 
    USER5 = 5
    USER6 = 6 
    USER7 = 7
    USER8 = 8 
    USER9 = 9 
    USER10 = 10

    def get_string(self): 
        return "USER{}".format(self.value)

class COUNTER_IMPEDANCES(enum.Enum): 
    _50_OHM = 0 
    _1_MEGAOHM = 1

    def get_string(self): 
        if(self.value == 0): 
            return "50"
        elif(self.value == 1): 
            return "1M"

class OUTPUT_IMPEDANCES(enum.Enum): 
    INFINITY = 0 
    MINIMUM = 1
    MAXIMUM = 2 

    def get_string(self): 
        return self.name

class OUTPUT_NOISE_SCALES(enum.Enum): 
    MINIMUM = 0 
    MAXIMUM = 1

    def get_string(self): 
        return self.name

class CHANNELS(enum.Enum): 
    CH1 = 1
    CH2 = 2
    
    def get_string(self): 
        if(self.value == 1): 
            return "CH1"
        elif(self.value == 2): 
            return "CH2"

class DAC16_FLAGS(enum.Enum): 
    CON = 0 
    END = 1

    def get_string(self): 
        return self.name

class MINMAX(enum.Enum): 
    MINIMUM = 0 
    MAXIMUM = 1

    def get_string(self): 
        return self.name


class DAC_INTERP_MODES(enum.Enum): 
    OFF = 0
    LINEAR = 1

    def get_string(self): 
        return self.name