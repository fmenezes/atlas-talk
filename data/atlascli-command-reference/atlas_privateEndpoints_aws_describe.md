## atlas privateEndpoints aws describe

Return the details for the specified AWS private endpoints for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints aws describe <privateEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints aws describe
atlas privateEndpoints aws get
atlas privateendpoints aws describe
atlas privateendpoints aws get
atlas private-endpoints aws describe
atlas private-endpoints aws get
atlas privateEndpoint aws describe
atlas privateEndpoint aws get
atlas privateendpoint aws describe
atlas privateendpoint aws get
atlas private-endpoint aws describe
atlas private-endpoint aws get
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

### See Also


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



