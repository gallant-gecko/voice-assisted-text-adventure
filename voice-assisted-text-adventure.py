import speech_recognition as sr

# Define the game's storyline and choices
game = {
    "start": {
        "text": "You are in a dark room. Do you want to go 'left' or 'right'?",
        "options": {"left": "left_room", "right": "right_room"}
    },
    "left_room": {
        "text": "You find a treasure chest! Do you want to 'open' it or 'leave'?",
        "options": {"open": "treasure", "leave": "start"}
    },
    "right_room": {
        "text": "Oh no! It's a trap room. You are back to start. Should you 'continue'?", 
        "options": {"continue": "start"}},
    "treasure": {
        "text": "Congratulations! You found the treasure!", 
        "options": {}}
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
            return None  # Return None when the user doesn't say anything
        
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("You mumbled something unrecognizable. Please try again.")
        return None  # Treat as if the user didn't say anything
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