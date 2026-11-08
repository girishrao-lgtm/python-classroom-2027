'''
Exercise 17 — Parking Lot Using Composition
'''
from dataclasses import dataclass


@dataclass(frozen=True)
class Vehicle:
    registration_number: str
    vehicle_type: str


class ParkingSlot:

    def __init__(self, slot_id, supported_type):
        self.slot_id = slot_id
        self.supported_type = supported_type
        self.vehicle = None

    def can_park(self, vehicle):
        return (
            self.vehicle is None
            and self.supported_type == vehicle.vehicle_type
        )

    def park(self, vehicle):
        if not self.can_park(vehicle):
            raise ValueError("Slot unavailable")

        self.vehicle = vehicle

    def release(self):
        vehicle = self.vehicle
        self.vehicle = None
        return vehicle


class ParkingLot:

    def __init__(self, slots):
        self.slots = slots

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if slot.can_park(vehicle):
                slot.park(vehicle)
                return slot.slot_id

        raise ValueError("No suitable slot")


parking_lot = ParkingLot([
    ParkingSlot(1, "CAR"),
    ParkingSlot(2, "BIKE"),
    ParkingSlot(3, "CAR")
])

vehicle = Vehicle("KA01AB1234", "CAR")

print("Allocated slot:", parking_lot.park_vehicle(vehicle))