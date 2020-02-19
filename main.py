"""
var = "loss:0.7454438183786545, accuracy:0.5572354197502136, binary_crossentropy:0.7007483839988708, f1_m:0.403618186712265, precision_m:0.651948094367981, recall_m:0.32348015904426575"


elems = var.split(",")

elems = [float(xi.split(":")[1]) for xi in elems]
print(elems)

res = '|'.join([f"{xi:.4f}" for xi in elems])
print("|"+res+"|")
"""

def create_line_for_table(seq_len, ii, var):
  
  elems = var.split(",")
  elems = list(filter(lambda xi: xi.strip().startswith("binary_crossentropy") is False, elems))
  elems = [float(xi.split(":")[1]) for xi in elems]
  print(ii, elems)
  res = '|'.join([f"{xi:.4f}" for xi in elems])
  return f'|{seq_len}|{res}|\n'


with open("input.txt", "r") as f:
  content = f.read().split("\n")
  n_lines = len(content)
  content = content[:n_lines-1]
  print("No. lines:", len(content))

# res = list(map(lambda item: create_line_for_table(item[0], item[1]), enumerate(content)))

seq_len = 7000 # 5000, 7000, 15000
res = list(map(lambda item: create_line_for_table(seq_len, item[0], item[1]), enumerate(content)))

with open("out.txt", "w") as f:
  f.writelines(res)