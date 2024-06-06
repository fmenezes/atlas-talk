## atlas dataFederation delete

Remove the specified data federation database from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation delete <name> [flags]
atlas datafederation delete <name> [flags]
atlas data-federation delete <name> [flags]
```

### Examples

```
# deletes data federation 'DataFederation1':
  atlas dataFederation delete DataFederation1

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


* [atlas dataFederation](atlas_dataFederation.md)	- Data federation.



