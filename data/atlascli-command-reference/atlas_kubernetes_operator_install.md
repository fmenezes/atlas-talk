## atlas kubernetes operator install

Install Atlas Kubernetes Operator to a cluster.


### Synopsis

This command installs a supported version of Atlas Kubernetes Operator to an existing cluster, and optionally imports Atlas resources that are managed by the operator.

This command creates an API key for the Operator and adds it to Kubernetes as a secret, which the Operator then uses to make Atlas Admin API calls.
The key is scoped to the project when you specify the --projectName option and to the organization when you omit the --projectName option.



```

atlas kubernetes operator install [flags]
```

### Examples

```
# Install latest version of the operator into the default namespace:
  atlas kubernetes operator install

  # Install the latest version of the operator targeting Atlas for Government instead of regular commercial Atlas:
  atlas kubernetes operator install --atlasGov

  # Install a specific version of the operator:
  atlas kubernetes operator install --operatorVersion=1.7.0

  # Install a specific version of the operator to a namespace and watch only this namespace and a second one:
  atlas kubernetes operator install --operatorVersion=1.7.0 --targetNamespace=<namespace> --watchNamespace=<namespace>,<secondNamespace>

  # Install and import all objects from an organization:
  atlas kubernetes operator install --targetNamespace=<namespace> --orgID <orgID> --import

  # Install and import objects from a specific project:
  atlas kubernetes operator install --targetNamespace=<namespace> --orgID <orgID> --projectName <project> --import

	# Install the operator and disable deletion protection:
	atlas kubernetes operator install --resourceDeletionProtection=false

	# Install the operator and disable deletion protection for sub-resources (Atlas project integrations, private endpoints, etc.):
	atlas kubernetes operator install --subresourceDeletionProtection=false
```


### Flags

```
      --atlasGov                        Flag that indicates whether to configure Atlas for Government as a target of the operator.
  -h, --help                            help for install
      --import                          Flag that indicates whether to import existing Atlas resources into the cluster for the operator to manage.
      --kubeContext string              Name of the kubeconfig context to use.
      --kubeconfig string               Path to the kubeconfig file to use for CLI requests.
      --operatorVersion string          Version of the operator to install.
      --orgId string                    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
      --projectName string              Name of the project to create or use with the installed operator.
      --resourceDeletionProtection      Toggle atlas operator deletion protection for resources like Projects, Deployments, etc. Read more: https://dochub.mongodb.org/core/ako-deletion-protection (default true)
      --subresourceDeletionProtection   Toggle atlas operator deletion protection for subresources like Alerts, Integrations, etc. Read more: https://dochub.mongodb.org/core/ako-deletion-protection (default true)
      --targetNamespace string          Namespace where to install the operator.
      --watchNamespace strings          List that contains namespaces that the operator will listen to.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas kubernetes operator](atlas_kubernetes_operator.md)	- Manage Atlas Kubernetes Operator.



