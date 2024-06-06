## atlas clusters describe

Return the details for the specified cluster for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters describe <clusterName> [flags]
```

### Aliases
```

atlas clusters describe
atlas clusters get
atlas cluster describe
atlas cluster get
```

### Examples

```
  # Return the JSON-formatted details for the cluster named myCluster:
  atlas clusters describe myCluster --output json
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



