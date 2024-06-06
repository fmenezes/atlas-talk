## atlas privateEndpoints gcp interfaces delete

Delete a specific GCP private endpoint interface for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints gcp interfaces delete <id> [flags]
```

### Aliases
```

atlas privateEndpoints gcp interfaces delete
atlas privateEndpoints gcp interfaces rm
atlas privateEndpoints gcp interface delete
atlas privateEndpoints gcp interface rm
atlas privateendpoints gcp interfaces delete
atlas privateendpoints gcp interfaces rm
atlas privateendpoints gcp interface delete
atlas privateendpoints gcp interface rm
atlas private-endpoints gcp interfaces delete
atlas private-endpoints gcp interfaces rm
atlas private-endpoints gcp interface delete
atlas private-endpoints gcp interface rm
atlas privateEndpoint gcp interfaces delete
atlas privateEndpoint gcp interfaces rm
atlas privateEndpoint gcp interface delete
atlas privateEndpoint gcp interface rm
atlas privateendpoint gcp interfaces delete
atlas privateendpoint gcp interfaces rm
atlas privateendpoint gcp interface delete
atlas privateendpoint gcp interface rm
atlas private-endpoint gcp interfaces delete
atlas private-endpoint gcp interfaces rm
atlas private-endpoint gcp interface delete
atlas private-endpoint gcp interface rm
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

### See Also


* [atlas privateEndpoints gcp interfaces](atlas_privateEndpoints_gcp_interfaces.md)	- Manage Atlas GCP private endpoint interfaces.



