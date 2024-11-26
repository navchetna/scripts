# WSL

## Install Windows Subsystem for Linux (WSL):

1. Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator"
2. `wsl --install`

 
## Change the default Linux distribution installed

To see a list of available Linux distributions available for download through the online store

```
wsl --list --online
```

Install the distro, preferred is: Ubuntu-22.04

```
wsl --install -d <DistroName> to install a distro
```
 
## Check the version of WSL

To see whether your Linux distribution is set to WSL 1 or WSL 2, use the command. It will be mostly WSL2
```
wsl -l -v
```

## Reference

1. https://learn.microsoft.com/en-us/windows/wsl/
