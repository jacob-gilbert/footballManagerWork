# Football Manager Squad Visualization

<!-- START doctoc -->
### Table of Contents
*[Description](#description)
*[Example](#example)
*[Setup and Directions](#setup-and-directions)
*[Imperfections](#imperfections)
<!-- END doctoc -->

### Description
* Creates a visual map of all players and where they play on the field from your squad
* Identify areas of weakness or areas with too many players
* Can add players in individually or import your squad in from football manager
* Contains an extra area to put players to send on loan or transfer list

### Example
![alt text](fmSquadVisualization.png)
* The players in the red section are ones to loan or transfer, where as the one in the white section will be registered into the squad

### Setup and Directions
* Download the zip file from github
* Unzip the file and put the folder somewhere you can easily find
* Go into football manager to your squad screen, make sure the view is set to general info (it won't work otherwise). Hide loans and trialists unless you want to include them. Highlight every player in your squad and press ctrl p. Choose to save as a text file put the file in the same folder as the code you downloaded from github. Name the file squad_text.rtf (the code won't work otherwise)
* Now you are almost ready to run the code. You need to have python downloaded (preferably 3.12.3) find a tutorial of how to install python if you do not have it already. You also need to import the python modules this code utilizes
* In your terminal type the command: pip install PyQt5
* In your terminal type the command: pip install pandas
* In your terminal change directories to the one that contains the code you downloaded. My code is located at \Users\jacob\desktop\footballManagerWork> but when I enter terminal I am only at \Users\jacob> so I have to type the command: cd desktop\footballManagerWork
* Finally run the python code with the command: python team_layout_interactive.py
* The graphical user interface (GUI) will now appear. You can either manually type your players in or click the "import players" button. If you have followed all of the steps above correctly, it will work instantly. You can then drag the players to where you want them on the screen.

### Imperfections
* When players are uploaded they are assigned a location on the screen based on their best position assign from football manager. This position may not be the one you want them to play in so you will have to drag them to where you'd like.
* There is an area around a player that you can click on to drag the player, not just on the circle. However, some players names are so long that they do not fit in the area and are cut off (see image above).
* Some characters to not import correctly from football manager (see image above).