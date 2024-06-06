## atlas projects settings describe

Retrieve details for settings to the specified project.



```

atlas projects settings describe [flags]
atlas projects settings get [flags]
atlas projects setting describe [flags]
atlas projects setting get [flags]
atlas project settings describe [flags]
atlas project settings get [flags]
atlas project setting describe [flags]
atlas project setting get [flags]
```

### Examples

```
  # This example uses the profile named "myprofile" for accessing Atlas.
  atlas projects settings describe -P myprofile --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas projects settings](atlas_projects_settings.md)	- Settings operations.



