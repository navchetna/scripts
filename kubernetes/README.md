# Kubernetes

1. [Minikube](minikube/README.md)


# Command Reference

### Core kubectl Commands
The most foundational commands are essential for everyday tasks.

#### List Resources
Start by listing resources with kubectl get. You can view all Kubernetes resources, whether pods, services, or nodes.

```
# List all pods, services, and nodes across all namespaces
kubectl get pods --all-namespaces
kubectl get svc        # shorthand for services
kubectl get nodes
```

#### Describe Resources
Use kubectl describe to view metadata, events, and configuration details of resources, which is incredibly useful for debugging.

```
# Describe a specific pod in a namespace
kubectl describe pod <pod_name> -n <namespace-name>
```

#### Delete Resources
kubectl delete removes resources—be careful, as it’s irreversible. Specify resource types, namespaces, or names to avoid unintended deletions.
```
# Delete a specific pod in a namespace
kubectl delete pod <pod_name> -n <namespace-name>
```

#### Create Resources
Create resources with kubectl create. You can create deployments, services, and other resources from YAML or JSON files.
```
# Create a deployment from a YAML file
kubectl create -f deployment.yaml
```

#### Edit Resources
kubectl edit opens resources in your default editor, allowing you to modify configurations directly.
```
# Edit a deployment
kubectl edit deployment <deployment_name>
```

#### Apply Resources
kubectl apply creates or updates resources defined in a YAML file. It’s a declarative way to manage resources.
```
# Apply a configuration file
kubectl apply -f config.yaml
```

#### Using Selectors with field-selector
Select specific pods based on attributes like name, status, or labels.

```
# Get all running pods based on their status
kubectl get pods --field-selector=status.phase=Running
```

### Working with Pods
Pods are the smallest deployable units and a core component of Kubernetes objects. Managing and debugging pods is fundamental to understanding application behavior.

#### Retrieve Pod Logs
Logs are invaluable for tracking application performance and error handling.
```
# Get logs for a specific pod in a namespace
kubectl logs <pod_name> -n <namespace-name>
```

#### Running Commands Inside Pods
Run interactive commands to troubleshoot inside a container.

```
# Execute commands within a pod's container
kubectl exec -it <pod_name> -- /bin/bash
```

#### Monitor CPU and Memory Usage
Get real-time data on CPU and memory usage with kubectl top. This command works for both nodes and pods.
```
# Monitor CPU and memory usage for a specific pod
kubectl top pod <pod_name> -n <namespace-name>
```

### Deployments and Rollouts
Deployments manage workloads by scaling applications, applying updates, and rolling back changes.

#### Creating a Deployment
Quickly set up a deployment using a container image.
```
# Create a deployment with a specified container image
kubectl create deployment <deployment_name> --image=<container_image>
```

#### Manage Rollouts
Rollouts help update images and configuration settings seamlessly.
```
# Update the container image in a deployment and check the rollout status
kubectl set image deployment/<deployment_name> <container_name>=<new_image>
kubectl rollout status deployment/<deployment_name>
```

#### Scaling Deployments
kubectl scale adjusts the number of replicas in a deployment, ensuring that applications can handle changes in demand.
```
# Scale a deployment to the desired number of replicas
kubectl scale deployment <deployment_name> --replicas=<desired_number>
```

### Namespace Management
Namespaces in Kubernetes are like organizing folders on your computer. They allow you to separate environments and isolate resources.

#### Create a Namespace
Organize resources by creating namespaces for staging, testing, and production environments.

```
# Create a new namespace
kubectl create namespace <namespace-name>
```

#### List All Namespaces
Get an overview of all namespaces.
```
# List all namespaces in the cluster
kubectl get namespaces
```

#### Switch Namespace Context
Use the kubectl config command to set a default namespace context, simplifying commands.
```
# Set the current context to a specific namespace
kubectl config set-context --current --namespace=<namespace-name>
```

#### Advanced Configurations and Resource Management
Efficiently manage cluster settings and resource configurations with commands that allow inspection and updates on the fly.

### View Cluster Configurations
Display your active kubeconfig file that shows context, cluster information, and namespace preferences.
```
# View the active kubeconfig settings
kubectl config view
```

#### Edit Resources Directly
Use kubectl edit to make changes directly to resources. This command opens a text editor with the current YAML configuration.
```
# Edit a specific pod's configuration in a namespace
kubectl edit pod <pod_name> -n <namespace-name>
```

#### Annotate and Label Resources
Adding labels and annotations can be helpful for identification and filtering.

1. Add a label:
```
# Add a label to a specific pod
kubectl label pod <pod_name> env=production
```
2. Add an annotation:
```
# Add an annotation to a specific pod
kubectl annotate pod <pod_name> description="Backend pod for service A"
```

### Cluster Management
Here’s how to gather information and monitor your Kubernetes environment to keep the cluster in shape.

#### Cluster Info
Quickly check API server endpoints and basic information.
```
# Display basic information about the cluster
kubectl cluster-info
```

### Persistent Volumes
Persistent storage is essential for data that needs to outlast the lifecycle of a pod.
```
# Get a list of persistent volumes in the cluster
kubectl get persistentvolumes
```

#### Mark Nodes as Schedulable/Unschedulable
During maintenance, you can mark nodes as unschedulable to prevent new workloads from being assigned.
```
# Mark a node as unschedulable
kubectl cordon <node_name>

# Mark a node as schedulable again
kubectl uncordon <node_name>
```

### Monitoring and Port Forwarding
Use advanced commands to get resource data and test internal services.

#### Forward a Pod’s Port
Expose a pod’s port to your local machine for testing or debugging.
```
# Forward a pod's port to a local port
kubectl port-forward <pod_name> <local_port>:<remote_port> -n <namespace-name>
```

#### Monitor Resource Metrics
To see resource usage, such as CPU and memory, for nodes or pods, use kubectl top.
```
# Monitor resource metrics for nodes
kubectl top node
```

#### JSON and YAML Output
Display Kubernetes resource output in YAML or JSON formats, useful for saving configurations to files.
```
# Get a list of pods in YAML format
kubectl get pods -o yaml
```


### Interacting with the Kubernetes API Server
Explore available resources in the Kubernetes API.

#### List API Resources
Display all available resource types in the API.
```
# List all resource types in the Kubernetes API
kubectl api-resources
```

#### Filter Output with JSONPath
Use JSONPath to pull specific fields from resource output.
```
# Get the names of all pods using JSONPath
kubectl get pods -o jsonpath='{.items[*].metadata.name}'
```

## Tutorial

1. [Kubernetes Crash Course for Absolute Beginners](https://youtu.be/s_o8dwzRlu4?si=Bb2rWh8ql7ZMLwgI)