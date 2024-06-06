## atlas dataFederation privateEndpoints delete

Remove the specified data federation private endpoint from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation privateEndpoints delete <endpointId> [flags]
atlas dataFederation privateendpoints delete <endpointId> [flags]
atlas dataFederation private-endpoints delete <endpointId> [flags]
atlas dataFederation privateEndpoint delete <endpointId> [flags]
atlas dataFederation privateendpoint delete <endpointId> [flags]
atlas dataFederation private-endpoint delete <endpointId> [flags]
atlas datafederation privateEndpoints delete <endpointId> [flags]
atlas datafederation privateendpoints delete <endpointId> [flags]
atlas datafederation private-endpoints delete <endpointId> [flags]
atlas datafederation privateEndpoint delete <endpointId> [flags]
atlas datafederation privateendpoint delete <endpointId> [flags]
atlas datafederation private-endpoint delete <endpointId> [flags]
atlas data-federation privateEndpoints delete <endpointId> [flags]
atlas data-federation privateendpoints delete <endpointId> [flags]
atlas data-federation private-endpoints delete <endpointId> [flags]
atlas data-federation privateEndpoint delete <endpointId> [flags]
atlas data-federation privateendpoint delete <endpointId> [flags]
atlas data-federation private-endpoint delete <endpointId> [flags]
```

### Examples

```
# deletes data federation private endpoint '507f1f77bcf86cd799439011':
  atlas dataFederation privateEndpoints delete 507f1f77bcf86cd799439011

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


* [atlas dataFederation privateEndpoints](atlas_dataFederation_privateEndpoints.md)	- Data federation private endpoints.



