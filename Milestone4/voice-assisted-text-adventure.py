import speech_recognition as sr

# Initialize score and completed actions set
score = 0
completed_actions = set()

# Define game's branching paths
game = {
    "start": {
        "text": "You find yourself at the entrance of a dimly lit cave. Do you want to [enter] deeper into the cave or [climb] upwards?",
        "options": {"enter": "river", "climb": "campsite"}
    },
    "river": {
        "text": "You stumble upon an underground river. Do you want to [swim], [boat], or [back]?",
        "options": {"swim": "cavern", "boat": "door", "back": "start"}
    },
    "campsite": {
        "text": "You discover an abandoned campsite. Do you want to [search], [ascend], or [descend]?",
        "options": {"search": "library", "ascend": "chamber", "descend": "start"}
    },
    "cavern": {
        "text": "You're in a cavern filled with glowing crystals. Do you want to [collect], [search], or [return]?",
        "options": {"collect": "cavern", "search": "maze", "return": "river"},
        "actions": {"collect": 10}  # Collecting crystals grants 10 points to score
    },
    "door": {
        "text": "You find a mysterious door with inscriptions. Do you want to [open], [examine], or [leave]?",
        "options": {"open": "door_locked", "examine": "library", "leave": "river"},
        "actions": {"open": "The door won't budge. It may need a closer look."}  # Provide feedback instead of points
    },
    "library": {
        "text": "You're in an ancient library. Do you want to [explore], [read] the ancient tome, or [exit]?",
        "options": {"explore": "chamber", "read": "library", "exit": "campsite"},
        "actions": {"read": 10}  # Reading ancient tome grants 10 points to score 
    },
    "chamber": {
        "text": "You discover a hidden chamber with a pedestal. Do you want to [approach], [look], or [leave]?",
        "options": {"approach": "dragon", "look": "maze", "leave": "campsite"}
    },
    "lava": {
        "text": "You're at the edge of a lava pit. Do you want to [cross], [find], or [retreat]?",
        "options": {"cross": "maze", "find": "cavern", "retreat": "library"}
    },
    "maze": {
        "text": "You've entered a confusing maze of tunnels. Do you want to [left], [right], or [straight]?",
        "options": {"left": "chamber", "right": "lava", "straight": "dragon"}
    },
    "dragon": {
        "text": "You've entered a dragon's lair! The dragon is asleep but stirs slightly as you approach. Do you want to [fight] the dragon, [sneak] past it, or [talk] to it?",
        "options": {"fight": "lava", "sneak": "exit", "talk": "riddle"},
        "actions": {"sneak": 5}  # Minor points for Sneaking past the dragon action
    },
    "riddle": {
        "text": "The dragon awakens fully and offers you a challenge. 'Answer my riddle, and I shall let you pass. Fail, and you shall be devoured. The riddle is: 'What has keys but opens no locks?'",
        "options": {"piano": "exit", "chest": "lava", "scroll": "lava", "map": "lava"},
        "actions": {"piano": 25}  # Correct answer to the riddle provides larger point increase
    },
    "exit": {
        "text": "You've found the exit to the cave! You see daylight streaming in. Congratulations on completing the adventure!",
        "options": {}
    }
}

def recognize_command(retries=3):
    recognizer = sr.Recognizer()

    for _ in range(retries):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjusting for ambient noise once
                print("Say something...")
                audio = recognizer.listen(source, timeout=10)  # Increase timeout to 10 seconds
                command = recognizer.recognize_google(audio)
                print("You said:", command)
                return command.lower()
        except sr.WaitTimeoutError:
            print("You didn't say anything. Please try again.")
        except sr.UnknownValueError:
            print("You mumbled something unrecognizable. Please try again.")
        except sr.RequestError:
            print("I'm having trouble with the network. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    print("Sorry, we're having trouble understanding you. Please try again.")
    return ""

def play_game():
    global score, completed_actions
    current_scene = "start"
    print("Welcome to the adventure! You can say [quit] at any time to exit the game.")

    while True:
        scene = game[current_scene]
        
        # Print the scene text
        print(scene["text"])
        
        # Get the player's command
        command = recognize_command()
        
        # Check for 'quit' command to exit the game
        if command == "quit":
            print("Closing the game...")
            print("Thanks for playing!")
            break

        # If command is None, skip to the next iteration
        if command is None:
            continue
        
        # Special handling for 'open' command at the 'door' scene
        if current_scene == "door" and command == "open":
            print(scene["actions"]["open"])  # Print the message that the door won't budge
            continue  # Do not change the scene, prompt for another command
        
        # Check if the command is a valid option
        next_scene = scene["options"].get(command)
        
        # If it's a valid command and an action that increases score
        if next_scene:
            if command in scene.get("actions", {}) and command not in completed_actions:
                # Check if the action is a point-increasing action or just a message
                if isinstance(scene["actions"][command], int):
                    score += scene["actions"][command]
                    completed_actions.add(command)
                    print(f"You gained {scene['actions'][command]} points. Your score is now {score}.")
                else:
                    print(scene["actions"][command])  # Print the message for the action
            # Move to the next scene
            current_scene = next_scene
        else:
            print("Invalid command, please try again.")

if __name__ == "__main__":
    play_game()