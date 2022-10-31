"""1603. Design Parking System"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self._free_spots = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        if self._free_spots[carType]:
            self._free_spots[carType] -= 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
