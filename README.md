# P4 - ChessApp
 This program allows to manage chess turnaments.
 - Create turnaments (name / date / place / players list / time control / number of rounds / description)
 - Manage a database (players / turnaments) using TinyDB.

 The turnament pairing system is based on the Swiss System.

# Environment
## To use this script in an virtual environment:
 
 Python >= 3.10.6
```
$ cd /path/to/project
$ python -m -venv <environment name>
```

activation windows  
`$ ~env\Scripts\activate.bat`  
activation macos/linux  
`$ ~source env/bin/activate`

packages installation  
`(env)$ python -m pip install -r requirements.txt`

## To use this script without an virtual environment:
- Install Python >=3.10.6
- From terminal `python -m pip install -r requirements.txt`
- To run the program 
```
$ cd /path/to/folder/P4_ChessApp-main
$ python -m main.py
```


# Requirements
tinydb==4.7.0


# Instructions
 At the start, the program will show you basic commands and instructions
```
/// Naviguer en entrant le numéro du menu ou des choix proposés.
/// Pour valider votre choix appuyer sur 'Entrée'.
/// Pour quitter le programme entrez: 'quitter'.
/// Pour annuler l'action en cours entrez: 'annuler'.
/// Pour afficher l'aide entrez: 'aide'.
```

 Closing the program between two actions (adding a player to the database, running a turnament's round) will not loose informations.
 
 
