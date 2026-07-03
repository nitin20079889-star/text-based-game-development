import time
import sys

def print_slow(text):
    """Prints text with a slight delay to create an engaging experience."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.015)
    print()

def start_game():
    print_slow("\n=== THE LOST CHRONICLES OF ELDORIA ===")
    print_slow("You are an archaeological explorer standing before the entrance of a forgotten tomb.")
    print_slow("Rumor has it that the Heart of Eldoria lies inside. The air is cold, and the door is cracked.")
    decision_point_1()

def decision_point_1():
    print_slow("\n--- DECISION POINT 1: THE ENTRANCE ---")
    print_slow("The main gate is rusted shut, but there is a dark fissure in the wall to your left.")
    print_slow("1. Try to force the rusted iron gate open using your crowbar.")
    print_slow("2. Squeeze through the narrow, dark fissure in the wall.")
    
    choice = input("\nWhat will you do? (Enter 1 or 2): ").strip()
    
    if choice == "1":
        print_slow("\n[CONSEQUENCE]: The heavy crowbar slips! The gate screeches open slightly, but the noise echoes.")
        print_slow("You successfully enter the Grand Hall, but you have alerted whatever dwells inside.")
        decision_point_2(alerted=True)
    elif choice == "2":
        print_slow("\n[CONSEQUENCE]: You squeeze through the tight fissure. It's quiet, but you drop your flashlight.")
        print_slow("You step into the Grand Hall completely undetected, though your visibility is limited.")
        decision_point_2(alerted=False)
    else:
        print("\nInvalid choice. The ambient dread forces you to make a valid decision.")
        decision_point_1()

def decision_point_2(alerted):
    print_slow("\n--- DECISION POINT 2: THE GRAND HALL ---")
    print_slow("In the center of the hall, you find two paths: a grand marble staircase leading down,")
    print_slow("and an ancient elevator shaft with a fraying rope pulley system.")
    print_slow("1. Walk cautiously down the crumbling marble staircase.")
    print_slow("2. Risk using the ancient mechanical elevator rope to descend quickly.")
    
    choice = input("\nWhich path will you take? (Enter 1 or 2): ").strip()
    
    if choice == "1":
        if alerted:
            print_slow("\n[CONSEQUENCE]: Because you made noise at the gate, temple guardians ambush you on the stairs!")
            print_slow("You manage to flee into a side room, but you lose your survival rations in the chaos.")
            decision_point_3(status="weakened")
        else:
            print_slow("\n[CONSEQUENCE]: Moving silently pays off. You bypass a sleeping guardian beast on the stairs.")
            print_slow("You arrive safely in the inner sanctum perfectly healthy.")
            decision_point_3(status="healthy")
            
    elif choice == "2":
        print_slow("\n[CONSEQUENCE]: The rope snaps! You slide rapidly down into the dark abyss.")
        print_slow("You land hard on a pile of ancient debris. You are bruised, but you skipped the main guards.")
        decision_point_3(status="injured")
    else:
        print("\nInvalid choice. Pick your path forward.")
        decision_point_2(alerted)

def decision_point_3(status):
    print_slow("\n--- DECISION POINT 3: THE HEART SANCTUM ---")
    print_slow("You have reached the inner chamber. Resting upon a golden pedestal is the glowing Heart of Eldoria.")
    print_slow("Suddenly, the room begins to rumble. Runes light up on the walls.")
    print_slow("1. Snatch the artifact directly off the pedestal and run for your life.")
    print_slow("2. Carefully swap the artifact with a stone of equal weight to circumvent traps.")
    
    choice = input("\nWhat is your final move? (Enter 1 or 2): ").strip()
    
    if choice == "1":
        if status == "injured" or status == "weakened":
            game_over("Ending A: The Weight of Greed. Your physical condition slows you down. The tomb collapses before you escape.")
        else:
            game_over("Ending B: The Daring Escape! Your peak condition allows you to outrun the collapsing ruins with the artifact in hand. You are rich!")
            
    elif choice == "2":
        if status == "weakened":
            game_over("Ending C: Fatal Exhaustion. Your lack of focus due to missing rations makes your calculation fail. The trap triggers, trapping you forever.")
        else:
            game_over("Ending D: The Master Thief! The weight match is perfect. The temple remains completely silent. You walk out safely with the greatest prize in history.")
    else:
        print("\nInvalid choice. Time is running out!")
        decision_point_3(status)

def game_over(ending_text):
    print_slow("\n========================================")
    print_slow(ending_text)
    print_slow("========================================")
    print_slow("\nThank you for playing 'The Lost Chronicles of Eldoria'!")
    
    retry = input("\nWould you like to try again? (yes/no): ").lower().strip()
    if retry == 'yes' or retry == 'y':
        start_game()
    else:
        print_slow("Goodbye, Adventurer!")

# Run the game engine
if __name__ == "__main__":
    start_game()