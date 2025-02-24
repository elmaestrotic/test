import disassembler

import dis
def main():
  tabla=8
  for i in range (1,11):
    resul =tabla *i
    print(tabla," x ", i," = ",resul)

dis.dis(main)
   
disassembler.disassemble(main)