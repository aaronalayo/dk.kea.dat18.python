class CellularAutomaton:
    def __init__(self, rule, init_state = []):
        self.rule = rule
        self.init_state = init_state      
        
        
        
       



    def generate(self, init_state):
        step = 0
        new_gen =[len(self.init_state)]
  
        for i in range(len(self.init_state)):
            left = self.init_state[i-1],
            center = self.init_state[i],
            right = self.init_state[i+1],
            new_gen[i] = self.rules(left[i], center[i], right[i])
            print(new_gen[i])

            self.init_state = new_gen
        step+=1
        return init_state
        
            
            

   
    def __call__(self):
        print(self.generate(self.init_state))
        cells = []
        for i in self.init_state:
            if i == 1:
                cells.append('*')
            else:
                if i == 0:
                    cells.append('-')
        print(self.init_state)
        
        



    def binary(self, rule2binary):
        rule2binary = []
        for i in bin(self.rule)[2:]:
           rule2binary.append(i)
        return rule2binary


    def rules(self,a,b,c):
        rule_in_binary = self.binary(self.rule)
        
        if a == 1 & b == 1 & c == 1:
            return rule_in_binary[0]
        if a == 1 & b == 1 & c == 0:
            return rule_in_binary[1]
        if a == 1 & b == 0 & c == 1:
            return rule_in_binary[2]
        if a == 1 & b == 0 & c == 0:
            return rule_in_binary[3]
        if a == 0 & b == 1 & c == 1:
            return rule_in_binary[4]
        if a == 0 & b == 1 & c == 0:
            return rule_in_binary[5]
        if a == 0 & b == 0 & c == 1:
            return rule_in_binary[6]
        if a == 0 & b == 0 & c == 0:
            return rule_in_binary[7]
        else:
            return 0
          
        



r = 232
s = [0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0]
ca = CellularAutomaton(r,s)
print(ca())




