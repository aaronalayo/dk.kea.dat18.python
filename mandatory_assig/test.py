   # def __init__(self, rule, size):
    #     self.rule = rule
    #     self.size = .gen(size)
        
        
        
        
        
    
    # def gen(self, size):
    #     init_state = [0]*self.size
    #     print(init_state)



    # def generate(self):
    #     cells = self.init_state
    #     a = len(cells)
        
        
        
    #     # print(cells)
        
    #     result = [] 
    #     step = 0
    #     while(step < 15):   
    #         self.display(cells)  
    #         for i in range(0,a):
                
    #             if i > 0 and i < (a-1):
                     
    #                 left = cells[i-1]
    #                 center = cells[i]
    #                 right = cells[i+1]
    #                 # print(result)
    #                 result.append(int(self.rules(center,left,right)))  
    #         # prints new state of the cells       
    #             # left-most cell : check the second cell
    #             elif i == 0:
    #                 if cells[1] == 1:
    #                     result.append(1)
                    
    #                 else:
    #                     result.append(0)

    #             # right-most cell : check the second to the last cell
    #             elif i == a-1:
    #                 if cells[a-2] == 1:
    #                     result.append(1)
    #                 else:
    #                     result.append(0)
                 
                    
            
            
    #         # print(result)

            
    #         self.display(cells)
    #         cells = result
    #         step+=1
            
        
   # def display(self,gen):
    #     self.gen = []
    #     cells = {0:'-', 1:'*'}

    #     print(''.join( [cells[e] for e in gen]))

    # def rules(self,a,b,c):
    #     rule_in_binary =  "{0:08b}".format(self.rule)
    #     # print(rule_in_binary)
    #     if a == 1 & b == 1 & c == 1:  
    #         return rule_in_binary[0]
    #     if a == 1 & b == 1 & c == 0:
    #         return rule_in_binary[1]
    #     if a == 1 & b == 0 & c == 1:
    #         return rule_in_binary[2]
    #     if a == 1 & b == 0 & c == 0:
    #         return rule_in_binary[3]
    #     if a == 0 & b == 1 & c == 1:
    #         return rule_in_binary[4]
    #     if a == 0 & b == 1 & c == 0:
    #         return rule_in_binary[5]
    #     if a == 0 & b == 0 & c == 1:
    #         return rule_in_binary[6]
    #     if a == 0 & b == 0 & c == 0:
    #         return rule_in_binary[7]
        # else: 
            # return 0