## atlas privateEndpoints azure interfaces describe

Return the details for the specified Azure private endpoint interface for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints azure interfaces describe <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interfaces get <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interface describe <privateEndpointResourceId> [flags]
atlas privateEndpoints azure interface get <privateEndpointResourceId> [flags]
atlas privateendpoints azure interfaces describe <privateEndpointResourceId> [flags]
atlas privateendpoints azure interfaces get <privateEndpointResourceId> [flags]
atlas privateendpoints azure interface describe <privateEndpointResourceId> [flags]
atlas privateendpoints azure interface get <privateEndpointResourceId> [flags]
atlas private-endpoints azure interfaces describe <privateEndpointResourceId> [flags]
atlas private-endpoints azure interfaces get <privateEndpointResourceId> [flags]
atlas private-endpoints azure interface describe <privateEndpointResourceId> [flags]
atlas private-endpoints azure interface get <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interfaces describe <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interfaces get <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interface describe <privateEndpointResourceId> [flags]
atlas privateEndpoint azure interface get <privateEndpointResourceId> [flags]
atlas privateendpoint azure interfaces describe <privateEndpointResourceId> [flags]
atlas privateendpoint azure interfaces get <privateEndpointResourceId> [flags]
atlas privateendpoint azure interface describe <privateEndpointResourceId> [flags]
atlas privateendpoint azure interface get <privateEndpointResourceId> [flags]
atlas private-endpoint azure interfaces describe <privateEndpointResourceId> [flags]
atlas private-endpoint azure interfaces get <privateEndpointResourceId> [flags]
atlas private-endpoint azure interface describe <privateEndpointResourceId> [flags]
atlas private-endpoint azure interface get <privateEndpointResourceId> [flags]
```

### Examples

```
  # Return the JSON-formatted details of the Azure private endpoint interface with the ID /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/cli-test in Azure for an AWS private endpoint with the ID 5f4fc14da2b47835a58c63a2 in Atlas:
  atlas privateEndpoints azure interfaces describe /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/cli-test --endpointServiceId 5f4fc14da2b47835a58c63a2
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


* [atlas privateEndpoints azure interfaces](atlas_privateEndpoints_azure_interfaces.md)	- Manage Atlas Azure private endpoint interfaces.



