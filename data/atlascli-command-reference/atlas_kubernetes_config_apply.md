## atlas kubernetes config apply

Generate and apply Kubernetes configuration resources for use with Atlas Kubernetes Operator.


### Synopsis

This command exports configurations for Atlas objects including projects, deployments, and users directly into Kubernetes, allowing you to manage these resources using the Atlas Kubernetes Operator. For more information, see https://www.mongodb.com/docs/atlas/atlas-operator/.


### Usage
```
atlas kubernetes config apply [flags]
```

### Aliases
```

atlas kubernetes config apply
```

### Examples

```
# Export and apply all supported resources of a specific project:
  atlas kubernetes config apply --projectId=<projectId>

  # Export and apply all supported resources of a specific project and to a specific namespace:
  atlas kubernetes config apply --projectId=<projectId> --targetNamespace=<namespace>
  
  # Export and apply all supported Project resource, and only the described Deployment resources of a specific project to a specific namespace:
  atlas kubernetes config apply --projectId=<projectId> --clusterName=<cluster-name-1, cluster-name-2> --targetNamespace=<namespace>

  # Export and apply all supported resources of a specific project to a specific namespace restricting the version of the Atlas Kubernetes Operator:
  atlas kubernetes config apply --projectId=<projectId> --targetNamespace=<namespace> --operatorVersion=1.5.1
```


### Flags

```
      --clusterName strings      One or more comma separated cluster names to import
  -h, --help                     help for apply
      --kubeContext string       Name of the kubeconfig context to use.
      --kubeconfig string        Path to the kubeconfig file to use for CLI requests.
      --operatorVersion string   Version of Atlas Kubernetes Operator to generate resources for.
      --orgId string             Organization ID to use. This option overrides the settings in the configuration file or environment variable.
      --projectId string         Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --targetNamespace string   Namespaces to use for generated kubernetes entities

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas kubernetes config](atlas_kubernetes_config.md)	- Manage Kubernetes configuration resources.



