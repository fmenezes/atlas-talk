## atlas privateEndpoints gcp interfaces delete

Delete a specific GCP private endpoint interface for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints gcp interfaces delete <id> [flags]
atlas privateEndpoints gcp interfaces rm <id> [flags]
atlas privateEndpoints gcp interface delete <id> [flags]
atlas privateEndpoints gcp interface rm <id> [flags]
atlas privateendpoints gcp interfaces delete <id> [flags]
atlas privateendpoints gcp interfaces rm <id> [flags]
atlas privateendpoints gcp interface delete <id> [flags]
atlas privateendpoints gcp interface rm <id> [flags]
atlas private-endpoints gcp interfaces delete <id> [flags]
atlas private-endpoints gcp interfaces rm <id> [flags]
atlas private-endpoints gcp interface delete <id> [flags]
atlas private-endpoints gcp interface rm <id> [flags]
atlas privateEndpoint gcp interfaces delete <id> [flags]
atlas privateEndpoint gcp interfaces rm <id> [flags]
atlas privateEndpoint gcp interface delete <id> [flags]
atlas privateEndpoint gcp interface rm <id> [flags]
atlas privateendpoint gcp interfaces delete <id> [flags]
atlas privateendpoint gcp interfaces rm <id> [flags]
atlas privateendpoint gcp interface delete <id> [flags]
atlas privateendpoint gcp interface rm <id> [flags]
atlas private-endpoint gcp interfaces delete <id> [flags]
atlas private-endpoint gcp interfaces rm <id> [flags]
atlas private-endpoint gcp interface delete <id> [flags]
atlas private-endpoint gcp interface rm <id> [flags]
```

### Examples

```
  atlas privateEndpoints gcp interfaces delete endpoint-1 \
  --endpointServiceId 61eaca605af86411903de1dd
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


* [atlas privateEndpoints gcp interfaces](atlas_privateEndpoints_gcp_interfaces.md)	- Manage Atlas GCP private endpoint interfaces.



