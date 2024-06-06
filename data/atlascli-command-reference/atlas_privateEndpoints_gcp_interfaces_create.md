## atlas privateEndpoints gcp interfaces create

Create a GCP private endpoint interface.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints gcp interfaces create <endpointGroupId> [flags]
```

### Aliases
```

atlas privateEndpoints gcp interfaces create
atlas privateEndpoints gcp interfaces add
atlas privateEndpoints gcp interface create
atlas privateEndpoints gcp interface add
atlas privateendpoints gcp interfaces create
atlas privateendpoints gcp interfaces add
atlas privateendpoints gcp interface create
atlas privateendpoints gcp interface add
atlas private-endpoints gcp interfaces create
atlas private-endpoints gcp interfaces add
atlas private-endpoints gcp interface create
atlas private-endpoints gcp interface add
atlas privateEndpoint gcp interfaces create
atlas privateEndpoint gcp interfaces add
atlas privateEndpoint gcp interface create
atlas privateEndpoint gcp interface add
atlas privateendpoint gcp interfaces create
atlas privateendpoint gcp interfaces add
atlas privateendpoint gcp interface create
atlas privateendpoint gcp interface add
atlas private-endpoint gcp interfaces create
atlas private-endpoint gcp interfaces add
atlas private-endpoint gcp interface create
atlas private-endpoint gcp interface add
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

### See Also


* [atlas privateEndpoints gcp interfaces](atlas_privateEndpoints_gcp_interfaces.md)	- Manage Atlas GCP private endpoint interfaces.



