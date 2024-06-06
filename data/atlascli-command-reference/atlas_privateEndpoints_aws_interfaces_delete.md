## atlas privateEndpoints aws interfaces delete

Remove the specified AWS private endpoint interface and related service from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints aws interfaces delete <interfaceEndpointId> [flags]
atlas privateEndpoints aws interfaces rm <interfaceEndpointId> [flags]
atlas privateEndpoints aws interface delete <interfaceEndpointId> [flags]
atlas privateEndpoints aws interface rm <interfaceEndpointId> [flags]
atlas privateendpoints aws interfaces delete <interfaceEndpointId> [flags]
atlas privateendpoints aws interfaces rm <interfaceEndpointId> [flags]
atlas privateendpoints aws interface delete <interfaceEndpointId> [flags]
atlas privateendpoints aws interface rm <interfaceEndpointId> [flags]
atlas private-endpoints aws interfaces delete <interfaceEndpointId> [flags]
atlas private-endpoints aws interfaces rm <interfaceEndpointId> [flags]
atlas private-endpoints aws interface delete <interfaceEndpointId> [flags]
atlas private-endpoints aws interface rm <interfaceEndpointId> [flags]
atlas privateEndpoint aws interfaces delete <interfaceEndpointId> [flags]
atlas privateEndpoint aws interfaces rm <interfaceEndpointId> [flags]
atlas privateEndpoint aws interface delete <interfaceEndpointId> [flags]
atlas privateEndpoint aws interface rm <interfaceEndpointId> [flags]
atlas privateendpoint aws interfaces delete <interfaceEndpointId> [flags]
atlas privateendpoint aws interfaces rm <interfaceEndpointId> [flags]
atlas privateendpoint aws interface delete <interfaceEndpointId> [flags]
atlas privateendpoint aws interface rm <interfaceEndpointId> [flags]
atlas private-endpoint aws interfaces delete <interfaceEndpointId> [flags]
atlas private-endpoint aws interfaces rm <interfaceEndpointId> [flags]
atlas private-endpoint aws interface delete <interfaceEndpointId> [flags]
atlas private-endpoint aws interface rm <interfaceEndpointId> [flags]
```

### Examples

```
  # Remove the AWS private endpoint interface with the ID vpce-00713b5e644e830a3 in AWS from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws interfaces delete vpce-00713b5e644e830a3 --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --endpointServiceId string   Unique 24-character alphanumeric string that identifies the private endpoint in Atlas.
      --force                      Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                       help for delete
      --projectId string           Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints aws interfaces](atlas_privateEndpoints_aws_interfaces.md)	- Manage Atlas AWS private endpoint interfaces.



