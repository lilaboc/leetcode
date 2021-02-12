# https://leetcode.com/problems/design-parking-system/


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]


    def addCar(self, carType: int) -> bool:
        slot = carType - 1
        self.slots[slot] = self.slots[slot] - 1
        if self.slots[slot] < 0:
            return False
        else:
            return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)