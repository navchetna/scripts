# Minikube

## Pre-requistes
1. [Docker](https://github.com/navchetna/scripts/tree/master/docker)

## Installation
1. Download the latest release with command
   ```
   curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
   ```
2. Make the `kubectl` binary executable
   ```
   chmod +x ./kubectl
   ```
3. Move the `kubectl` binary to your PATH
   ```
    sudo mv ./kubectl /usr/local/bin/kubectl
    ```
4. Verify the installation
   ```
   kubectl version --client
   ```
5. Start cluster
   ```
   minikube start
   ```

## Reference

1. https://k8s-docs.netlify.app/en/docs/tasks/tools/install-kubectl/
