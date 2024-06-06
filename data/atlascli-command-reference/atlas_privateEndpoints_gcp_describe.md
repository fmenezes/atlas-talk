## atlas privateEndpoints gcp describe

Return a specific GCP private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints gcp describe <privateEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints gcp describe
atlas privateEndpoints gcp get
atlas privateendpoints gcp describe
atlas privateendpoints gcp get
atlas private-endpoints gcp describe
atlas private-endpoints gcp get
atlas privateEndpoint gcp describe
atlas privateEndpoint gcp get
atlas privateendpoint gcp describe
atlas privateendpoint gcp get
atlas private-endpoint gcp describe
atlas private-endpoint gcp get
```

### Examples

```
  atlas privateEndpoint gcp describe vpce-abcdefg0123456789
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


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



