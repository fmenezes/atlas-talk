## atlas auditing describe

Returns the auditing configuration for the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas auditing describe [flags]
atlas auditing get [flags]
```

### Examples

```
  # Return the JSON-formatted details for the default project:
  atlas auditing describe --output json
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


* [atlas auditing](atlas_auditing.md)	- Returns database auditing settings for MongoDB Cloud projects.



