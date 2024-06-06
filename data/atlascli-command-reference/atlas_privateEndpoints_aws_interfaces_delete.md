## atlas privateEndpoints aws interfaces delete

Remove the specified AWS private endpoint interface and related service from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints aws interfaces delete <interfaceEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints aws interfaces delete
atlas privateEndpoints aws interfaces rm
atlas privateEndpoints aws interface delete
atlas privateEndpoints aws interface rm
atlas privateendpoints aws interfaces delete
atlas privateendpoints aws interfaces rm
atlas privateendpoints aws interface delete
atlas privateendpoints aws interface rm
atlas private-endpoints aws interfaces delete
atlas private-endpoints aws interfaces rm
atlas private-endpoints aws interface delete
atlas private-endpoints aws interface rm
atlas privateEndpoint aws interfaces delete
atlas privateEndpoint aws interfaces rm
atlas privateEndpoint aws interface delete
atlas privateEndpoint aws interface rm
atlas privateendpoint aws interfaces delete
atlas privateendpoint aws interfaces rm
atlas privateendpoint aws interface delete
atlas privateendpoint aws interface rm
atlas private-endpoint aws interfaces delete
atlas private-endpoint aws interfaces rm
atlas private-endpoint aws interface delete
atlas private-endpoint aws interface rm
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

### See Also


* [atlas privateEndpoints aws interfaces](atlas_privateEndpoints_aws_interfaces.md)	- Manage Atlas AWS private endpoint interfaces.



