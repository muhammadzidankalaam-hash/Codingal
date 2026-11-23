# Smart Device Command Center
 
# PART 1: Import tools for abstraction
from abc import ABC, abstractmethod
 
# PART 2: Create an abstract class
class SmartDevice(ABC):
 
    # Common method
    def show_device(self, name):
        print("Device Name:", name)
 
    # Abstract method
    @abstractmethod
    def turn_on(self):
        pass
 
 
# PART 3: Create subclasses that override the abstract method
class SmartLight(SmartDevice):
    def turn_on(self):
        print("Smart Light is now ON")
 
 
class SmartFan(SmartDevice):
    def turn_on(self):
        print("Smart Fan is now ON")
 
 
class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Smart Speaker is now ON")
 
 
# PART 4: Create objects and call their methods
light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()
 
light.show_device("Living Room Light")
light.turn_on()
 
fan.show_device("Bedroom Fan")
fan.turn_on()
 
speaker.show_device("Music Speaker")
speaker.turn_on()
 
 
# PART 5: Polymorphism without inheritance
# These classes do not inherit from SmartDevice,
# but they share the same method name.
 
class SecurityCamera:
    def check_status(self):
        print("Security Camera is recording")
 
 
class DoorLock:
    def check_status(self):
        print("Door Lock is secure")
 
 
# PART 6: Use the shared method name
devices = [SecurityCamera(), DoorLock()]
 
print("")
print("===== SMART DEVICE STATUS =====")
 
for device in devices:
    device.check_status()
 
print("===============================")
