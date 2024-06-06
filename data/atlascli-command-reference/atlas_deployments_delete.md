## atlas deployments delete

Delete a deployment.


### Synopsis

The command prompts you to confirm the operation when you run the command without the --force option. 
		
Deleting an Atlas deployment also deletes any backup snapshots for that cluster.
Deleting a Local deployment also deletes any local data volumes.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas deployments delete <deploymentName> [flags]
atlas deployments rm <deploymentName> [flags]
atlas deployment delete <deploymentName> [flags]
atlas deployment rm <deploymentName> [flags]
```

### Examples

```
  # Remove an Atlas deployment named myDeployment after prompting for a confirmation:
  atlas deployments delete myDeployment --type ATLAS
  
  # Remove an Atlas deployment named myDeployment without requiring confirmation:
  atlas deployments delete myDeployment --type ATLAS --force

  # Remove an Local deployment named myDeployment without requiring confirmation:
  atlas deployments delete myDeployment --type LOCAL --force
```


### Flags

```
      --force               Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                help for delete
      --projectId string    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string         Type of deployment. Valid values are ATLAS or LOCAL.
  -w, --watch               Flag that indicates whether to watch the command until it completes its execution or the watch times out. To set the time that the watch times out, use the --watchTimeout option.
      --watchTimeout uint   Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments](atlas_deployments.md)	- Manage cloud and local deployments.



