# Lesson 2 : Assignments : Nested If

# Problem One 
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    torch_action = input("Do you want to light a torch or proceed in the dark? ")
    if torch_action == "light a torch":
        print("You light a torch and illuminate your path. You find a hidden treasure!")
    elif torch_action == "proceed in the dark":
        print("You proceed in the dark and stumble upon a pile of gold coins!")
else:
    pass        

#Problem Two
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
facilities = ""

if attendees > 50:
    facilities += "audio system"
if attendees > 80:
    if facilities:
        facilities += " and "
    facilities += "projector"

if facilities:
    print("The recommended venue is", venue, "with the following facilities:", facilities + ".")
else:
    print("The recommended venue is", venue + ".")

vegetarian_choice = input("Do you want vegetarian food? (yes/no): ")
caterer = ""

if vegetarian_choice.lower() == "yes":
    caterer = "Veggie Delight Caterers"
else:
    caterer = "Gourmet Meals Caterers"

print("We recommend", caterer, "for catering services.")
