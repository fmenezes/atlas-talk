## atlas integrations list

Return all active third-party integrations for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas integrations list [flags]
```

### Aliases
```

atlas integrations list
atlas integrations ls
atlas integration list
atlas integration ls
```

### Examples

```
  # Return a JSON-formatted list of active third-party integrations for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations list --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas integrations](atlas_integrations.md)	- Configure third-party integrations for your Atlas project.



