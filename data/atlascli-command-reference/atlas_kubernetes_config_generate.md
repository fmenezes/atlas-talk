## atlas kubernetes config generate

Generate Kubernetes configuration resources for use with Atlas Kubernetes Operator.


### Synopsis

This command exports configurations for Atlas objects including projects, deployments, and users in a Kubernetes-compatible format, allowing you to manage these resources using the Atlas Kubernetes Operator. For more information, see https://www.mongodb.com/docs/atlas/atlas-operator/



```

atlas kubernetes config generate [flags]
```

### Examples

```
# Export Project, DatabaseUsers, Deployments resources for a specific project without connection and integration secrets:
  atlas kubernetes config generate --projectId=<projectId>

  # Export Project, DatabaseUsers, Deployments resources for a specific project including connection and integration secrets:
  atlas kubernetes config generate --projectId=<projectId> --includeSecrets

  # Export Project, DatabaseUsers, Deployments resources for a specific project including connection and integration secrets to a specific namespace:
  atlas kubernetes config generate --projectId=<projectId> --includeSecrets --targetNamespace=<namespace>

  # Export Project, DatabaseUsers, DataFederations and specific Deployment resources for a specific project including connection and integration secrets to a specific namespace:
  atlas kubernetes config generate --projectId=<projectId> --clusterName=<cluster-name-1, cluster-name-2> --includeSecrets --targetNamespace=<namespace>

  # Export resources for a specific version of the Atlas Kubernetes Operator:
  atlas kubernetes config generate --projectId=<projectId> --targetNamespace=<namespace> --operatorVersion=1.5.1

  # Export Project, DatabaseUsers, Clusters and specific DataFederation resources for a specific project to a specific namespace:
  atlas kubernetes config generate --projectId=<projectId> --dataFederationName=<data-federation-name-1, data-federation-name-2> --targetNamespace=<namespace>
```


### Flags

```
      --clusterName strings          One or more comma separated cluster names to import
      --dataFederationName strings   One or more comma separated data federation names to import
  -h, --help                         help for generate
      --includeSecrets               Flag that generates kubernetes secrets with data for projects, users, deployments entities.
      --operatorVersion string       Version of Atlas Kubernetes Operator to generate resources for. (default "2.2.0")
      --orgId string                 Organization ID to use. This option overrides the settings in the configuration file or environment variable.
      --projectId string             Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --targetNamespace string       Namespaces to use for generated kubernetes entities

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas kubernetes config](atlas_kubernetes_config.md)	- Manage Kubernetes configuration resources.



