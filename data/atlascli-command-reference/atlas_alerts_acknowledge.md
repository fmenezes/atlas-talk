## atlas alerts acknowledge

Acknowledges the specified alert for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas alerts acknowledge <alertId> [flags]
atlas alerts ack <alertId> [flags]
atlas alert acknowledge <alertId> [flags]
atlas alert ack <alertId> [flags]
```

### Examples

```
  # Acknowledge an alert with the ID 5d1113b25a115342acc2d1aa in the project with the ID 5e2211c17a3e5a48f5497de3 until January 1 2028:
  atlas alerts acknowledge 5d1113b25a115342acc2d1aa --until 2028-01-01T20:24:26Z --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --comment string     Optional description or comment for the entry.
  -F, --forever            Option that acknowledges an alert 'forever'. You can't set both the forever option and the until option in the same command.
  -h, --help               help for acknowledge
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --until string       ISO 8601-formatted time until which the alert is acknowledged. This command returns this value if a MongoDB user previously acknowledged the alert. After this date, the alert becomes unacknowledged.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas alerts](atlas_alerts.md)	- Manage alerts for your project.



