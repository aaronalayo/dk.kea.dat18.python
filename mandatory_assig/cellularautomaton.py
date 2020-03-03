class CellularAutomaton:
    def __init__(self, rule, init_state = []):
        self.rule = rule
        self.init_state = init_state
        self.generate()     
        
 


    def generate(self):
        
        a = len(self.init_state)
        
        self.display(self.init_state)

        step = 0
        while(step < 50):
            result = []
            for i in range(0,a):
                
                if i > 0 and i < a-1:
                    left = self.init_state[i-1]
                    center = self.init_state[i]
                    right = self.init_state[i+1]
                    
                    result.append(int(self.rules(center,left,right)))
                    
                # left-most cell : check the second cell
                elif(i == 0):
                    if self.init_state[1] == 1:
                        result.append(1)
                    else:
                        result.append(0)

                # right-most cell : check the second to the last cell
                elif(i == a-1):
                    if self.init_state[a-2] == 1:
                        result.append(1)
                    else:
                        result.append(0)
           
            # prints new state of the cells
            self.display(result)

            
            self.init_state = result
            
            step+= 1
                
        
   
    def display(self,gen):
        self.gen = gen
        cells = {0:'-', 1:'*'}

        print(''.join( [cells[e] for e in gen]))



    def rules(self,a,b,c):
        rule_in_binary =  "{0:08b}".format(self.rule)
        
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
        
            
            
          
        

if __name__ == "__main__":
    r = 200
    
    s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ca = CellularAutomaton(r,s)
    ca


    





