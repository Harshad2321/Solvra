"""Debug logic puzzle truth table"""

from itertools import product

# P: "Exactly one of us is a knight"
# Q: "P is a knave"
# R: "Q is a knave"

print("Testing all 8 combinations:")
print("=" * 60)

for p_type, q_type, r_type in product([0, 1], repeat=3):
    # P says: "Exactly one of us is a knight"
    p_statement = (p_type + q_type + r_type == 1)
    p_consistent = (p_type == 1 and p_statement) or (p_type == 0 and not p_statement)
    
    # Q says: "P is a knave"
    q_statement = (p_type == 0)
    q_consistent = (q_type == 1 and q_statement) or (q_type == 0 and not q_statement)
    
    # R says: "Q is a knave"
    r_statement = (q_type == 0)
    r_consistent = (r_type == 1 and r_statement) or (r_type == 0 and not r_statement)
    
    p_name = "Knight" if p_type == 1 else "Knave"
    q_name = "Knight" if q_type == 1 else "Knave"
    r_name = "Knight" if r_type == 1 else "Knave"
    
    print(f"P={p_name}, Q={q_name}, R={r_name}: ", end="")
    print(f"P_ok={p_consistent}, Q_ok={q_consistent}, R_ok={r_consistent}", end="")
    
    if p_consistent and q_consistent and r_consistent:
        print(" ✓ VALID!")
    else:
        print()
