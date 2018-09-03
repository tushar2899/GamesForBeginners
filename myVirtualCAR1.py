#my virtual car1.0
"""
Author::: tushar2899
following inputs required:
license plate number 
vehicle identification no. 
and then choice codes for continuous operation 
 ENTER THE DESIRED CHOICE CODE:
1.GEAR UP     2.GEAR DOWN
3.MOVE FAST     4.MOVE SLOW
5.TURN LEFT     6.TURN RIGHT     7.GO REVERSE
8.STOP  9.EXIT
"""

class Cars():

    """CLASS NAME:Cars

    Version 1.0

    Author: tushar2899

    Description:THIS CLASS contains cars various details and operation related to the working of cars

    """

    direction="NORTH"  #inittially the direction of car is set as north



    def __init__(self, lic_plate, veh_Iden_No, speed=0, rpm=0, gear=0, fuel_level=100, engine_temp=37.5):

        self.lic_plate=lic_plate

        self.veh_Iden_No=veh_Iden_No

        self.speed=speed

        self.rpm=rpm

        self.gear=gear
        self.fuel_level=fuel_level

        self.engine_temp=engine_temp


    
#defining the 8 getter methods
    def getLic_plate(self):
        """getting the license plate number of the car"""
        return "LICENSE PLATE NO.           %s"%self.lic_plate

    def getVeh_id(self):
        """getting the vehicle identification no."""
        return "VEHICLE IDENTIFICATION NO.  %s"%self.veh_Iden_No

    def getSpeed(self):
        """getting the speed of the car at that moment"""
        return "SPEED:                      %d"%self.speed

    def getRpm(self):
        """getting the rpm of the car"""
        return "RPM:                        %d"%self.rpm

    def getGear(self):
        """getting the gear level """
        return "GEAR:                       %d"%self.gear

    def getFuel(self):
        """getting the fuel level of the car"""
        return "FUEL LEVEL                  %s"%self.fuel_level

    def getEng_temp(self):
        """getting the engine temperature"""
        return "ENGINE TEMPERATURE:         %s"%self.engine_temp
        
    def getDir(self):
        """getting the direction of the car"""
        return "DIRECTION:                  %s"%Cars.direction


    def gearUp(self):
        """to increase the gear level
        if gear is at 5 it can't be increased
        if gear inc. speed inc.
        if speed inc.rpm and temp inc."""
        
        if(self.gear<5 ):

            self.gear+=1
        else:
            print ("Maximum gear level Reached")


       
        
#since speed has to change with gear hence if gear>0 with every increment speed will inc. by 40

        if(self.gear>0 and self.speed<=160):

            self.speed+=40

        elif(self.gear==0):

            self.speed=0

        else:
            if self.gear==-1:
                self.speed=40


        
#since rpm has to change with speed hence if gear>0 with every increment rpm will inc. by 750

        if(self.gear>0 and self.rpm<=400):

            self.rpm+=750

        elif(self.gear==0):

            self.rpm=0

        else:
            if self.gear==-1:
                self.rpm=750



        #since engine temp has to change with speed hence if gear>0 with every increment temp will inc. by 40
 
        if(self.gear>0 and self.engine_temp<160):

            self.engine_temp+=40

        elif(self.gear==0):

            self.engine_temp=35

        else:
            if self.gear==-1:
                self.engine_temp=75


    def gearDown(self):
        """ lowering the gear level
        if gear is lowered speed dec.
        if speed dec. rpm and temp. dec.
        """
        if(self.gear>=0):
            self.gear-=1

        else:
            print ("LOWEST GEAR REACHED")
        if(self.gear==0):
            self.speed=0


        #since speed has to change with gear hence if gear>0 with every decrement speed will dec. by 40

        if(self.gear>0 and self.speed>+40):
            self.speed-=40

        elif(self.gear==0):
            self.speed=0

        else:
            if self.gear==-1:
                self.speed=40
        

            
        
    #since rpm has to change with speed hence if gear>0 with every decrement rpm will dec. by 750

        if(self.gear>0 and self.rpm>=750):
            self.rpm-=750

        elif(self.gear==0):
            self.rpm=0

        else:
            if self.gear==-1:
                self.rpm=750


        #since engine temp has to change with speed hence if gear>0 with every decrement temp will dec. by 40

        if(self.gear>0 and self.engine_temp>=65):
            self.engine_temp-=40

        elif(self.gear==0):
            self.engine_temp=35

        else:
            if self.gear==-1:
                self.engine_temp=75


    def moveFast(self):
        """to increase the speed  if gear is !=0  by 10
        if speed inc.rpm and temp icreases"""

        if(self.gear!=0 and self.speed<=190):

            self.speed+=10

        else:

            self.speed=0
        if self.speed==200:
            print ("Maximum speed reached")


     
   #since rpm has to change with speed hence if gear>0 with every increment rpm will inc. by 200

        if(self.gear!=0):

            self.rpm+=200

        else:

            self.rpm=0


       
 #since engine temp has to change with speed hence if gear>0 with every increment temp will inc. by 10

        if(self.gear!=0):

            self.engine_temp+=15

        else:

            self.engine_temp=35


    def moveSlow(self):
        """to decrease the speed  if gear is !=0  by 10
        if speed inc.rpm and temp dec."""
        
        if(self.gear!=0 and self.speed>=10):

            self.speed-=10

        else:
 
            self.speed=0
        if self.speed==0:
            print ("Lowest speed reached")



     
   #since rpm has to change with speed hence if gear>0 with every decrement rpm will inc. by 200

        if(self.gear!=0 and self.rpm>=200):

            self.rpm-=200

        else:

            self.rpm=0


       
 #since engine temp has to change with speed hence if gear>0 with every decrement temp will inc. by 10

        if(self.gear!=0 and self.temp>=45):

            self.engine_temp-=15

        else:

            self.engine_temp=35

    
    def moveRight(self):
        """to take a left turn 
        respectively the direction changes"""
        if Cars.direction=="NORTH":
            Cars.direction="EAST"

        elif Cars.direction=="EAST":
            Cars.direction="SOUTH"

        elif Cars.direction=="SOUTH":
            Cars.direction="WEST"

        else:
            Cars.direction="NORTH"

    def moveLeft(self):
        """to take a right turn 
        respectively the direction changes"""
        if Cars.direction=="NORTH":

            Cars.direction="WEST"

        elif Cars.direction=="WEST":

            Cars.direction="SOUTH"

        elif Cars.direction=="SOUTH":

            Cars.direction="EAST"

        else:

            Cars.direction="NORTH"


    def moveBack(self):
        "to go on reverse"
        self.gear=-1
        self. speed=40

        
    def stop(self):
        """to stop the vehicle"""
        self.gear=0
        self.speed=0
        self.rpm=0

    
    

        




