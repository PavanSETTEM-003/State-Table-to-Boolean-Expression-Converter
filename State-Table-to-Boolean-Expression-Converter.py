#%%
from tabulate import tabulate

import tkinter as tk
from tkinter import messagebox


def display(state_table):
  for i in state_table:
    print(i)

def generate_state(no_of_states):
  states = []
  for i in range(no_of_states):
    states.append("{0:b}".format(i))

  #beautify
  print("original",states)
  maxi = len("{0:b}".format(no_of_states-1))

  for i in range(len(states)):
    zeros = maxi - len(str(states[i]))
    states[i] = "0"*zeros + str(states[i])


  return states

def generate_state_table(states):
  #notations
  no_of_state_notations = 0
  while(len(states) > 2**no_of_state_notations):
    no_of_state_notations += 1
    
  notations = [chr(i+65) for i in range(no_of_state_notations)]

  state_table = [["" for j in range(3)] for i in range(len(states)+2)]


  state_table[0][0] = "Present state"
  state_table[0][1] = "Next state"
  state_table[0][2] = "Output"

  state_table[1][0] = notations
  state_table[1][1] = "[x=0, x=1]"
  state_table[1][2] = "[x=0, x=1]"

  return state_table

def call_by_index(states):
  index = 1
  data = []

  for i in states:
    ref = [[j for j in i],[],[]]
    for present_state in range(2):
      print("The next state of "+str(i)+" when input was x = "+str(present_state))
      ref[1].append(states[int(input())])
      ref[2].append(int(input()))
      
    state_table.loc[index] = ref
    index += 1
    data.append(ref)

  return data

def call_by_states(states):
  index = 2
  for i in states:
    ref = [[j for j in i],[],[]]
    for present_state in range(2):
      print("The next state of "+str(i)+" when input was x = "+str(present_state))
      ref[1].append(input())
      ref[2].append(input())

    state_table[index] = ref
    index += 1

def flip_flop_selction(ff):
  if("t" in ff):
    print("T Flip flop")
    flip_flop = [ ["Qn","Qn+1","T"] , ["0","0", ["0"] ] , ["0","1", ["1"] ] , ["1","0", ["1"] ] , ["1","1", ["0"] ] ]
    print(tabulate(flip_flop,tablefmt="fancy_grid"))

  elif ("jk" in ff ):
    flip_flop = [ ["Qn","Qn+1","J K"] , ["0","0",["0","X"]] , ["0","1",["1","X"]] , ["1","0",["X","1"]] , ["1","1",["X","0"]] ]
    print("traditional JK flipflop")
    print(tabulate(flip_flop,tablefmt="fancy_grid"))

    print("we will consider X (dont care) as '1', which helps in solving K-map better") 
    print()

  elif("d" in ff):
    flip_flop = [[]]

  return flip_flop

def generate_rules(flip_flop):
  rules = {}
  for i in range(1,len(flip_flop)):
    ref = str(flip_flop[i][0]) + str(flip_flop[i][1])
    if ref not in rules:
      rules[ref] = flip_flop[i][-1]
  
  return rules

