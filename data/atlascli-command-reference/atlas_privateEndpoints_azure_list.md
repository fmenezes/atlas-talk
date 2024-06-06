## atlas privateEndpoints azure list

Return all Azure private endpoints for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints azure list [flags]
atlas privateEndpoints azure ls [flags]
atlas privateendpoints azure list [flags]
atlas privateendpoints azure ls [flags]
atlas private-endpoints azure list [flags]
atlas private-endpoints azure ls [flags]
atlas privateEndpoint azure list [flags]
atlas privateEndpoint azure ls [flags]
atlas privateendpoint azure list [flags]
atlas privateendpoint azure ls [flags]
atlas private-endpoint azure list [flags]
atlas private-endpoint azure ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of all Azure private endpoints for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints azure list --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints azure](atlas_privateEndpoints_azure.md)	- Manage Azure Private Endpoints.



