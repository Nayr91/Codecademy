class Memory:
    def __init__(self):
        self.memory_storage = [0, 0, 0, 0, 0, 0
                               0, 0, 0, 0, 0, 0
                               0, 0, 0, 0, 0, 0
                               0, 0, 0, 0, 0, 0
                               ]
        self.memory_no = 0
        
    def to_add(self, num):
        self.memory_storage[self.memory_no] = num
        self.memory_no += 1
        return


class CPU:
    def __init__(self):
        self.cache = [{ "r1" : None},
                      { "r2" : None},
                      { "r3" : None},
                      { "r4" : None}]
        self.instruction_list = {"ADD" : None, "ADDI": None, "SUB": None, 
                                 "SLT": None, "BNE": None, "J": None, 
                                 "JAL": None, "LW": None, "SW": None,
                                 "CACHE": None, "HALT": None}
            
    def read_inst(self, instr):
        outp = None
        if instr in self.instruction_list:
            outp = self.instruction_list[instr]
        
    def execute_instr(self, num):
        