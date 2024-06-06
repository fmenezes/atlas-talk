## atlas clusters delete

Remove the specified cluster from your project.


### Synopsis

The command prompts you to confirm the operation when you run the command without the --force option. 
		
Deleting a cluster also deletes any backup snapshots for that cluster.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas clusters delete <clusterName> [flags]
atlas clusters rm <clusterName> [flags]
atlas cluster delete <clusterName> [flags]
atlas cluster rm <clusterName> [flags]
```

### Examples

```
  # Remove a cluster named myCluster after prompting for a confirmation:
  atlas clusters delete myCluster
  
  # Remove a cluster named myCluster without requiring confirmation:
  atlas clusters delete myCluster --force
```


### Flags

```
      --force               Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                help for delete
      --projectId string    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
  -w, --watch               Flag that indicates whether to watch the command until it completes its execution or the watch times out. To set the time that the watch times out, use the --watchTimeout option.
      --watchTimeout uint   Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



