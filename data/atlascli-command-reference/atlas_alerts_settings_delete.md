## atlas alerts settings delete

Remove the specified alert configuration for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas alerts settings delete <alertConfigId> [flags]
atlas alerts settings rm <alertConfigId> [flags]
atlas alerts config delete <alertConfigId> [flags]
atlas alerts config rm <alertConfigId> [flags]
atlas alert settings delete <alertConfigId> [flags]
atlas alert settings rm <alertConfigId> [flags]
atlas alert config delete <alertConfigId> [flags]
atlas alert config rm <alertConfigId> [flags]
```

### Examples

```
  # Remove the alert configuration with the ID 5d1113b25a115342acc2d1aa in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas alerts settings delete 5d1113b25a115342acc2d1aa --projectId 5e2211c17a3e5a48f5497de3
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


* [atlas alerts settings](atlas_alerts_settings.md)	- Manages alerts configuration for your project.



