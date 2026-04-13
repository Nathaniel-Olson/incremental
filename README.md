# Hello!
## welcome to my pygame incremental game project!

For the most part, this project is simply messing around with incremental games, and a light exploration into creating gui elements from scratch.
In the future, i plan to try and learn Rust, so this will serve as a sort of stepping stone for me to recreate, as well as going from oop/inheritance-based towards compositional instead.

# files

### `calc.py`
> stores the `LongInt` class, necessary for working with enormous numbers.  
> also stores the `UpgradeableParameter` class, to allow for easier modification of the value, cost, and multiplier of a variable.

### `constants.py`
> stores the `Color` class, responsible for the colors in the gui; has several swappable colorwaves  
> stores the `Font` class, which stores the various fonts (and their sizes) for use in the project.

### `game.py`
> responsible for all of the user i/o in the game, through the `Game` class.

### `gui.py`
> stores the classes responsible for gui: (strictly hierarchical, `Group` -> `TextBox` -> `Text`)  
	- `Group`  
	- `TextBox`  
	- `Text`

### `main2.py`
> the second part of the main game. Currently based off of position and its 6 derivates, inspired by Antimatter Dimensions.
