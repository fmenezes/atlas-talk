## atlas dataFederation privateEndpoints describe

Return the details for the specified data federation private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation privateEndpoints describe <endpointId> [flags]
atlas dataFederation privateendpoints describe <endpointId> [flags]
atlas dataFederation private-endpoints describe <endpointId> [flags]
atlas dataFederation privateEndpoint describe <endpointId> [flags]
atlas dataFederation privateendpoint describe <endpointId> [flags]
atlas dataFederation private-endpoint describe <endpointId> [flags]
atlas datafederation privateEndpoints describe <endpointId> [flags]
atlas datafederation privateendpoints describe <endpointId> [flags]
atlas datafederation private-endpoints describe <endpointId> [flags]
atlas datafederation privateEndpoint describe <endpointId> [flags]
atlas datafederation privateendpoint describe <endpointId> [flags]
atlas datafederation private-endpoint describe <endpointId> [flags]
atlas data-federation privateEndpoints describe <endpointId> [flags]
atlas data-federation privateendpoints describe <endpointId> [flags]
atlas data-federation private-endpoints describe <endpointId> [flags]
atlas data-federation privateEndpoint describe <endpointId> [flags]
atlas data-federation privateendpoint describe <endpointId> [flags]
atlas data-federation private-endpoint describe <endpointId> [flags]
```

### Examples

```
# retrieves data federation private endpoint '507f1f77bcf86cd799439011':
  atlas dataFederation privateEndpoints describe 507f1f77bcf86cd799439011

```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation privateEndpoints](atlas_dataFederation_privateEndpoints.md)	- Data federation private endpoints.



