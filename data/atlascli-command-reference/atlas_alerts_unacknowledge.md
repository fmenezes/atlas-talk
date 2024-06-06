## atlas alerts unacknowledge

Unacknowledge the specified alert for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas alerts unacknowledge <alertId> [flags]
```

### Aliases
```

atlas alerts unacknowledge
atlas alerts unack
atlas alert unacknowledge
atlas alert unack
```

### Examples

```
  # Unacknowledge the alert with the ID 5d1113b25a115342acc2d1aa in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas alerts unacknowledge 5d1113b25a115342acc2d1aa --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --comment string     Optional description or comment for the entry.
  -h, --help               help for unacknowledge
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas alerts](atlas_alerts.md)	- Manage alerts for your project.



