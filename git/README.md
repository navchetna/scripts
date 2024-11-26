# GIT

## Installation and configuring git cli
1. Install Git package
    ```
    sudo apt-get install git
    ```
2. Configure Git
    ```
    git config --global user.name "Your Name"
    git config --global user.email "Your Email"
    ```
  
## Installation and configuring gh cli
(This is required to authenticate to GitHub)

1. Install gh cli
    ```
    (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
    && sudo mkdir -p -m 755 /etc/apt/keyrings \
    && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && sudo apt update \
    && sudo apt install gh -y
    ```
2. Upgrade gh cli
    ```
    sudo apt update
    sudo apt install gh
    ```
3. Navigate to https://github.com/settings/tokens and generate a new token with the required permissions
4. Authenticate to GitHub
    ```
    gh auth login
    ```
5. Select `Github.com`
6. Select `HTTPS`
7. Select `Paste an authentication token`
8. Paste the token generated in step 3