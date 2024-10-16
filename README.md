## Dependencies
see DEPENDENCIES.txt

## Platforms
Unix-based. Mainly targeted at Linux, but if you can run wofi on MacOS, then I guess it should work on it too

## How it works
the ./run bash executable is the entry point of the program. it gets the user input and then passed it to python, which handles the logic.
there are also a bunch of little executable files, each taking care of a single command that would normally be ran in the terminal

## Why do this?
I use Toggl to track my time (see https://track.toggl/com) and recently I started using its CLI (see DEPENDENCIES.txt for the link) to manage my time entries more efficiently
I wanted to bind this script to a keybind so that I can spend less time stopping and starting my time entries

## Committing
Any pull requests are welcome



I hope someone will find this useful lol
