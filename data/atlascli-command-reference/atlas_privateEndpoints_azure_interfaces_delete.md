## atlas privateEndpoints azure interfaces delete

Remove the specified Azure private endpoint interface and related service from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints azure interfaces delete <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interfaces rm <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interface delete <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interface rm <privateEndpointResourceId> [flags]
atlas privateendpoints azure interfaces delete <privateEndpointResourceId> [flags]
atlas privateendpoints azure interfaces rm <privateEndpointResourceId> [flags]
atlas privateendpoints azure interface delete <privateEndpointResourceId> [flags]
atlas privateendpoints azure interface rm <privateEndpointResourceId> [flags]
atlas private-endpoints azure interfaces delete <privateEndpointResourceId> [flags]
atlas private-endpoints azure interfaces rm <privateEndpointResourceId> [flags]
atlas private-endpoints azure interface delete <privateEndpointResourceId> [flags]
atlas private-endpoints azure interface rm <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interfaces delete <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interfaces rm <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interface delete <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interface rm <privateEndpointResourceId> [flags]
atlas privateendpoint azure interfaces delete <privateEndpointResourceId> [flags]
atlas privateendpoint azure interfaces rm <privateEndpointResourceId> [flags]
atlas privateendpoint azure interface delete <privateEndpointResourceId> [flags]
atlas privateendpoint azure interface rm <privateEndpointResourceId> [flags]
atlas private-endpoint azure interfaces delete <privateEndpointResourceId> [flags]
atlas private-endpoint azure interfaces rm <privateEndpointResourceId> [flags]
atlas private-endpoint azure interface delete <privateEndpointResourceId> [flags]
atlas private-endpoint azure interface rm <privateEndpointResourceId> [flags]
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

### SEE ALSO


* [atlas privateEndpoints azure interfaces](atlas_privateEndpoints_azure_interfaces.md)	- Manage Atlas Azure private endpoint interfaces.



