class CellularAutomaton:
    def __init__(self, rule, size):
        self.rule = rule
        self.size = size
        self.generate()
        
 
    def generate(self):
        
        init_state = '0'*self.size + '1' + '0' * self.size
        current_state = list(init_state)
        a = len(current_state)

        step = 0
        

        
        while step < self.size:

            self.display(current_state)
            new_state = [None]*a
            
            for i in range(0,a-1):
                 if(i == 0):
                    new_rule = current_state[i-1], current_state[i], current_state[i+1]
                 if(i == a-2):
                    new_rule = current_state[i], current_state[i+1], current_state[0]
                    new_state[i+1] = self.rules(new_rule)
                    
                    left = current_state[i-1]
                    center = current_state[i]
                    right = current_state[i+1]
                    
                    
                    new_rule = left, center, right
                    new_state[i] = self.rules(new_rule)

            current_state = new_state
            
            step = step + 1
                
        
   
 
    def display(self, state):
        for cell in state:
            if cell == '1':
                print('*', end="", flush=True)
            else:
                print('-', end="", flush=True)
        print('')  


    
    def rules(self, combination):
         rule_in_binary =  "{0:08b}".format(self.rule)
         #print(rule_in_binary)
         if (combination == ('1', '1', '1')):
             return str(rule_in_binary[0])
         if (combination == ('1', '1', '0')):
             return str(rule_in_binary[1])
         if (combination == ('1', '0', '1')):
             return str(rule_in_binary[2])
         if (combination == ('1', '0', '0')):
             return str(rule_in_binary[3])
         if (combination == ('0', '1', '1')):
             return str(rule_in_binary[4])
         if (combination == ('0', '1', '0')):
             return str(rule_in_binary[5])
         if (combination == ('0', '0', '1')):
             return str(rule_in_binary[6])
         if (combination == ('0', '0', '0')):
             return str(rule_in_binary[7])
  
            
     

        

if __name__ == "__main__":
    rule = 30
    size = 21
    # s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # s = [0,0,1,0,0]
    ca = CellularAutomaton(rule,size)
    ca

 
    





