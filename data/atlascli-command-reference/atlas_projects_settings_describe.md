## atlas projects settings describe

Retrieve details for settings to the specified project.


### Usage
```
atlas projects settings describe [flags]
```

### Aliases
```

atlas projects settings describe
atlas projects settings get
atlas projects setting describe
atlas projects setting get
atlas project settings describe
atlas project settings get
atlas project setting describe
atlas project setting get
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

### See Also


* [atlas projects settings](atlas_projects_settings.md)	- Settings operations.



