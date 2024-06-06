## atlas privateEndpoints azure describe

Return the details for the specified Azure private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints azure describe <privateEndpointId> [flags]
atlas privateEndpoints azure get <privateEndpointId> [flags]
atlas privateendpoints azure describe <privateEndpointId> [flags]
atlas privateendpoints azure get <privateEndpointId> [flags]
atlas private-endpoints azure describe <privateEndpointId> [flags]
atlas private-endpoints azure get <privateEndpointId> [flags]
atlas privateEndpoint azure describe <privateEndpointId> [flags]
atlas privateEndpoint azure get <privateEndpointId> [flags]
atlas privateendpoint azure describe <privateEndpointId> [flags]
atlas privateendpoint azure get <privateEndpointId> [flags]
atlas private-endpoint azure describe <privateEndpointId> [flags]
atlas private-endpoint azure get <privateEndpointId> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the Azure private endpoint connection with the ID 5f4fc81c1f03a835c2728ff7 for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints azure describe 5f4fc81c1f03a835c2728ff7 --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas privateEndpoints azure](atlas_privateEndpoints_azure.md)	- Manage Azure Private Endpoints.



