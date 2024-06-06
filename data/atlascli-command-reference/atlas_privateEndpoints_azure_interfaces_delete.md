## atlas privateEndpoints azure interfaces delete

Remove the specified Azure private endpoint interface and related service from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints azure interfaces delete <privateEndpointResourceId> [flags]
```

### Aliases
```

atlas privateEndpoints azure interfaces delete
atlas privateEndpoints azure interfaces rm
atlas privateEndpoints azure interface delete
atlas privateEndpoints azure interface rm
atlas privateendpoints azure interfaces delete
atlas privateendpoints azure interfaces rm
atlas privateendpoints azure interface delete
atlas privateendpoints azure interface rm
atlas private-endpoints azure interfaces delete
atlas private-endpoints azure interfaces rm
atlas private-endpoints azure interface delete
atlas private-endpoints azure interface rm
atlas privateEndpoint azure interfaces delete
atlas privateEndpoint azure interfaces rm
atlas privateEndpoint azure interface delete
atlas privateEndpoint azure interface rm
atlas privateendpoint azure interfaces delete
atlas privateendpoint azure interfaces rm
atlas privateendpoint azure interface delete
atlas privateendpoint azure interface rm
atlas private-endpoint azure interfaces delete
atlas private-endpoint azure interfaces rm
atlas private-endpoint azure interface delete
atlas private-endpoint azure interface rm
```

### Examples

```
  # Remove the Azure private endpoint interface with the ID /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/cli-test in Azure from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints azure interfaces delete /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/cli-test --projectId 5e2211c17a3e5a48f5497de3
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


* [atlas privateEndpoints azure interfaces](atlas_privateEndpoints_azure_interfaces.md)	- Manage Atlas Azure private endpoint interfaces.