def generate_circuit_excitation_table(state_table, flip_flop, flip_flop_type):

  circuit_excitation_table = [ [0 for j in range(5)] for i in range(2*(len(state_table)-2) + 2)]
  circuit_excitation_table[0] = ["Present State", "Input","Output", "Next state", "Filp flop"]

  if("t" in flip_flop_type):
    exp = len(state_table[1][0])
    res = []
    for i in range(exp):
      res.append("T"+chr(97+i))
    circuit_excitation_table[1] = [state_table[1][0], "X","Y", state_table[1][0], res]
    
  else:
    exp = len(state_table[1][0])
    res = []
    for i in range(exp):
      res.append("J"+chr(97+i))
      res.append("K"+chr(97+i))
    circuit_excitation_table[1] = [state_table[1][0], "X","Y", state_table[1][0],res]
    

  


  ## copying data from the state tables to the circuit_excitation_table format
  index = 2
  circuit_index = 2

  for i in range(2,len(state_table)):
    for j in range(2):
      ref = []
      ref.append(state_table[index][0])
      ref.append(0) if(j==0) else ref.append(1)
      ref.append(state_table[index][-1][0]) if(j==0) else ref.append(state_table[index][-1][1])
      ref.append(state_table[index][1][0]) if(j==0) else ref.append(state_table[index][1][1])

      circuit_excitation_table[circuit_index] = ref
      circuit_index += 1
    
    index += 1
  
  ## generating rules based on the flip flop condition
  rules = generate_rules(flip_flop)
  

  ## logic
  for i in range(2,len(circuit_excitation_table)):
    ref = []
    index = 0
    for j in range(len(circuit_excitation_table[i][0])): 
      condition = circuit_excitation_table[i][0][index] + circuit_excitation_table[i][3][index]
      result = rules[condition]
      for z in result:  ref.append(z)
      index += 1

    circuit_excitation_table[i].append(ref)

  
  
  ##display(circuit_excitation_table)

  return circuit_excitation_table

def one_bit_difference(n1,n2):         # looking for the prime implicants
  one_bit_flag = 0
  for i in range(len(n1)):
    if(n1[i]!=n2[i]):
      one_bit_flag += 1
      if(one_bit_flag>1): return False
  return True

def nomenclature(n):                   # naming for the boolean equation
  s = [chr(65+i) for i in range(len(n)-1)]
  expression = ""
  for i in range(len(n)-1):
    if(n[i]=="1"):  expression += s[i]
    elif(n[i]=="_"):  continue
    else: expression += s[i]+chr(39)
  if(n[-1]!="_"):
    if(n[-1]=="1"): expression += "x" 
    else: expression += "x"+chr(39)          ## x for the indication of input
  return expression

def generate_groups(flip_flop_high):
  groups = {}
  for i in flip_flop_high:
    ones = i.count("1")
    if(ones not in groups):
      groups[ones] = [i]
    else: groups[ones].append(i)
  
  groups = dict(sorted(groups.items()))
  return groups  

def approach(flip_flop_high):
  groups = generate_groups(flip_flop_high) 
  
  left_over = []
  present_bit_difference = True

  cache_memory = list(groups.values())
  cache_memory_keys = []
  cache_memory_pair_status = [ [0 for val in sublist] for sublist in cache_memory ]

  for i in range(len(cache_memory)):
    res = []
    for j in range(len(cache_memory[i])):
      res.append(int(str(cache_memory[i][j]),2))
    cache_memory_keys.append(res)
  
  while(present_bit_difference==True):
    present_bit_difference = False
    holder = []

    for i in range(len(cache_memory)-1):
      res = []
      for a in range(len(cache_memory[i])):
        for b in range(len(cache_memory[i+1])):
          if(one_bit_difference( cache_memory[i][a] , cache_memory[i+1][b] )):

            present_bit_difference = True
            cache_memory_pair_status[i][a] , cache_memory_pair_status[i+1][b] = 1 , 1
            name = str(cache_memory_keys[i][a]) + " - " + str(cache_memory_keys[i+1][b])
            result = ""
            for z in range(len(cache_memory[i][a])):
              if cache_memory[i][a][z] == cache_memory[i+1][b][z]:
                  result += cache_memory[i][a][z]
              else:
                  result += "_"

            res.append([name , result])
      
      holder.append(res)
      
    
    for i in range(len(cache_memory_pair_status)):
      for j in range(len(cache_memory_pair_status[i])):
        if( cache_memory_pair_status[i][j] == 0):
          left_over.append([ cache_memory_keys[i][j], cache_memory[i][j] ])
    
    
    cache_memory = []
    cache_memory_keys = []

    for i in range(len(holder)):
      res = []
      res_keys = []
      for j in range(len(holder[i])):
        res.append(holder[i][j][1])
        res_keys.append(holder[i][j][0])

      cache_memory.append(res)
      cache_memory_keys.append(res_keys)
    cache_memory_pair_status = [ [0 for val in sublist ] for sublist in cache_memory ]


  # print("left_over = ",left_over)
  return left_over

