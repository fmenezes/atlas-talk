## atlas streams instances create

Create an Atlas Stream Processing instance for your project


### Synopsis

To get started quickly, specify a name, a cloud provider, and a region to configure an Atlas Stream Processing instance.To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams instances create <name> [flags]
atlas streams instance create <name> [flags]
atlas stream instances create <name> [flags]
atlas stream instance create <name> [flags]
```

### Examples

```
  # Deploy an Atlas Stream Processing instance called myProcessor for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas streams instance create myProcessor --projectId 5e2211c17a3e5a48f5497de3 --provider AWS --region VIRGINIA_USA --tier SP30
```


### Flags

```
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string    Cloud service provider that applies to the provisioned Atlas Stream Processing instance. (default "AWS")
  -r, --region string      Human-readable label that identifies the physical location of your Atlas Stream Processing instance. The region can affect network latency and performance if it is far from your source or sink.
      --tier string        Tier for your Stream Instance. (default "SP30")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



