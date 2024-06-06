## atlas privateEndpoints aws interfaces create

Create a new interface for the specified AWS private endpoint.


### Synopsis

To learn more about how to set up private endpoints with the Atlas CLI, see the tutorial on the Atlas CLI tab here: https://www.mongodb.com/docs/atlas/security-cluster-private-endpoint/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints aws interfaces create <endpointServiceId> [flags]
```

### Aliases
```

atlas privateEndpoints aws interfaces create
atlas privateEndpoints aws interfaces add
atlas privateEndpoints aws interface create
atlas privateEndpoints aws interface add
atlas privateendpoints aws interfaces create
atlas privateendpoints aws interfaces add
atlas privateendpoints aws interface create
atlas privateendpoints aws interface add
atlas private-endpoints aws interfaces create
atlas private-endpoints aws interfaces add
atlas private-endpoints aws interface create
atlas private-endpoints aws interface add
atlas privateEndpoint aws interfaces create
atlas privateEndpoint aws interfaces add
atlas privateEndpoint aws interface create
atlas privateEndpoint aws interface add
atlas privateendpoint aws interfaces create
atlas privateendpoint aws interfaces add
atlas privateendpoint aws interface create
atlas privateendpoint aws interface add
atlas private-endpoint aws interfaces create
atlas private-endpoint aws interfaces add
atlas private-endpoint aws interface create
atlas private-endpoint aws interface add
```

### Examples

```
  # Create a new interface for an AWS private endpoint with the ID 5f4fc14da2b47835a58c63a2 in Atlas and the ID vpce-00713b5e644e830a3 in AWS for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws interfaces create 5f4fc14da2b47835a58c63a2 --privateEndpointId vpce-00713b5e644e830a3 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help                       help for create
  -o, --output string              Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --privateEndpointId string   Unique 22-character alphanumeric string that identifies the AWS PrivateLink connection in AWS. You can find this value on the AWS VPC Dashboard under Endpoints > VPC ID.
      --projectId string           Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas privateEndpoints aws interfaces](atlas_privateEndpoints_aws_interfaces.md)	- Manage Atlas AWS private endpoint interfaces.



