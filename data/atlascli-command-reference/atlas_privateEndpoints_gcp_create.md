## atlas privateEndpoints gcp create

Create a new GCP private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints gcp create [flags]
```

### Aliases
```

atlas privateEndpoints gcp create
atlas privateendpoints gcp create
atlas private-endpoints gcp create
atlas privateEndpoint gcp create
atlas privateendpoint gcp create
atlas private-endpoint gcp create
```

### Examples

```
  atlas privateEndpoints gcp create --region CENTRAL_US
```


### Flags

```
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string      Cloud provider region in which you want to create the private endpoint connection. For a complete list of supported AWS regions, see: https://dochub.mongodb.org/core/aws-atlas. For a complete list of supported Azure regions, see: https://dochub.mongodb.org/core/azure-atlas. For a complete list of supported GCP regions, see: https://dochub.mongodb.org/core/gcp-atlas.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



