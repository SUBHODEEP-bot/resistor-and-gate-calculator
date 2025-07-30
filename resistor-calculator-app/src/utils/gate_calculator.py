# src/utils/gate_calculator.py

def calculate_logic_gate(gate_type, input1, input2=None):
    if gate_type == "NOT":
        return not input1
    elif gate_type == "AND":
        return input1 and input2
    elif gate_type == "OR":
        return input1 or input2
    elif gate_type == "NAND":
        return not (input1 and input2)
    elif gate_type == "NOR":
        return not (input1 or input2)
    elif gate_type == "XOR":
        return input1 != input2
    elif gate_type == "XNOR":
        return input1 == input2
    else:
        return None
