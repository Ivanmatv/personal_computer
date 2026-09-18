from personal_computer import PersonalComputer


computer = PersonalComputer("Apple")

computer.add_cell("AMD", 3.3)
computer.add_video_card("Nvidia", 16)
computer.add_hard_driver("Samsung", 512)

print(computer.get_configuration_computer())
