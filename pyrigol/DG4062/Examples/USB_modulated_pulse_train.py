import time
import pyvisa
from ..lib import definitions as rigol_defs
from ..lib import commands as scpi
from ..lib import SCPI_util


if __name__ == "__main__":
    ## connecting to the visa backend
    rm = pyvisa.ResourceManager()

    ## taking out the address of usb 
    usb_address = rm.list_resources()[0]

    ## open a connection to the resource
    rigol_visa = rm.open_resource(usb_address)    
    scpi_ref = scpi.DG4062_Commander()
    
    ## message list to initiatilize the device
    initial_messages = [scpi_ref.identify_device() ,
            scpi_ref.query_output_impedance(rigol_defs.CHANNELS.CH2) ,                 
            scpi_ref.set_voltage_high_value(rigol_defs.CHANNELS.CH2 , 10), 
            scpi_ref.set_voltage_low_value(rigol_defs.CHANNELS.CH2 , -10),
            scpi_ref.set_source_freq(rigol_defs.CHANNELS.CH2 , 1000),
            scpi_ref.set_output_load(rigol_defs.CHANNELS.CH2 , rigol_defs.OUTPUT_IMPEDANCE.INFINITY),
            scpi_ref.set_number_of_points(16384)
            ]

    ## ------------ making the waveform points ------------------ 
    repeat_point_count = 100
    sym_pt_count = 10
    values = []
    for i in range(sym_pt_count): 
        if(i%2 == 0): 
            for j in range(repeat_point_count):
                values.append(0.2)
        else: 
            for j in range(repeat_point_count):
                values.append(-0.2)

    for i in range(sym_pt_count):
        if(i % 2 == 0):
            # pad to make a perfect rectangle 
            for j in range(repeat_point_count): 
                values.append(1)
            
        else: 
            for j in range(repeat_point_count):
                values.append(-1)

    ## -----------------------------------------------------------
    
    ## formatting the message that tells the device what waveform to generate
    message_load_data = scpi_ref.load_data_values(values)

    ## iterating thourgh the message list and writing the messages to the device. If a 
    ## needs a response, the response is read and put in the answer field of the cmd object   
    mes:SCPI_util.RigolCmdObj = None
    for mes in initial_messages:
        time.sleep(1)
        rigol_visa.write(mes.get_cmd())
        # print(mes.get_cmd())
        if(mes.needs_answer()):
            resp = rigol_visa.read_ascii_values(str)
            mes.set_answer(resp)
            print(resp)
    

    ## write the waveform data to the device
    rigol_visa.write(message_load_data.get_cmd())
    print(message_load_data.get_cmd())