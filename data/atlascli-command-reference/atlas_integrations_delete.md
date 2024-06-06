## atlas integrations delete

Remove the specified third-party integration from your project.


### Synopsis

Deleting an integration from a project removes that integration configuration only for that project. This does not affect any other project or organization's configured integrations.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas integrations delete <integrationType> [flags]
```

### Aliases
```

atlas integrations delete
atlas integrations rm
atlas integration delete
atlas integration rm
```

### Examples

```
  # Remove the Datadog integration for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations delete DATADOG --projectId 5e2211c17a3e5a48f5497de3
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

### See Also


* [atlas integrations](atlas_integrations.md)	- Configure third-party integrations for your Atlas project.



