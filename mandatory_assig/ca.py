def ca():

   ca = [
         0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0, 0,1,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,  0,0,0,0]
   
   ca_new = ca[:]

   dic = {0:'-', 1:'*'}

   print(''.join( [dic[e] for e in ca_new]))
   # additional 31 steps
   step = 1
   while(step < 32):
      ca_new = []
      # loop through 0 to 63 and store the current cell status in ca_new list
      for i in range(0,64):
         # inside cells - check the neighbor cell state
         if i > 0 and i < 63:
            if ca[i-1] == ca[i+1]:
               ca_new.append(0)
            else:
               ca_new.append(1)

         # left-most cell : check the second cell
         elif(i == 0):
            if ca[1] == 1:
               ca_new.append(1)
            else:
               ca_new.append(0)

         # right-most cell : check the second to the last cell
         elif(i == 63):
            if ca[62] == 1:
               ca_new.append(1)
            else:
               ca_new.append(0)

      # draw current cell state
      print(''.join( [dic[e] for e in ca_new]))

      # update cell list
      ca = ca_new[:]

      # step count
      step += 1

if __name__ == '__main__':
   ca()


