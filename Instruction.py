class Instruction:
    def __init__(self, opcode, Rd, Rs1, Rs2, immed):
        self.opcode = opcode
        self.Rd = Rd
        self.Rs1 = Rs1
        self.Rs2 = Rs2
        self.immed = immed