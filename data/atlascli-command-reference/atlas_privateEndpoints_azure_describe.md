## atlas privateEndpoints azure describe

Return the details for the specified Azure private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints azure describe <privateEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints azure describe
atlas privateEndpoints azure get
atlas privateendpoints azure describe
atlas privateendpoints azure get
atlas private-endpoints azure describe
atlas private-endpoints azure get
atlas privateEndpoint azure describe
atlas privateEndpoint azure get
atlas privateendpoint azure describe
atlas privateendpoint azure get
atlas private-endpoint azure describe
atlas private-endpoint azure get
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

### See Also


* [atlas privateEndpoints azure](atlas_privateEndpoints_azure.md)	- Manage Azure Private Endpoints.



