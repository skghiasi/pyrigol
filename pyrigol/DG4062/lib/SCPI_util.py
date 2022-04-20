from base64 import encode
import enum 

class RigolCmdObj: 
    """
        command object to hold command information: 
            - command string 
            - needs answer or not 
            - parsed answer (by setting a proper command parser)
    """
    

    def __init__(self , cmd_string): 
        self.__answer = ""
        self.__parser = None 
        self.__active_channel_for_cmd = None 

        ## if scpi command has '?' in the end, it needs answer
        cmd_string = cmd_string.strip()

        # if(cmd_string[-1] == '?'): 
        #     self.__needs_answer = True

        if('?' in cmd_string): 
            self.__needs_answer = True
            
        else: 
            self.__needs_answer = False 
        
        self.__cmd = cmd_string + '\n' 
        


    def needs_answer(self): 
        """ 
            returns True if the device sends a response to the message
            returns False if the device does not send anything back
        """
        return self.__needs_answer

    def get_cmd(self , encoded = False):
        """
            @return The string of the command
        """
        if(not encoded):
            return self.__cmd
        
        assert 1 == 0, "encoding not implemented yet"

    def set_answer(self , answer:str): 
        """
            Attaches the response received from the device to the command, used to keep track of the answers
        """
        self.__answer = answer 
        # self.__parser = ScpiRespParser(self.get_cmd() , self.__answer)


    def get_answer(self): 
        return self.__answer

    # def get_parser(self): 
    #     return self.__parser

    # def set_active_channel(self , active_channel): 
    #     self.__active_channel_for_cmd = active_channel

# class batchedCmdObj(cmdObj): 
#     def __init__(self , str_cmd  , end_of_batch = False):
#         super().__init__("no string")
#         self.__cmd = str_cmd
#         if(end_of_batch): 
#             self.__cmd += '\n'

#         ## can also implement if the code needs answer or not 
#         ## pass 
        
    
#     def get_cmd(self): 
#         return self.__cmd 


    

# class encodedCmdObj(cmdObj): 
#     def __init__(self , cmd):         
#         super(encodedCmdObj , self).__init__("no string")
#         cmd_barr:bytearray = bytearray(cmd) 
#         cmd_barr.append(ord('\n'))
#         cmd = bytes(cmd_barr)        
#         self._mock_cmd = self.emulate_str(cmd)

#     def get_cmd(self): 
#         return self._mock_cmd

#     class emulate_str: 
#         def __init__(self , mock_str): 
#             self._mock_str = mock_str
#             pass 

#         def encode(self): 
#             return self._mock_str

#         def lower(self):
#             my_str:str = self.__str__()
#             return my_str.lower()

#         def __str__(self): 
#             output_str = ""
#             # sharp_index = output_str.index('#')
#             sharp_index = self._mock_str.index(ord('#'))
           
#             data_counter_digits = int(self._mock_str[sharp_index + 1]) - 48
#             end_str_idx = sharp_index + 1 + data_counter_digits + 1
#             string_part = self._mock_str[0:end_str_idx]
#             output_str = str(string_part)

#             ## prepare the binary block for printing: 
#             for  bite in self._mock_str[end_str_idx :]: 
#                 output_str += ",{:x}".format(bite)

#             # return str(self._mock_str)
#             return output_str

class ScpiRespParser: 
    class answer_types(enum.Enum): 
        FLOAT_LIST = 0 
        INT_LIST = 1
        BYTE = 2
    
    def __init__(self , cmd_string , answer_bytes): 
        self._cmd_string = cmd_string 
        self._answer_bytes = answer_bytes
         

    def parse(self): 
        cmd:str = self._cmd_string
        parsed_answer = None 
        answer_type = None 

        if(cmd.lower() == "*esr?\n"): 
            answer_type = self.answer_types.BYTE
            parsed_answer = self._answer_bytes[0] - 48
        
        return [answer_type , parsed_answer]


    

    