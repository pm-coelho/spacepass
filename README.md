# SpacePass

## Description
SpacePass is a [spacemacs](http://spacemacs.org) inspired gui for [pass](https://www.passwordstore.org) 
It was designed to be used in i3wm but should work on another DE/WM

## Dependencies
[pass](https://www.passwordstore.org)
gtk-3.0

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
bindsym the desired
```
bindsym $mod+p exec spacepass
```

## Configuration
Configuration is read from the config file 

## TODO
  * allow different colours
  * give option to show the password contents (multiline)
  * allow to create/update/delete passwords from the ui
  * implement search


## License
GPL-3.0-or-later 
