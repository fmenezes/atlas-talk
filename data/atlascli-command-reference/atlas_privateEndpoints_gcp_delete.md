## atlas privateEndpoints gcp delete

Delete a GCP private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints gcp delete <privateEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints gcp delete
atlas privateEndpoints gcp rm
atlas privateendpoints gcp delete
atlas privateendpoints gcp rm
atlas private-endpoints gcp delete
atlas private-endpoints gcp rm
atlas privateEndpoint gcp delete
atlas privateEndpoint gcp rm
atlas privateendpoint gcp delete
atlas privateendpoint gcp rm
atlas private-endpoint gcp delete
atlas private-endpoint gcp rm
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

### See Also


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



