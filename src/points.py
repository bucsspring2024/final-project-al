class points:
    def __init__(self,multiplier,hits):
        self.multiplier= multiplier
        self.point=0+(hits*multiplier)
        
           
    def points(self):
        return self.point
    
    

    def hits(self):
        self.count=0
        if pygame.cursorcollide:
            self.count+=1
        #can program so if the cursor collides with the "mole" it counts a hit
        return self.count
    
    
    
    