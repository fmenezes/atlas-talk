## atlas privateEndpoints gcp describe

Return a specific GCP private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints gcp describe <privateEndpointId> [flags]
atlas privateEndpoints gcp get <privateEndpointId> [flags]
atlas privateendpoints gcp describe <privateEndpointId> [flags]
atlas privateendpoints gcp get <privateEndpointId> [flags]
atlas private-endpoints gcp describe <privateEndpointId> [flags]
atlas private-endpoints gcp get <privateEndpointId> [flags]
atlas privateEndpoint gcp describe <privateEndpointId> [flags]
atlas privateEndpoint gcp get <privateEndpointId> [flags]
atlas privateendpoint gcp describe <privateEndpointId> [flags]
atlas privateendpoint gcp get <privateEndpointId> [flags]
atlas private-endpoint gcp describe <privateEndpointId> [flags]
atlas private-endpoint gcp get <privateEndpointId> [flags]
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

### SEE ALSO


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



