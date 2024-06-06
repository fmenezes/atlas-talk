## atlas dataFederation privateEndpoints describe

Return the details for the specified data federation private endpoint for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataFederation privateEndpoints describe <endpointId> [flags]
```

### Aliases
```

atlas dataFederation privateEndpoints describe
atlas dataFederation privateendpoints describe
atlas dataFederation private-endpoints describe
atlas dataFederation privateEndpoint describe
atlas dataFederation privateendpoint describe
atlas dataFederation private-endpoint describe
atlas datafederation privateEndpoints describe
atlas datafederation privateendpoints describe
atlas datafederation private-endpoints describe
atlas datafederation privateEndpoint describe
atlas datafederation privateendpoint describe
atlas datafederation private-endpoint describe
atlas data-federation privateEndpoints describe
atlas data-federation privateendpoints describe
atlas data-federation private-endpoints describe
atlas data-federation privateEndpoint describe
atlas data-federation privateendpoint describe
atlas data-federation private-endpoint describe
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

### See Also


* [atlas dataFederation privateEndpoints](atlas_dataFederation_privateEndpoints.md)	- Data federation private endpoints.



