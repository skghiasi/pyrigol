from .SCPI_util import RigolCmdObj as cmdObj
from . import definitions
import inspect
class DG4062_Commander:

    def __init__(self): 
        pass 

    def set_counter_attenuation(self , atn:definitions.ATTENUATIONS): 
        result = ":COUNter:ATTenuation {}".format(atn.get_string())
        return cmdObj(result) 

    def query_counter_attenuation(self): 
        result = ":COUNter:ATTenuation?"
        return cmdObj(result)


    def set_counter_auto(self):
        """
        Send this command and the instrument will set the gate time of the counter automatically. 
        This command is only available when the counter function is enabled.
        The function of this command is the same with that of the :COUNter:GATEtime AUTO command
        """
        result = ":COUNter:AUTO"
        return cmdObj(result)

    
    def set_counter_coupling(self , cpl:definitions.COUPLINGS): 
        """ 
            Sets the coupling of the counter
        """
        result = ":counter:coupling {}".format(cpl.get_string())
        return cmdObj(result)

    def query_counter_coupling(self): 
        
        result = ":counter:coupling?"
        return cmdObj(result)

    
    def set_counter_gatetime(self , time:definitions.GATETIMES): 
        result = ":counter:gatetime {}".format(time.get_string())
        return cmdObj(result)

    def set_counter_HF(self , on_off:definitions.ON_OFF): 
        result = ":counter:hf {}".format(on_off.get_string())
        return cmdObj(result)

    def query_counter_HF(self): 
        result = ":counter:hf?"
        return cmdObj(result)

    def set_counter_impedance(self , counter_imp:definitions.COUNTER_IMPEDANCES):
        if(not isinstance(counter_imp , definitions.COUNTER_IMPEDANCES)): 
            raise Exception("invalid argument: counter_impedance")

        result = ":counter:impedance {}".format(counter_imp.get_string())
        return cmdObj(result)

    def query_counter_impedance(self): 
        result = ":counter:impedance?"
        return cmdObj(result)

