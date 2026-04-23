# main

from lib.room_sensor import RoomSensor

r1 = RoomSensor("Kitchen", 28, 99, 189)
r2 = RoomSensor("Guest_Rooom", 22, 49, 149)
r3 = RoomSensor("Living_room", 33, 69, 285)

rooms = [r1, r2, r3]

# Counters_ GPT HELPED
comfortable_count = 0
normal_count = 0
warning_count = 0

# THE Loop
for r in rooms:
    r.show_info()
    
    level = r.comfort_level()
    print("Comfort Level:", level)
    
    print("Light Status:", r.light_status())
    print()
    
    # CATEGORY Numbers counting
    if level == "Comfortable":
        comfortable_count += 1
    elif level == "Warning":
        warning_count += 1
    else:
        normal_count += 1

#counting the totals 
print("Comfortable:", comfortable_count)
print("Normal:", normal_count)
print("Warning:", warning_count)