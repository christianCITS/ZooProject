import unittest
from unittest import TestCase
from src.zoo import Zoo,Fence,Zookeeper,Animal

class Test_Zoo(TestCase):

    def setUp(self) -> None:
        self.zookeper1:Zookeeper=Zookeeper("Gianni","Rossi",1)
        self.fence1:Fence=Fence(25,100,"Savana")
        self.animal1:Animal=Animal("Pluto","gatto",5,1,1,"Savana")
        self.zoo1:Zoo =Zoo(self.fence1,self.zookeper1)
    
    def test_1(self):
            self.zookeper1.add_animal(self.animal1,self.fence1)
            result:int=len(self.fence1.animals)
            message:str=f"error: the function add animal should not add animal1 into fence1"
            self.assertEqual(result,0,message)


    def test_2(self):
         pass
        



    if __name__=="__main__":
        unittest.main()




