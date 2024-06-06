## atlas privateEndpoints azure interfaces create

Create a new interface for the specified Azure private endpoint.


### Synopsis

To learn more about how to set up private endpoints with the Atlas CLI, see the tutorial on the Atlas CLI tab here: https://www.mongodb.com/docs/atlas/security-cluster-private-endpoint/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints azure interfaces create <endpointServiceId> [flags]
atlas privateEndpoints azure interfaces add <endpointServiceId> [flags]
atlas privateEndpoints azure interface create <endpointServiceId> [flags]
atlas privateEndpoints azure interface add <endpointServiceId> [flags]
atlas privateendpoints azure interfaces create <endpointServiceId> [flags]
atlas privateendpoints azure interfaces add <endpointServiceId> [flags]
atlas privateendpoints azure interface create <endpointServiceId> [flags]
atlas privateendpoints azure interface add <endpointServiceId> [flags]
atlas private-endpoints azure interfaces create <endpointServiceId> [flags]
atlas private-endpoints azure interfaces add <endpointServiceId> [flags]
atlas private-endpoints azure interface create <endpointServiceId> [flags]
atlas private-endpoints azure interface add <endpointServiceId> [flags]
atlas privateEndpoint azure interfaces create <endpointServiceId> [flags]
atlas privateEndpoint azure interfaces add <endpointServiceId> [flags]
atlas privateEndpoint azure interface create <endpointServiceId> [flags]
atlas privateEndpoint azure interface add <endpointServiceId> [flags]
atlas privateendpoint azure interfaces create <endpointServiceId> [flags]
atlas privateendpoint azure interfaces add <endpointServiceId> [flags]
atlas privateendpoint azure interface create <endpointServiceId> [flags]
atlas privateendpoint azure interface add <endpointServiceId> [flags]
atlas private-endpoint azure interfaces create <endpointServiceId> [flags]
atlas private-endpoint azure interfaces add <endpointServiceId> [flags]
atlas private-endpoint azure interface create <endpointServiceId> [flags]
atlas private-endpoint azure interface add <endpointServiceId> [flags]
```

### Examples

```
  # Create a new interface for an Azure private endpoint with the ID 5f4fc14da2b47835a58c63a2 in Atlas and the ID /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/test-endpoint in Azure for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints azure interfaces create 5f4fc14da2b47835a58c63a2 --privateEndpointId /subscriptions/4e133d35-e734-4385-a565-c0945567ae346/resourceGroups/rg_95847a959b876e255dbb9b33_dfragd7w/providers/Microsoft.Network/privateEndpoints/test-endpoint --projectId 5e2211c17a3e5a48f5497de3 --privateEndpointIpAddress 192.0.2.5
  --output json
```


### Flags

```
  -h, --help                              help for create
  -o, --output string                     Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --privateEndpointId string          Unique string that identifies the Azure private endpoint in Azure. The Properties page for your private endpoint on your Azure dashboard displays this property in the Resource ID field.
      --privateEndpointIpAddress string   Private IP address of the private endpoint network interface you created in your Azure VNet.
      --projectId string                  Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints azure interfaces](atlas_privateEndpoints_azure_interfaces.md)	- Manage Atlas Azure private endpoint interfaces.



