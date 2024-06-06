## atlas clusters watch

Watch the specified cluster in your project until it becomes available.


### Synopsis

This command checks the cluster's status periodically until it reaches an IDLE state. 
Once the cluster reaches the expected state, the command prints "Cluster available."
If you run the command in the terminal, it blocks the terminal session until the resource state changes to IDLE.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters watch <clusterName> [flags]
```

### Aliases
```

atlas clusters watch
atlas cluster watch
```

### Examples

```
  # Watch for the cluster named myCluster to become available for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas clusters watch myCluster --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for watch
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



