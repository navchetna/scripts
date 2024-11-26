Install windows subsystem for Linux:

wsl --install

 

List of available distros

wsl --list --online

 

Install the distro, preferred is: Ubuntu-22.04

wsl --install -d <DistroName> to install a distro

 

To see whether your Linux distribution is set to WSL 1 or WSL 2, use the command. It will be mostly WSL2

wsl -l -v
