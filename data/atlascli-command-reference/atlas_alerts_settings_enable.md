## atlas alerts settings enable

Enables one alert configuration for the specified project.



```

atlas alerts settings enable <alertConfigId> [flags]
atlas alerts config enable <alertConfigId> [flags]
atlas alert settings enable <alertConfigId> [flags]
atlas alert config enable <alertConfigId> [flags]
```

### Examples

```
  # Enable the alert configuration with the ID 5d1113b25a115342acc2d1aa in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas alerts settings enable 5d1113b25a115342acc2d1aa --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for enable
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas alerts settings](atlas_alerts_settings.md)	- Manages alerts configuration for your project.



