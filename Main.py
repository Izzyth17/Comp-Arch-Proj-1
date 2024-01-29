from CPU import CPU
from Instruction import Instruction

NOOP = 0
ADD = 1
ADDI = 2
BEQ = 3
JAL = 4
LW = 5
SW = 6
RETURN = 7

def build_instruction(opcode, Rd, Rs1, Rs2, immed):
    instr = opcode << 28
    if Rd is not None:
        instr = instr + (Rd << 24)
    if Rs1 is not None:
        instr = instr + (Rs1 << 20)
    if Rs2 is not None:
        instr = instr + (Rs2 << 16)
    if immed is not None:
        instr = instr + immed
    return instr

cpu = CPU()
print(cpu.regs[1])


i0 = build_instruction(NOOP, None, None, None, None)
i1 = build_instruction(ADDI, cpu.regs[1], cpu.regs[0], None, 8)
i2 = build_instruction(ADDI, cpu.regs[2], cpu.regs[0], None, 7)
i3 = build_instruction(ADD, cpu.regs[3], cpu.regs[1], cpu.regs[1], None)
i4 = build_instruction(ADD, cpu.regs[4], cpu.regs[2], cpu.regs[2], None)
i5 = build_instruction(BEQ, None, cpu.regs[3], cpu.regs[4], 3)
i6 = build_instruction(ADDI, cpu.regs[8], cpu.regs[0], None, 10)
i7 = build_instruction(JAL, cpu.regs[0], None, None, 2)
i8 = build_instruction(ADDI, cpu.regs[8], cpu.regs[0], None, 1000)
i9 = build_instruction(SW, None, cpu.regs[2], cpu.regs[8], 16)
i10 = build_instruction(LW, cpu.regs[5], cpu.regs[8], None, 16)
i11 = build_instruction(RETURN, None, None, None, None)

print(i0)

cpu.memory[100] = i0
cpu.memory[101] = i1
cpu.memory[102] = i2
cpu.memory[103] = i3
cpu.memory[104] = i4
cpu.memory[105] = i5
cpu.memory[106] = i6
cpu.memory[107] = i7
cpu.memory[108] = i8
cpu.memory[109] = i9
cpu.memory[110] = i10
cpu.memory[111] = i11

cpu.pc = 100