## atlas privateEndpoints gcp interfaces describe

Return a specific GCP private endpoint interface for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints gcp interfaces describe <id> [flags]
atlas privateEndpoints gcp interfaces get <id> [flags]
atlas privateEndpoints gcp interface describe <id> [flags]
atlas privateEndpoints gcp interface get <id> [flags]
atlas privateendpoints gcp interfaces describe <id> [flags]
atlas privateendpoints gcp interfaces get <id> [flags]
atlas privateendpoints gcp interface describe <id> [flags]
atlas privateendpoints gcp interface get <id> [flags]
atlas private-endpoints gcp interfaces describe <id> [flags]
atlas private-endpoints gcp interfaces get <id> [flags]
atlas private-endpoints gcp interface describe <id> [flags]
atlas private-endpoints gcp interface get <id> [flags]
atlas privateEndpoint gcp interfaces describe <id> [flags]
atlas privateEndpoint gcp interfaces get <id> [flags]
atlas privateEndpoint gcp interface describe <id> [flags]
atlas privateEndpoint gcp interface get <id> [flags]
atlas privateendpoint gcp interfaces describe <id> [flags]
atlas privateendpoint gcp interfaces get <id> [flags]
atlas privateendpoint gcp interface describe <id> [flags]
atlas privateendpoint gcp interface get <id> [flags]
atlas private-endpoint gcp interfaces describe <id> [flags]
atlas private-endpoint gcp interfaces get <id> [flags]
atlas private-endpoint gcp interface describe <id> [flags]
atlas private-endpoint gcp interface get <id> [flags]
```

### Examples

```
  atlas privateEndpoints gcp interfaces describe endpoint-1 \
  --endpointServiceId 61eaca605af86411903de1dd
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


* [atlas privateEndpoints gcp interfaces](atlas_privateEndpoints_gcp_interfaces.md)	- Manage Atlas GCP private endpoint interfaces.



