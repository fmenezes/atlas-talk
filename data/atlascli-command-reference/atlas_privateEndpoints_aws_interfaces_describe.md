## atlas privateEndpoints aws interfaces describe

Return the details for the specified AWS private endpoint interface for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints aws interfaces describe <interfaceEndpointId> [flags]
atlas privateEndpoints aws interfaces get <interfaceEndpointId> [flags]
atlas privateEndpoints aws interface describe <interfaceEndpointId> [flags]
atlas privateEndpoints aws interface get <interfaceEndpointId> [flags]
atlas privateendpoints aws interfaces describe <interfaceEndpointId> [flags]
atlas privateendpoints aws interfaces get <interfaceEndpointId> [flags]
atlas privateendpoints aws interface describe <interfaceEndpointId> [flags]
atlas privateendpoints aws interface get <interfaceEndpointId> [flags]
atlas private-endpoints aws interfaces describe <interfaceEndpointId> [flags]
atlas private-endpoints aws interfaces get <interfaceEndpointId> [flags]
atlas private-endpoints aws interface describe <interfaceEndpointId> [flags]
atlas private-endpoints aws interface get <interfaceEndpointId> [flags]
atlas privateEndpoint aws interfaces describe <interfaceEndpointId> [flags]
atlas privateEndpoint aws interfaces get <interfaceEndpointId> [flags]
atlas privateEndpoint aws interface describe <interfaceEndpointId> [flags]
atlas privateEndpoint aws interface get <interfaceEndpointId> [flags]
atlas privateendpoint aws interfaces describe <interfaceEndpointId> [flags]
atlas privateendpoint aws interfaces get <interfaceEndpointId> [flags]
atlas privateendpoint aws interface describe <interfaceEndpointId> [flags]
atlas privateendpoint aws interface get <interfaceEndpointId> [flags]
atlas private-endpoint aws interfaces describe <interfaceEndpointId> [flags]
atlas private-endpoint aws interfaces get <interfaceEndpointId> [flags]
atlas private-endpoint aws interface describe <interfaceEndpointId> [flags]
atlas private-endpoint aws interface get <interfaceEndpointId> [flags]
```

### Examples

```
  # Return the JSON-formatted details of the AWS private endpoint interface with the ID 	
		vpce-00713b5e644e830a3 in AWS for an AWS private endpoint with the ID 5f4fc14da2b47835a58c63a2 in Atlas:
  atlas privateEndpoints aws interfaces describe 	
  vpce-00713b5e644e830a3 --endpointServiceId 5f4fc14da2b47835a58c63a2
```


### Flags

```
      --endpointServiceId string   Unique 24-character alphanumeric string that identifies the private endpoint in Atlas.
  -h, --help                       help for describe
  -o, --output string              Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string           Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints aws interfaces](atlas_privateEndpoints_aws_interfaces.md)	- Manage Atlas AWS private endpoint interfaces.



