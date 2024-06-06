## atlas privateEndpoints gcp interfaces create

Create a GCP private endpoint interface.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints gcp interfaces create <endpointGroupId> [flags]
atlas privateEndpoints gcp interfaces add <endpointGroupId> [flags]
atlas privateEndpoints gcp interface create <endpointGroupId> [flags]
atlas privateEndpoints gcp interface add <endpointGroupId> [flags]
atlas privateendpoints gcp interfaces create <endpointGroupId> [flags]
atlas privateendpoints gcp interfaces add <endpointGroupId> [flags]
atlas privateendpoints gcp interface create <endpointGroupId> [flags]
atlas privateendpoints gcp interface add <endpointGroupId> [flags]
atlas private-endpoints gcp interfaces create <endpointGroupId> [flags]
atlas private-endpoints gcp interfaces add <endpointGroupId> [flags]
atlas private-endpoints gcp interface create <endpointGroupId> [flags]
atlas private-endpoints gcp interface add <endpointGroupId> [flags]
atlas privateEndpoint gcp interfaces create <endpointGroupId> [flags]
atlas privateEndpoint gcp interfaces add <endpointGroupId> [flags]
atlas privateEndpoint gcp interface create <endpointGroupId> [flags]
atlas privateEndpoint gcp interface add <endpointGroupId> [flags]
atlas privateendpoint gcp interfaces create <endpointGroupId> [flags]
atlas privateendpoint gcp interfaces add <endpointGroupId> [flags]
atlas privateendpoint gcp interface create <endpointGroupId> [flags]
atlas privateendpoint gcp interface add <endpointGroupId> [flags]
atlas private-endpoint gcp interfaces create <endpointGroupId> [flags]
atlas private-endpoint gcp interfaces add <endpointGroupId> [flags]
atlas private-endpoint gcp interface create <endpointGroupId> [flags]
atlas private-endpoint gcp interface add <endpointGroupId> [flags]
```

### Examples

```
  atlas privateEndpoints gcp interfaces create endpoint-1 \
  --endpointServiceId 61eaca605af86411903de1dd \
  --gcpProjectId mcli-private-endpoints \
  --endpoint endpoint-0@10.142.0.2,endpoint-1@10.142.0.3,endpoint-2@10.142.0.4,endpoint-3@10.142.0.5,endpoint-4@10.142.0.6,endpoint-5@10.142.0.7
```


### Flags

```
      --endpoint strings           List of GCP endpoints in the group separated by commas, such as: endpointName1@ipAddress1,...,endpointNameN@ipAddressN
      --endpointServiceId string   Unique 24-character alphanumeric string that identifies the private endpoint in Atlas.
      --gcpProjectId string        Unique identifier of the GCP project in which the network peer resides.
  -h, --help                       help for create
  -o, --output string              Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string           Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints gcp interfaces](atlas_privateEndpoints_gcp_interfaces.md)	- Manage Atlas GCP private endpoint interfaces.



