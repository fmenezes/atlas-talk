## atlas privateEndpoints gcp delete

Delete a GCP private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints gcp delete <privateEndpointId> [flags]
atlas privateEndpoints gcp rm <privateEndpointId> [flags]
atlas privateendpoints gcp delete <privateEndpointId> [flags]
atlas privateendpoints gcp rm <privateEndpointId> [flags]
atlas private-endpoints gcp delete <privateEndpointId> [flags]
atlas private-endpoints gcp rm <privateEndpointId> [flags]
atlas privateEndpoint gcp delete <privateEndpointId> [flags]
atlas privateEndpoint gcp rm <privateEndpointId> [flags]
atlas privateendpoint gcp delete <privateEndpointId> [flags]
atlas privateendpoint gcp rm <privateEndpointId> [flags]
atlas private-endpoint gcp delete <privateEndpointId> [flags]
atlas private-endpoint gcp rm <privateEndpointId> [flags]
```

### Examples

```
  atlas privateEndpoint gcp delete vpce-abcdefg0123456789 --force
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



