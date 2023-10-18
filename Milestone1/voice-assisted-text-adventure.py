import speech_recognition as sr

# Define game's branching paths
game = {
    "start": {
        "text": "You find yourself at the entrance of a dimly lit cave. Do you want to 'enter' deeper into the cave or 'climb' upwards?",
        "options": {"enter": "river", "climb": "campsite"}
    },
    "river": {
        "text": "You stumble upon an underground river. Do you want to 'swim', 'boat', or 'back'?",
        "options": {"swim": "cavern", "boat": "door", "back": "start"}
    },
    "campsite": {
        "text": "You discover an abandoned campsite. Do you want to 'search', 'ascend', or 'descend'?",
        "options": {"search": "library", "ascend": "chamber", "descend": "start"}
    },
    "cavern": {
        "text": "You're in a cavern filled with glowing crystals. Do you want to 'collect', 'look' around, or 'return'?",
        "options": {"collect": "lava", "look": "dragon", "return": "river"}
    },
    "door": {
        "text": "You find a mysterious door with inscriptions. Do you want to 'open', 'read', or 'leave'?",
        "options": {"open": "exit", "read": "library", "leave": "river"}
    },
    "library": {
        "text": "You're in an ancient library. Do you want to 'study', 'clue', or 'exit'?",
        "options": {"study": "chamber", "clue": "lava", "exit": "campsite"}
    },
    "chamber": {
        "text": "You discover a hidden chamber with a pedestal. Do you want to 'approach', 'look', or 'leave'?",
        "options": {"approach": "dragon", "look": "exit", "leave": "campsite"}
    },
    "lava": {
        "text": "You're at the edge of a lava pit. Do you want to 'jump', 'find', or 'retreat'?",
        "options": {"jump": "dragon", "find": "cavern", "retreat": "library"}
    },
    "dragon": {
        "text": "You've entered a dragon's lair! The dragon is asleep but stirs slightly as you approach. Do you want to 'fight' the dragon, 'sneak' past it, or 'talk' to it?",
        "options": {"fight": "lava", "sneak": "exit", "talk": "riddle"}
    },
    "riddle": {
        "text": "The dragon awakens fully and offers you a challenge. 'Answer my riddle, and I shall let you pass. Fail, and you shall return from whence you came.' The riddle is: 'What has keys but opens no locks?' Do you answer 'piano', 'chest', or 'door'?",
        "options": {"piano": "exit", "chest": "lava", "door": "lava"}
    },
    "exit": {
        "text": "You've found the exit to the cave! You see daylight streaming in. Congratulations on completing the adventure!",
        "options": {}
    }
}


def recognize_command():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    with microphone as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjusting for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)  # 5 seconds timeout
            recognizer.energy_threshold += 500  # Increase the energy threshold
        except sr.WaitTimeoutError:
            print("You didn't say anything. Please try again.")
            return None
        
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("You mumbled something unrecognizable. Please try again.")
        return None
    except sr.RequestError:
        print("I felt a severed thread from a vast interconnect web. (Network Issues)")
    return ""



def play_game():
    current_scene = "start"
    while True: 
        scene = game[current_scene]
        print(scene["text"])
        
        if not scene["options"]:
            break  # End the game if there are no more options
        
        command = recognize_command()
        
        if command is None:
            continue  # Go to the next iteration of the loop if the user didn't say anything
        
        next_scene = scene["options"].get(command)
        
        if next_scene:
            current_scene = next_scene
        else:
            print("Invalid command, please try again.")

if __name__ == "__main__":
    play_game()