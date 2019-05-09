# SpacePass

## Description
SpacePass is a [spacemacs](http://spacemacs.org) inspired gui for [pass](https://www.passwordstore.org) 
It was designed to be used in i3wm but should work on another DE/WM

## Dependencies
[pass](https://www.passwordstore.org), gtk-3.0

## Installation

Install for your user (make sure ~/.local/bin is included in PATH):
```bash
pip install --user spacepass
```

Globally install:
```bash
sudo pip install spacepass
```

## Usage
### i3wm
bindsym the desired keyboard shortcut
```
bindsym $mod+p exec spacepass
```

## Configuration
Configuration is read from the config file.
Try 'spacepass -h' for details

### options
  * config: path to the config file (defaults to $XDG_CONFIG_HOME/spacepass/config)
  * pass-dir: path to the password repository (defaults to $HOME/.password-store**

### GUI options
  * margin: Inner margin for the window
  * column-spacing: Spacing between each column
  * row-spacing: Spacing between each row
  * max-columns: Maximum number of columns to display
  * row-height: The height of the buttons in each row

## TODO
  * allow different colours
  * give option to show the password contents (multiline)
  * allow to create/update/delete passwords from the ui
  * implement search


## License
GPL-3.0-or-later 
