## atlas processes describe

Return the details for the specified MongoDB process for your project.



```

atlas processes describe <hostname:port> [flags]
atlas process describe <hostname:port> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the MongoDB process with hostname and port atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017
  atlas process describe atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 --output json
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


* [atlas processes](atlas_processes.md)	- Manage MongoDB processes for your project.



