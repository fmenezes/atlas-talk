## atlas privateEndpoints aws list

Return all AWS private endpoints for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints aws list [flags]
atlas privateEndpoints aws ls [flags]
atlas privateendpoints aws list [flags]
atlas privateendpoints aws ls [flags]
atlas private-endpoints aws list [flags]
atlas private-endpoints aws ls [flags]
atlas privateEndpoint aws list [flags]
atlas privateEndpoint aws ls [flags]
atlas privateendpoint aws list [flags]
atlas privateendpoint aws ls [flags]
atlas private-endpoint aws list [flags]
atlas private-endpoint aws ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of all AWS private endpoints for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws list --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