def generate_prime_implicants(prefinal_prime_implicants, dont_care_positions):
  # print(prefinal_prime_implicants)
  for i in range(len(prefinal_prime_implicants)):
    prefinal_prime_implicants[i][0] = sorted(list(int(n) for n in str(prefinal_prime_implicants[i][0]).split(" - ")))
    ref = prefinal_prime_implicants[i][0]
    prefinal_prime_implicants[i][0] = []
    for j in ref:
      if(j not in dont_care_positions): prefinal_prime_implicants[i][0].append(j)
  
  duplicates = []
  for i in prefinal_prime_implicants:
    if i not in duplicates:
      duplicates.append(i)
  
  prefinal_prime_implicants = duplicates
    
  d = {}
  for i in range(len(prefinal_prime_implicants)):
    for j in prefinal_prime_implicants[i][0]:
      if(j not in d):
        d[j] = 1
      else:
        d[j] += 1

  result = ""
  for i in range(len(prefinal_prime_implicants)):
    for j in prefinal_prime_implicants[i][0]:
      if(d[j]==1):
        result += nomenclature(prefinal_prime_implicants[i][1]) + " + "
        break
    
  return(result[0:-2])

def generate_boolean_expression(circuit_excitation_table):
  result = []
  flip_flop_boolen_expresssion = len(circuit_excitation_table[1][-1])
  

  ## looking over the high states in the flip flop
  flip_flop_bit = 0
  for _ in range(flip_flop_boolen_expresssion):
    flip_flop_high = []
    dont_care_positions = []
  
    for i in range(2,len(circuit_excitation_table)):
      if(circuit_excitation_table[i][-1][flip_flop_bit] == "1" or circuit_excitation_table[i][-1][flip_flop_bit] == "X"):
        flip_flop_high.append(str(circuit_excitation_table[i][0]) + str(circuit_excitation_table[i][1]))
        if(circuit_excitation_table[i][-1][flip_flop_bit] == "X"):  dont_care_positions.append(i-2)
    
    # print("Filp flop high = ",flip_flop_high,dont_care_positions)
    final_prime_implicants = generate_prime_implicants(approach(flip_flop_high), dont_care_positions)

    result.append([circuit_excitation_table[1][-1][flip_flop_bit],final_prime_implicants])
    # print(circuit_excitation_table[1][-1][flip_flop_bit]+" = ",final_prime_implicants)
    # print("-----------------------------------------------------------------------------------")

    flip_flop_bit += 1

  ##boolean exp fot the output y
  output = []
  for i in range(2,len(circuit_excitation_table)):
    if(circuit_excitation_table[i][2] == ("1")):
      output.append(str(circuit_excitation_table[i][0]) + str(circuit_excitation_table[i][1]))
  
  result.append(["Output 'Y' = ",generate_prime_implicants(approach(output),[])])
  # print("Output 'Y' = ",generate_prime_implicants(approach(output),[]))

  
  return result



