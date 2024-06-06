## atlas streams instances delete

Delete an Atlas Stream Processing instance.


### Synopsis

The command prompts you to confirm the operation when you run the command without the --force option.

Before deleting an Atlas Streams Processing instance, you must first stop all processes associated with it.
To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams instances delete <name> [flags]
atlas streams instances rm <name> [flags]
atlas streams instance delete <name> [flags]
atlas streams instance rm <name> [flags]
atlas stream instances delete <name> [flags]
atlas stream instances rm <name> [flags]
atlas stream instance delete <name> [flags]
atlas stream instance rm <name> [flags]
```

### Examples

```
  # Remove an Atlas Stream Processing instance after prompting for a confirmation:
  atlas streams instance delete myProcessorInstance

  # Remove an Atlas Stream Processing instance named myProcessorInstance without requiring confirmation:
  atlas streams instance delete myProcessorInstance --force
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