#---------------------end of class Cars---------------------------------------------------
#getting the lic plate no. and vin from the user
car_lic=input("Enter license plate number:")
car_vin=int(input("Enter vehicle verification number:"))

car1=Cars(car_lic,car_vin) #creating an object named car1 of class Cars

#PRINTING THE CURRENT STATUS OF THE CAR
print (car1.getLic_plate())
print (car1.getVeh_id())

print (car1.getGear())

print (car1.getSpeed())

print (car1.getRpm())

print (car1.getFuel())

print (car1.getEng_temp())

print (car1.getDir())

#INITIATING A INFINITE LOOP FOR CONTINUOUS OPERATION ON THE CAR
while(1==1):
    #SHOW CASING THE PREFENCE MENU AND GETTING THE CHOICE FROM USER
    choice=int(input("********menu********\n ENTER THE DESIRED CHOICE CODE:\n1.GEAR UP     2.GEAR DOWN\n3.MOVE FAST     4.MOVE SLOW\n5.TURN LEFT     6.TURN RIGHT     7.GO REVERSE\n8.STOP  9.EXIT\n"))
    #EXECUTING DESIRED ACTION BASED ON USER CHOICE
    if(choice==1):

        car1.gearUp()

    elif(choice==2):

        car1.gearDown()

    elif(choice==3):
        car1.moveFast()

    elif(choice==4):

        car1.moveSlow()
    elif(choice==5):

        car1.moveLeft()

    elif(choice==6):

        car1.moveRight()

    elif(choice==7):

        car1.moveBack()

    elif(choice==8):

        car1.stop()

    elif(choice==9):

        break

    else:

        print ("INVALID CHOICE CODE")
        
    #PRINTING THE CHANGED STATE OF THE VEHCLE    
    print (car1.getLic_plate())
    print (car1.getVeh_id())

    print (car1.getGear())

    print (car1.getSpeed())

    print (car1.getRpm())

    print (car1.getFuel())

    print (car1.getEng_temp())

    print (car1.getDir())
    print ("\n\n")
    
    

#SAMPLE OUTPUT
"""
Enter license plate number:MH-02-7899
Enter vehicle verification number:879541457
LICENSE PLATE NO.           MH-02-7899
VEHICLE IDENTIFICATION NO.  879541457
GEAR:                       0
SPEED:                      0
RPM:                        0
FUEL LEVEL                  100
ENGINE TEMPERATURE:         37.5
DIRECTION:                  NORTH
********menu********
 ENTER THE DESIRED CHOICE CODE:
1.GEAR UP     2.GEAR DOWN
3.MOVE FAST     4.MOVE SLOW
5.TURN LEFT     6.TURN RIGHT     7.GO REVERSE
8.STOP  9.EXIT
1
LICENSE PLATE NO.           MH-02-7899
VEHICLE IDENTIFICATION NO.  879541457
GEAR:                       1
SPEED:                      40
RPM:                        750
FUEL LEVEL                  100
ENGINE TEMPERATURE:         77.5
DIRECTION:                  NORTH


********menu********
 ENTER THE DESIRED CHOICE CODE:
1.GEAR UP     2.GEAR DOWN
3.MOVE FAST     4.MOVE SLOW
5.TURN LEFT     6.TURN RIGHT     7.GO REVERSE
8.STOP  9.EXIT
6
LICENSE PLATE NO.           MH-02-7899
VEHICLE IDENTIFICATION NO.  879541457
GEAR:                       1
SPEED:                      40
RPM:                        750
FUEL LEVEL                  100
ENGINE TEMPERATURE:         77.5
DIRECTION:                  EAST


********menu********
 ENTER THE DESIRED CHOICE CODE:
1.GEAR UP     2.GEAR DOWN
3.MOVE FAST     4.MOVE SLOW
5.TURN LEFT     6.TURN RIGHT     7.GO REVERSE
8.STOP  9.EXIT
"""
 
