## atlas clusters sampleData watch

Watch the specified sample data job in your cluster until it completes.


### Synopsis

This command checks the sample data job's status periodically until it reaches an COMPLETED state. 
If you run the command in the terminal, it blocks the terminal session until the resource state changes to COMPLETED.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters sampleData watch <id> [flags]
atlas clusters sampledata watch <id> [flags]
atlas clusters sample-data watch <id> [flags]
atlas clusters sampleDatum watch <id> [flags]
atlas clusters sampledatum watch <id> [flags]
atlas clusters sample-datum watch <id> [flags]
atlas cluster sampleData watch <id> [flags]
atlas cluster sampledata watch <id> [flags]
atlas cluster sample-data watch <id> [flags]
atlas cluster sampleDatum watch <id> [flags]
atlas cluster sampledatum watch <id> [flags]
atlas cluster sample-datum watch <id> [flags]
```

### Examples

```
  # Watch for the sample data job with ID 5e2211c17a3e5a48f5497de3 to complete:
  atlas clusters sampledata watch 5e2211c17a3e5a48f5497de3
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

### SEE ALSO


* [atlas clusters sampleData](atlas_clusters_sampleData.md)	- Manage sample data for your cluster.



