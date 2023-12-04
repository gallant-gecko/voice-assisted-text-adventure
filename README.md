# voice-assisted-text-adventure
a project created for CSCI4250

The Voice Assisted Text Adventure is a stand-alone game that uses voice inputs to navigate a typical text-adventure style game.

## Installation
1. Install the dependencies with the following commands:
  pip install SpeechRecognition pyaudio
2. Create a folder of your choosing to act as a Git repository:
  mkdir folderOfYourChosing
  git init
3. Clone the repository from within that folder:
  git clone https://github.com/gallant-gecko/voice-assisted-text-adventure.git

## Usage

/pathToYourPythonInterpreter voice-assisted-text-adventure.py
Alternatively, you could add a shabang line at the top of the text adventure that points to your Python installation and simply run the program from the terminal like so:
  ./voice-assisted-text-adventure.py

The shabang line would would look like the following:
  #!/path/to/your/python/python.exe

Once the game is started, you will prompted to give a single word voice command that corresponds with a given option.
Speak the word and the option will be selected.

## Troubleshooting
If your voice commands are not being accepted, you may need to reduce your mic sensativity or adjust recognizer.energy_threshold variable to be higher to reduce ambient noise.

## Changelog
Milestone1 added a basic prototype that had few rooms and expected functionality.

Milestone2 added a progression of rooms to explore and navigate through, leading to a confrontation with a dragon. (+10 Room Minimum)

Milestone3 added a scoring system based on player actions and improved timeouts for voice actions. (Points are obtained from reading the ancient tome, gathering crystals, etc)

Milestone4 added improvements to the overall gameplay experience gathered from usability testing. (Ability to exit game at any time, clarified user voice options, etc.)
