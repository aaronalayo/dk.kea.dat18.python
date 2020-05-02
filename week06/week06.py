def foo_bar(n, d):
    """
    

    """
    for i in range(n+1):
        msg = ""
        for k, v in d.items():
            if i % k == 0:
                msg += v
        if msg:
            print(msg)
        else:
            print(i)

# you can replace last for lines (down below) but the logic is not good in case of 0
        # print(msg or i)
        
d = {
    3:"Foo", 
    5:"Bar", 
    7:"Fiz", 
    4:"Buz"
}
   
     

       


foo_bar(25,d)   