def mygui(n, states):
    user_inputs = []
    ref = []
    
    def submit():
        nonlocal user_inputs
        nonlocal ref
        
        for i in range(2,n+2):
            user_inputs = [[j for j in states[i-2]], [], []]
            user_inputs[1].append(input_list[i-2][0].get())
            user_inputs[2].append(input_list[i-2][1].get())
            user_inputs[1].append(input_list[i-2][2].get())
            user_inputs[2].append(input_list[i-2][3].get())
            
            ref.append(user_inputs)
            
        messagebox.showinfo("Info", "Inputs saved successfully")
        root.destroy()

    root = tk.Tk()
    root.title("State Diagram to Boolean Expression Generator")
    
    label = tk.Label(root, text="PROVIDE THE INPUTS")
    label.pack(padx= 100)
    
    frame = tk.Frame(root,padx=20,pady=20)
    frame.columnconfigure(0,weight=2)
    frame.columnconfigure(1,weight=2)
    frame.columnconfigure(2,weight=2)
    frame.columnconfigure(3,weight=2)
    
    label = tk.Label(frame,text="input x = 0").grid(row=0,column=1)
    label = tk.Label(frame,text="input x = 1").grid(row=0,column=3)
    
    label = tk.Label(frame,text=" Present State ").grid(row=1,column=0)
    label = tk.Label(frame,text=" Next State ").grid(row=1,column=1)
    label = tk.Label(frame,text=" Output ").grid(row=1,column=2)
    
    label = tk.Label(frame,text=" Next State ").grid(row=1,column=3)
    label = tk.Label(frame,text=" Output ").grid(row=1,column=4)
    
    input_list = []
    for i in range(2,n+2):
        label = tk.Label(frame,text=states[i-2]).grid(row=i,column= 0)
        input_1 = tk.Entry(frame)
        input_2 = tk.Entry(frame)
        input_3 = tk.Entry(frame)
        input_4 = tk.Entry(frame)
        input_1.grid(row=i,column=1)
        input_2.grid(row=i,column=2)
        input_3.grid(row=i,column=3)
        input_4.grid(row=i,column=4)
        input_list.append([input_1, input_2, input_3, input_4])
        
    check_status_c1 = tk.IntVar()
    check_status_c2 = tk.IntVar()
    flip_flop = ""
    
    label = tk.Label(frame,text="Select Flip Flop: ").grid(row=n+3,column=1)
    c1 = tk.Checkbutton(frame,text="JK flip flop",variable=check_status_c1).grid(row=n+3,column=2)
    c2 = tk.Checkbutton(frame,text="T flip flop",variable=check_status_c2).grid(row=n+3,column=3)
    
    frame.pack()
    
    
    button = tk.Button(root,text="Submit", command=submit)
    button.pack()
    root.mainloop()
    
    if(check_status_c1.get()==1):    flip_flop="JK flip flop"
    elif(check_status_c2.get()==1):  flip_flop="T flip flop"
    
    return ref,flip_flop
  
  
#%%
"""The above section includes the implementation of various helper functions and the GUI code used in the program. 
These functions assist in generating the state table, displaying the GUI, selecting the flip-flop type, generating the circuit excitation table,
and generating boolean expressions."""


print("enter no of states in the state daigram : ")
no_of_states = int(input())
states = generate_state(no_of_states)

for i in range(len(states)):
  print("state " + str(i) +" : " + str(states[i]))

state_table = generate_state_table(states)

##display(state_table)

data,flip_flop_gui = mygui(no_of_states,states)

state_table_index = 2
for i in data:
    state_table[state_table_index] = i
    state_table_index+=1


print("State table generated till now")
print(tabulate(state_table,tablefmt="fancy_grid"))
print(2*"\n")

## filp flop selection
print("enter the required flip flop")
flip_flop_type = flip_flop_gui.lower()
flip_flop = flip_flop_selction(flip_flop_type)
print(2*"\n")

circuit_excitation_table = generate_circuit_excitation_table(state_table, flip_flop, flip_flop_type)
for i in range(2,len(circuit_excitation_table)):  circuit_excitation_table[i][0] = "".join(circuit_excitation_table[i][0])

print("Circuit excitation table")
print(tabulate(circuit_excitation_table,tablefmt="fancy_grid"))
print(2*"\n")

"""## Boolean Equations"""

print("Results")
result = (generate_boolean_expression(circuit_excitation_table))

print(tabulate(result,headers=["Boolean Expression",""],tablefmt="fancy_grid"))
print(2*"\n")


#%%
