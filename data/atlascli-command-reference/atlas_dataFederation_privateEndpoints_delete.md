## atlas dataFederation privateEndpoints delete

Remove the specified data federation private endpoint from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataFederation privateEndpoints delete <endpointId> [flags]
```

### Aliases
```

atlas dataFederation privateEndpoints delete
atlas dataFederation privateendpoints delete
atlas dataFederation private-endpoints delete
atlas dataFederation privateEndpoint delete
atlas dataFederation privateendpoint delete
atlas dataFederation private-endpoint delete
atlas datafederation privateEndpoints delete
atlas datafederation privateendpoints delete
atlas datafederation private-endpoints delete
atlas datafederation privateEndpoint delete
atlas datafederation privateendpoint delete
atlas datafederation private-endpoint delete
atlas data-federation privateEndpoints delete
atlas data-federation privateendpoints delete
atlas data-federation private-endpoints delete
atlas data-federation privateEndpoint delete
atlas data-federation privateendpoint delete
atlas data-federation private-endpoint delete
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

### See Also


* [atlas dataFederation privateEndpoints](atlas_dataFederation_privateEndpoints.md)	- Data federation private endpoints.



