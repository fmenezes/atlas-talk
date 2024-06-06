## atlas streams instances describe

Describe an Atlas Stream Processing instance for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas streams instances describe <name> [flags]
```

### Aliases
```

atlas streams instances describe
atlas streams instance describe
atlas stream instances describe
atlas stream instance describe
```

### Examples

```
  # Return an Atlas Stream Processing instance with a specific name:
  atlas streams instance describe myProcessor
  # Return a JSON-formatted Atlas Stream Processing instance with a specific name:
  atlas streams instance describe myProcessor --output json
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


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



