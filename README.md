# Pacman_Python_with_Portals
In this assignment, you will create the Pacman Portal game, based on the classic Pacman game, and
the classic Portal (3d) game.
 The image resources you will need (ship, ship animation destruction, bunker, different types of aliens,
alien animation destruction, and ufo destruction) will all have to be created using an Image editing tool
such as Inkscape or Gimp. The audio resources you will need can be captured using an audio editor
such as Audacity from an online version of Pacman.



1. The game has a startup screen that shows the name of the game, shows the animations of the
ghosts chasing Pacman, Pacman chasing the ghosts and eating them, and the ghosts being
individually introduced.
2. The startup page has a menu for Start game and high scores. The high scores are stored on
disk, and are displayed when the High Scores menu is selected, or after each game. The
menu is animated when the mouse hovers over it.
3. Implemented the maze, as laid out in the image above or in the Pacman game, and which has:
a startup pen for the ghosts, a tunnel from the far right to the far left, Power pills in each of the
four corners, power points uniformly spread through the maze, and a fruit value that appears
randomly.
4. Allow Pacman to create temporary Portals in the walls of the maze, similar to the 3d
game Portal, or the movie Dr. Strange. These portals only allow Pacman to pass through
at the lower game levels. At the higher levels, the ghosts can also pass through.
5. Implemented four types of enemy ghosts, Blinky, Pinky, Inkey, and Clyde, that cooperatively
chase Pacman and try to eat him. Also implemented their AIs. If Pacman eats a Power pill, they
change (for a short time) to blue versions, and run away from him. Pacman can eat them in this
state, for 200, 400, 800, and 1600 pts. each, if he eats all four of them before they change
back. When they are about to change back, they flash white and blue (slowly), to warn him. If
the ghosts are eaten by Pacman, their eyes remain, and fly back to their starting pen, where
they are resurrected. They are immediately resurrected, even if the other ghosts are still in their
blue or white/blue state.
6. Each ghost has its own personality: Blinky (red) is the most aggressive, and moves faster as the
number of points decreases. Pinky and Inkey and Clyde move at the same speed, but Clyde is
not very aggressive. Pinky circles the maze counterclockwise. Inkey and Clyde circle
clockwise. They are thrown off by rapid left/right or up/down arrow keys, but quickly home in
on Pacman if he moves in a straight line.
7. Implemented our hero, Pacman, who runs trough the maze trying to eat as many points, power
pills, and fruits as he can without getting eaten by the ghosts. He can eat ghosts (for a short
time) if he eats a Power pill, when they change to their blue, running away selves.
8. Created the images of the ghosts, including their blue and white alter-egos, the Pacman, Maze,
Startup screen text images, ghost point values, fruit and fruit values with an Image editor, such
CPSC 386 – project two – page 2 of 4
as Inkscape or Gimp.
9. Created and implemented the animations (Startup animations of ghosts chasing Pacman and
Pacman chasing and eating the ghosts, and the introductions of each of the four ghosts,
Pacman eating, Ghosts moving, Pacman being eaten, Ghosts being eaten) with an image
editor. Note: the ghosts have a simple, two-frame animation, alternating between three and
four legs, and their eyes look in their direction of motion. Also note: Pacman has a simple, 4-
frame animation (run forwards and backwards) for eating, and a 16-frame animation when he
is destroyed (his mouth becomes larger and larger, then he disappears and a circle of
increasing diameter is seen.
10. Implemented multiple levels, of increasing difficulty (faster, more aggressive ghosts, who can
also go through portals), once Pacman has successfully eaten all power points and power pills
in a level.
11. Used a sound editor such as Audacity to record the music (Start screen, Level up, Ghost
running away, Game over), Pacman eating sounds (eating points, eating Power pills, eating
ghosts), and Ghosts eating Pacman sounds.
12. Ensure that every python source file shows a green checkmark in Pycharm (passes all PEP 8
requirements).
13. Push the contents of your project to a new GitHub repository using a git client (e.g., the git
command-line client, GitHub Desktop, or GitHub for Atom). Do not submit files using drag-anddrop onto the repository web page, and do not push this assignment to the same repository as
your previous homework assignments.
Submission
Turn in the code for this project by uploading all of the Python source files you created, the images
directory, and the sounds directory to a single public repository on GitHub. While you may discuss this
homework assignment with other students. Work you submit must have been completed on your own.
To complete your submission, print the following sheet, fill out the spaces below, and submit it to the
professor in class by the deadline. Failure to follow the instructions exactly will incur a 10% penalty on
the grade for this assignment.
