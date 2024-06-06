## atlas dataFederation privateEndpoints create

Creates a new Data Federation private endpoint.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation privateEndpoints create <endpointId> [flags]
atlas dataFederation privateendpoints create <endpointId> [flags]
atlas dataFederation private-endpoints create <endpointId> [flags]
atlas dataFederation privateEndpoint create <endpointId> [flags]
atlas dataFederation privateendpoint create <endpointId> [flags]
atlas dataFederation private-endpoint create <endpointId> [flags]
atlas datafederation privateEndpoints create <endpointId> [flags]
atlas datafederation privateendpoints create <endpointId> [flags]
atlas datafederation private-endpoints create <endpointId> [flags]
atlas datafederation privateEndpoint create <endpointId> [flags]
atlas datafederation privateendpoint create <endpointId> [flags]
atlas datafederation private-endpoint create <endpointId> [flags]
atlas data-federation privateEndpoints create <endpointId> [flags]
atlas data-federation privateendpoints create <endpointId> [flags]
atlas data-federation private-endpoints create <endpointId> [flags]
atlas data-federation privateEndpoint create <endpointId> [flags]
atlas data-federation privateendpoint create <endpointId> [flags]
atlas data-federation private-endpoint create <endpointId> [flags]
```

### Examples

```
# create data federation private endpoint:
  atlas dataFederation privateEndpoints create 507f1f77bcf86cd799439011 --comment "comment"

```


### Flags

```
      --comment string     Optional description or comment for the entry.
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation privateEndpoints](atlas_dataFederation_privateEndpoints.md)	- Data federation private endpoints.