###
# counter not complete yet
#################################################
    def set_coupling_amplitude_deviation(self , deviation_vpp):
        if(deviation_vpp < 0 or deviation_vpp > 20 ): 
            raise Exception 
        
        result = ":coupling:ampl:deviation {}".format(deviation_vpp)
        return cmdObj(result)

    def query_coupling_amplitude_deviation(self): 
        result = ":coupling:ampl:deviation?"
        return cmdObj(result)

    
    def set_amplitude_coupling(self , on_off:definitions.ON_OFF): 
        result = ":coupling:ampl {}".format(on_off.get_string())
        return cmdObj(result)

    def query_amplitude_coupling(self): 
        result = ":coupling:ampl?"
        return cmdObj(result)

    def set_coupling_channel_base(self , ch:definitions.CHANNELS):
        result = ":coupling:channel:base {}".format(ch.get_string())
        return cmdObj(result)

    def query_coupling_channel_base(self): 
        result = "coupling:channel:base?"
        return cmdObj(result)

    def set_copuling_freq_deviation(self , deviation): 
        if(deviation < 0 or deviation > 160000000): 
            raise Exception("frequency deviation should be between 0 uHz and 160 Mhz")
    
        result = ":coupling:frequency:deviation {}".format(deviation)
        return cmdObj(result)

    def query_coupling_freq_deviation(self): 
        result = ":coupling:frequency:deviation?"
        return cmdObj(result)

    def set_freq_deviation_on_off(self , on_off:definitions.ON_OFF): 
        result = ":coupling:frequency {}".format(on_off.get_string())
        return cmdObj(result)

    def query_freq_deviation_on_off(self): 
        result = ":coupling:frequency?"
        return cmdObj(result)

    def set_coupling_phase_deviation(self , ph_dev): 
        if(ph_dev > 360 or ph_dev < 0): 
            raise Exception("phase deviation should be between 0 and 360")

        result = ":coupling:phase:deviation {}".format(ph_dev)
        return cmdObj(result)

    def query_coupling_phase_deviation(self): 
        result = ":coupling:phase:deviation?"
        return cmdObj(result)

    def set_coupling_phase_on_off(self , on_off:definitions.ON_OFF): 
        result = ":coupling:phase {}".format(on_off.get_string())
        return cmdObj(result)
    
    def query_coupling_phase_on_off(self): 
        result = ":coupling:phase?"
        return cmdObj(result)

    def set_coupling_on_off(self , on_off:definitions.ON_OFF): 
        result = ":coupling {}".format(on_off.get_string())
        return cmdObj(result)
    
    def query_coupling_on_off(self): 
        result = ":coupling?"
        return cmdObj(result)

    
    def identify_device(self): 
        return cmdObj("*idn?")

    def recall_user_profile(self , user:definitions.USERS):
        result = "*rcl {}".format(user.get_string())
        return cmdObj(result)

    def factory_reset(self): 
        return cmdObj("*rst")

    def save_current_state_to_user(self , user:definitions.USERS): 
        result = "*sav {}".format(user.get_string())
        return cmdObj(result)

    def trig_to_generate(self): 
        """
            This command is only available when Sweep or Burst is enabled (refer to the 
            [:SOURce<n>]:SWEep:STATe OFF|ON or [:SOURce<n>]:BURSt[:STATe] ON|OFF command) 
            and the trigger source is set to manual (refer to the [:SOURce<n>]:SWEep:TRIGger:SOURce 
            INTernal|EXTernal|MANual or [:SOURce<n>]:BURSt:TRIGger:SOURce INTernal|EXTernal|MANual command).
        """
        return cmdObj("*trg")

    def delete_memory_state(self , user:definitions.USERS): 
        """
            Delete the state file stored in the specified storage location.
        """

        result = ":memory:state:delete {}".format(user.get_string())
        return cmdObj(result)

    def lock_memory_state(self , user:definitions.USERS): 
        """
            Lock or unlock the file stored in the specified storage location.
            Query whether the file stored in the specified storage location is locked.
        """ 
        result = ":memory:state:lock {}".format(user.get_string())
        return cmdObj(result)

    def query_lock_memory_state(self , user:definitions.USERS): 
        result = ":memory:state:lock? {}".format(user.get_string())
        return cmdObj(result)

    def query_memory_state_valid(self , user:definitions.USERS): 
        result = ":memory:state:valid? {}".format(user.get_string())
        return cmdObj(result)

    
    ############ OUPTUT COMMANDS ##############
    def set_output_impedance(self , ch:definitions.CHANNELS , output_imp): 
        print("1{}".format(type(output_imp) == type(definitions.OUTPUT_IMPEDANCES.INFINITY)))
        print(type(output_imp))
        print(type(definitions.OUTPUT_IMPEDANCES.INFINITY))
        print(inspect.getmodule(type(output_imp)))
        print(inspect.getmodule(type(definitions.OUTPUT_IMPEDANCES.INFINITY)))
        if(isinstance(output_imp, int) or isinstance(output_imp , float)): 
            if(output_imp < 1 or output_imp > 10000): 
                raise Exception("Arguent out of range: output_imp should be between 1 and 10000")
            imp_str = "{}".format(output_imp)
        
        elif(isinstance(output_imp , definitions.OUTPUT_IMPEDANCES)): 
            imp_str = "{}".format(output_imp.get_string())
        else: 
            raise Exception("Invalid argument: output impedance should be int, float or OUTPUT_IMPEDANCE")
        
        result = ":output{}:impedance {}".format(ch.value , imp_str)
        return cmdObj(result)

    def query_output_impedance(self , ch:definitions.CHANNELS): 
        result = ":output{}:impedance?".format(ch.value)
        return cmdObj(result)

    
    def set_output_load(self , ch:definitions.CHANNELS , output_imp): 
        return self.set_output_impedance(ch , output_imp)

    def query_output_load(self , ch:definitions.CHANNELS): 
        return self.query_output_impedance(ch)

    def set_output_noise_scale(self , ch:definitions.CHANNELS , scale):
        if(isinstance(scale , int)): 
            scl_string = "{}".format(int)
        elif(isinstance(scale , definitions.OUTPUT_NOISE_SCALE)): 
            scl_string = scale.get_string()
        
        else: 
            raise Exception("Invalid argument: noise scale should be int or OUTPUT_NOISE_SCALE")

        result = ":output{}:noise:scale {}".format(ch.value , scl_string)
        return cmdObj(result )

    def query_output_noise_scale(self , ch:definitions.CHANNELS): 
        result = ":output{}:noise:scale?"
        return cmdObj(result)

    def set_output_noise_on_off(self , ch:definitions.CHANNELS , on_off:definitions.ON_OFF): 
        result = ":output{}:noise {}".format(ch.value , on_off.get_string())
        return cmdObj(result)

    def query_output_noise_on_off(self , ch:definitions.CHANNELS): 
        result = ":output{}:noise?".format(ch.value)
        return cmdObj(result)

    
    def set_output_polarity(self): 
        raise Exception("func not implemented")

    def set_output_on_off(self , ch:definitions.CHANNELS , on_off: definitions.ON_OFF): 
        result = ":output{}:state {}".format(ch.value , on_off.get_string())
        return cmdObj(result)

    def query_output_on_off(self , ch:definitions.CHANNELS): 
        result = ":output{}:state?".format(ch.value)
        return cmdObj(result)

    
    def set_output_sync_polarity(self): 
        raise Exception("func not implemented")
    def query_output_sync_polarity(self): 
        raise Exception("func not implmeneted")


    ##################### SOURCE COMMANDS #####################

    def __prepare_nested_func_args(self ,freq , 
                                        freq_min_max, 
                                        amp , 
                                        offset , 
                                        phase, 
                                        phase_min_max):

        result = ""
        if(freq != None): 
            if(freq < freq_min_max[0] or freq > freq_min_max[1]): 
                raise Exception("Arg out of range: frequency should be between {}Hz and {}Hz".format(freq_min_max[0],freq_min_max[1]))
            result += " {}".format(freq)

            if(amp != None):
                result += ",{}".format(amp)

                if(offset != None): 
                    result += ",{}".format(offset)

                    if(phase != None): 
                        if(phase < phase_min_max[0] or phase > phase_min_max[1]): 
                            raise Exception("Arg out of range: phase should be between {} and {}".format(phase_min_max[0] , phase_min_max[1]))
                        result += ",{}".format(phase)


        if(freq == None and (amp != None or offset != None or phase != None)): 
            raise Exception("Useless argument")
        if(amp == None and (offset != None or phase != None)): 
            raise Exception("Useless argument")
        if(offset == None and phase != None): 
            raise Exception("Useless argument")

        return result

    def apply_custom_output(self,
                            ch:definitions.CHANNELS,
                            freq=None,
                            amp=None,
                            offset=None,
                            phase=None):
        """
            sets a custom waveform to the output
            amplitude and offset cannot be checked statically: 
            amp depends on impedance and frequency/period settings 
            offset depends on impedance and amplitude/high level settings
        """ 
        result = ":source{}:apply:custom".format(ch.value)
        
        result += self.__prepare_nested_func_args(freq , [0.000001 , 40000000],amp , offset , phase , [0,360])
        
        return cmdObj(result)
    
    def apply_output_harmonic(self): 
        raise Exception("func not implemented")
    def apply_output_noise(self): 
        raise Exception("func ont impolemented")

    def apply_output_pulse(self , ch:definitions.CHANNELS , freq=None , amp=None , offset=None , delay=None): 
        """
            output a pulse with specified frequency, amplitude, dc offset and delay
        """
        result = ":source{}:apply:pulse".format(ch.value)
            
        result += self.__prepare_nested_func_args(freq , [0.000001 , 40000000] , amp ,  offset , delay , [0 , 1/freq])

        return cmdObj(result)

    def apply_output_ramp(self , ch:definitions.CHANNELS , freq=None , amp=None , offset=None,phase=None): 
        result = ":source{}:apply:ramp".format(ch.value)
        result += self.__prepare_nested_func_args(freq , [0.000001 , 4000000] , amp , offset , phase , [0,360])
        return cmdObj(result)

    def apply_output_sine(self , ch:definitions.CHANNELS , freq=None , amp=None , offset=None , phase=None):
        result = ":source{}:apply:sin".format(ch.value)
        result += self.__prepare_nested_func_args(freq , [0.000001 , 160000000] , amp , offset , phase , [0,360])
        return cmdObj(result)

    def apply_output_square(self , ch:definitions.CHANNELS , freq=None ,amp=None , offset=None , phase=None): 
        result = ":source{}:apply:squ".format(ch.value)
        result += self.__prepare_nested_func_args(freq , [0.000001 , 50000000],amp, offset , phase ,[0,360])
        return cmdObj(result)

    def apply_output_arb(self , ch:definitions.CHANNELS , freq=None , amp=None , offset=None , phase = None): 
        result = ":source{}:apply:user".format(ch.value)
        result += self.__prepare_nested_func_args(freq , [0.000001 , 40000000] , amp , offset , phase , [0,360])
        return cmdObj(result)

    def query_output_applied_func(self , ch:definitions.CHANNELS): 
        result = ":source{}:apply?".format(ch.value)
        return cmdObj(result)

    
    def set_source_freq(self , ch:definitions.CHANNELS , freq): 
       
        if(isinstance(freq, float) or isinstance(freq , int)): 
            str_freq = "{}".format(freq)
        elif(isinstance(freq , definitions.MINMAX)): 
            str_freq = freq.get_string()
        else: 
            raise Exception("Invalid argument")

        result =":source{}:freq {}".format(ch.value , str_freq)

        return cmdObj(result)

    
    def set_arb_stepbystep_mode(self, ch:definitions.CHANNELS): 
        """ 
            In step-by-step output mode, the generator calculates the frequency (30.517578125 kHz) of the output signal automatically according to the waveform length (16,384) and sample rate. The generator outputs waveform point by point at this fixed frequency. The step-by-step output mode can prevent the loss of important waveform points. 
            This command is only available when the arbitrary waveform function is enabled.
        """
        
        result = ":source{}:function:arb:step".format(ch.value)
        return cmdObj(result)

    def set_source_period(self , ch:definitions.CHANNELS , period): 
        """
            period range is defined by waveform type 
        """
        result = ":source{}:period {}".format(ch.value , period)
        return cmdObj(result)

    def query_source_period(self , ch:definitions.CHANNELS): 
        result = ":source{}:period?".format(ch.value)
        return cmdObj(result)

    def set_source_phase(self , ch:definitions.CHANNELS , phase): 
        if(isinstance(phase , definitions.MINMAX)): 
            ph_str = phase.get_string()
        elif(isinstance(phase , float)): 
            if(phase < 0 or phase > 360): 
                raise Exception("Arg out of range: phase should be between 0 and 360")
            ph_str = str(float)
        result = ":source{}:phase {}".format(ch.value , ph_str)

        return cmdObj(result) 
    
    def query_source_phase(self , ch:definitions.CHANNELS): 
        result = ":source{}:phase?".format(ch.value)
        return cmdObj(result)

    def exec_align_phase(self , ch:definitions.CHANNELS): 
        result = ":source{}:phase:init".format(ch.value)
        return cmdObj(result)

    def set_pulse_dcycle(self , ch:definitions.CHANNELS , percent): 
        if(isinstance(percent , float)): 
            if(percent < 0 or percent > 100): 
                raise Exception("Arg out of range: percent should be between 0 and 100")
            percent_str = str(percent)

        elif(isinstance(percent , definitions.MINMAX)): 
            percent_str = percent.get_string()

        result = ":source{}:pulse:dcycle {}".format(ch.value , percent_str)
        return cmdObj(result)
    
    def query_pulse_dcycle(self , ch:definitions.CHANNELS): 
        result = ":source{}:pulse:dcycle?".format(ch.value)
        return cmdObj(result)

    def set_pulse_delay(self , ch:definitions.CHANNELS , delay): 
        if(isinstance(delay,float)): 
            del_str = str(delay)
        elif(isinstance(delay , definitions.MINMAX)): 
            del_str = delay.get_string()

        result = ":source{}:pulse:delay {}".format(ch.value , del_str)
        return cmdObj(result)
    
    def query_pulse_delay(self , ch:definitions.CHANNELS): 
        result = ":source{}:pulse:delay?".format(ch.value)
        return cmdObj(result)

    def set_pulse_width_or_dcycle(self, ch:definitions.CHANNELS , wd:definitions.PULSE_WIDTH_OR_DUTY): 
        result = ":source{}:pulse:hold {}".format(ch.value , wd.get_string())
        return cmdObj(result)

    def query_pulse_width_or_dcycle(self , ch:definitions.CHANNELS): 
        result = ":source{}:pulse:hold?".format(ch.value)
        return cmdObj(result)

    def set_pulse_width(self , ch:definitions.CHANNELS , pw): 
        if(isinstance(pw , float)): 
            pw_str = str(pw)
        elif(isinstance(pw , definitions.MINMAX)): 
            pw_str = pw.get_string()

        result = ":source{}:pulse:width {}".format(ch.value , pw_str)
        return cmdObj(result)
    
    def query_pulse_width(self , ch:definitions.CHANNELS): 
        result = ":source{}:pulse:width?".format(ch.value)
        return cmdObj(result)


    def set_source_amplitude(self , ch:definitions.CHANNELS , amp): 
        if(isinstance(amp , float)): 
            str_amp = str(float)
        elif(isinstance(amp , definitions.MINMAX)): 
            str_amp = amp.get_string()

        result = ":source{}:voltage {}".format(ch.value , str_amp)

        return cmdObj(result)

    def query_source_amplitude(self , ch:definitions.CHANNELS): 
        result = ":source{}:voltage?".format(ch.value)
        return cmdObj(result)


    def set_voltage_high_value(self , ch:definitions.CHANNELS , voltage): 
        result = ":source{}:voltage:HIGH {}".format(ch.value , voltage)
        return cmdObj(result)

    def set_voltage_low_value(self , ch:definitions.CHANNELS , voltage): 
        result = ":source{}:voltage:LOW {}".format(ch.value , voltage)
        return cmdObj(result)

    def query_voltage_high_value(self , ch:definitions.CHANNELS): 
        result = ":source{}:voltage:HIGH?".format(ch.value)
        return cmdObj(result)

    def query_voltage_low_value(self , ch:definitions.CHANNELS): 
        result = ":source{}:voltage:LOW?".format(ch.value)
        return cmdObj(result)

    def set_source_offset(self , ch:definitions.CHANNELS , offset): 
        if(isinstance(offset , float)): 
            off_str = str(offset)
        elif(isinstance(offset , definitions.MINMAX)): 
            off_str = offset.get_string()

        result = ":source{}:voltage:offset {}".format(ch.value , off_str)
        return cmdObj(result)
    
    def query_source_offset(self , ch:definitions.CHANNELS): 
        result = ":source{}:voltage:offset?".format(ch.value)
        return cmdObj(result)

    def query_system_error(self): 
        return cmdObj(":system:error?")
    
    def restore_system(self , user:definitions.USERS): 
        result = ":system:preset {}".format(user.get_string())
        return cmdObj(result)

    def restart_system(self): 
        result = ":system:restart"
        return cmdObj(result)
    
    def query_system_version(self): 
        result = ":system:version?"
        return cmdObj(result)


    ############################## LOADING ARB DATA #############
    # def __get_bytearray_data(self , data_points:list): 
    #     list_len = len(data_points)
    #     list_len_digit_count = len(str(list_len))
    #     header_str = "#{}{}".format(list_len_digit_count,list_len)

    #     byte_arr_header = bytearray()
    #     byte_arr_header.extend(map(ord , header_str))

    #     byte_arr_values = bytearray()
    #     for point in data_points: 

    def __find_digit_count(self , input_num): 
        digits = 1
        if(input_num < 0): 
            raise Exception("function works only for positive numbers")

        input_num = input_num // 10
        while(input_num > 0):
            input_num = input_num // 10
            digits += 1

        return digits
    
    

    def load_data_dac16(self , flag:definitions.DAC16_FLAGS , data_list): 
        """
            data points downloaded to the oscilloscope should exactly be 16384 , if data list has fewer elements, 
            it should be extended with zeros
        """
        out_len = 16384

        if(len(data_list) > out_len): 
            raise Exception("function not implememnted yet")
    
        ## The output length is constant
        byte_count = 2 * out_len
        digit_count = 5


        header = ":source1:data:dac16 volatile,{},#{}{}".format(flag.get_string(), digit_count , byte_count)
        # print(header)
        header_bytes = bytearray()
        header_bytes.extend(map(ord , header))

        ## byte range is within 0000 and 3FFF meaning 0 and 16183
        ## data list should be between -1 and 1
        hex_max = 0x3FFF

        step_size = 2 / 0x3FFF
        start_hex_range = 0x0000
        data_byte_array = bytearray()
        
        ## pad data list with zeros 
        pad_len = out_len - len(data_list)
        for _ in range(pad_len):
            data_list.append(0)

        for data in data_list:
        
            data_distance = data - (-1)
            steps_in_current_float = data_distance // step_size
            place_in_hex_range = int(start_hex_range + steps_in_current_float)
            if(place_in_hex_range > hex_max): 
                place_in_hex_range = hex_max

            high_hex = int(place_in_hex_range // 256)
            low_hex = int(place_in_hex_range - high_hex * 256)
            
            data_byte_array.append(high_hex)
            data_byte_array.append(low_hex)

        
        result = bytes(header_bytes + data_byte_array)
              
        return encodedCmdObj(result)

    def load_data_dac(self , data_list): 
        """
            data points downloaded to the oscilloscope should exactly be 16384 , if data list has fewer elements, 
            it should be extended with zeros
        """
        out_len = 16384

        if(len(data_list) > out_len): 
            raise Exception("function not implememnted yet")
    
        # The output length is constant
        byte_count = 2 * out_len
        digit_count = 5

        # byte_count = 2 * len(data_list)
        # digit_count = self.__find_digit_count(byte_count)

        header = ":source1:data:dac volatile,#{}{}".format(digit_count , byte_count)
        # print(header)
        header_bytes = bytearray()
        header_bytes.extend(map(ord , header))

        ## byte range is within 0000 and 3FFF meaning 0 and 16183
        ## data list should be between -1 and 1
        hex_max = 0x3FFF

        step_size = 2 / 0x3FFF
        start_hex_range = 0x0000
        data_byte_array = bytearray()
        
        # pad data list with zeros 
        pad_len = out_len - len(data_list)
        for _ in range(pad_len):
            data_list.append(0)

        for data in data_list:
        
            data_distance = data - (-1)
            steps_in_current_float = data_distance // step_size
            place_in_hex_range = int(start_hex_range + steps_in_current_float)
            if(place_in_hex_range > hex_max): 
                place_in_hex_range = hex_max

            high_hex = int(place_in_hex_range // 256)
            low_hex = int(place_in_hex_range - high_hex * 256)
            
            data_byte_array.append(high_hex)
            data_byte_array.append(low_hex)

        
        result = bytes(header_bytes + data_byte_array)
              
        return encodedCmdObj(result)


    
    def load_data_values(self , data_list):
        """
            Load float values to the device
            each data point should be between -1 and 1
        """
        # if(len(data_list) > 1470): 
        #     raise Exception("data with length {} too long for transmission, use batch function".format(len(data_list)))

        for data in data_list: 
            if(data > 1 or data < -1): 
                raise Exception("Data point out of range: data points should be between -1 and 1")
        
        if(len(data_list) > 16384): 
            raise Exception("No more than 16384 points can be downloaded at once")

        result = ":data volatile"
        for data in data_list:
            str_num = str(data).rstrip('0').rstrip('.') 
            # result = result + "," + str(data)
            result = result + "," + str_num

        return cmdObj(result)

    def load_data_values_in_batch(self , data_list , batch_len = 1400): 
        """
            return type is a list of commands
        """
        
        batch_count = len(data_list) // batch_len + 1 
        if(len(data_list) % batch_len == 0): 
            batch_count -= 1

        batch_list = []

        print(batch_count)

        header = ":data volatile"

        for i in range(batch_count): 
            batch_start = i * batch_len
            if((i+1)*batch_len >= len(data_list)): 
                batch_end = len(data_list)
            else: 
                batch_end = (i+1)*batch_len

            current_batch = data_list[batch_start : batch_end]
            current_batch_str = ""
            for value in current_batch: 
                current_batch_str += ",{}".format(value)

            if(i == 0): 
                current_batch_str = header + current_batch_str

            if(i < batch_count - 1):
                batch_list.append(batchedCmdObj(current_batch_str))
            else: 
                batch_list.append(batchedCmdObj(current_batch_str , end_of_batch= True))
            
        return batch_list
        
                

    def set_dac_interpolation_mode(self , mode:definitions.DAC_INTERP_MODES): 
        result = ":data:points:interpolate {}".format(mode.get_string())
        return cmdObj(result)

    def set_number_of_points(self , point_count): 
        if(isinstance(point_count , int)): 
            # if(point_count < 2 or point_count > 16384): 
            #     raise Exception("value out of range: point count can be between 2 and 16384")
            pt_cnt_str = str(point_count)
        elif(isinstance(point_count , definitions.MINMAX)): 
            pt_cnt_str = point_count.get_string()

        result = ":data:points volatile,{}".format(pt_cnt_str)

        return cmdObj(result)


    def set_points_index_value_type(self , input_list): 
        if(len(input_list) == 0): 
            raise Exception("point list empty")
        result = ":data:value volatile"
        for idx , val in enumerate(input_list): 
            result += "," + str(idx + 1) + "," + str(val)

        return cmdObj(result)

    def query_number_of_points(self): 
        result = ":data:points? volatile"
        return cmdObj(result)

    def query_volatile_point_value(self , index): 
        index = int(index)
        if(index < 1 or index > 16384): 
            raise Exception("Index out of range: point index should be between 1 and 16384")

        result = ":data:value? volatile,{}".format(index)
        return cmdObj(result)

    def mod_point_value_volatile_mem(self , index , new_value): 
        """
            The function only available when the current output waveform is 
            volatile
        """
        index = int(index)
        new_value = int(new_value)
        
        result = ":data:value volatile,{},{}".format(index , new_value)
        return cmdObj(result)

    def query_volatile_arb_wave_count(self): 
        result = ":data:load? volatile"
        return cmdObj(result)

    

    def is_operation_complete(self): 
        result = "*OPC?"
        return cmdObj(result)

    def clear_status_register(self): 
        result = "*CLS"
        return cmdObj(result)

    def set_operation_complete(self): 
        result = "*OPC"
        return cmdObj(result)



    def query_status_register(self): 
        result = "*ESR?"
        return cmdObj(result)