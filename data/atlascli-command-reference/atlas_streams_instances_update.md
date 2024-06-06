## atlas streams instances update

Updates an Atlas Stream Processing instance for your project.


### Synopsis

Before updating an Atlas Streams Processing instance, you must first stop all processes associated with it.
To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams instances update <name> [flags]
atlas streams instance update <name> [flags]
atlas stream instances update <name> [flags]
atlas stream instance update <name> [flags]
```

### Examples

```
  # Modify the Atlas Stream Processing instance configuration with the name MyInstance:
  atlas streams instance update MyInstance --provider AWS --region VIRGINIA_USA
```


### Flags

```
  -h, --help               help for update
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string    Cloud service provider that applies to the provisioned Atlas Stream Processing instance. (default "AWS")
  -r, --region string      Human-readable label that identifies the physical location of your Atlas Stream Processing instance. The region can affect network latency and performance if it is far from your source or sink.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



