## atlas privateEndpoints aws describe

Return the details for the specified AWS private endpoints for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints aws describe <privateEndpointId> [flags]
atlas privateEndpoints aws get <privateEndpointId> [flags]
atlas privateendpoints aws describe <privateEndpointId> [flags]
atlas privateendpoints aws get <privateEndpointId> [flags]
atlas private-endpoints aws describe <privateEndpointId> [flags]
atlas private-endpoints aws get <privateEndpointId> [flags]
atlas privateEndpoint aws describe <privateEndpointId> [flags]
atlas privateEndpoint aws get <privateEndpointId> [flags]
atlas privateendpoint aws describe <privateEndpointId> [flags]
atlas privateendpoint aws get <privateEndpointId> [flags]
atlas private-endpoint aws describe <privateEndpointId> [flags]
atlas private-endpoint aws get <privateEndpointId> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the AWS private endpoint connection with the ID 5f4fc81c1f03a835c2728ff7 for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws describe 5f4fc81c1f03a835c2728ff7 --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



