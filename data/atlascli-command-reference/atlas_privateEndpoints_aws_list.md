## atlas privateEndpoints aws list

Return all AWS private endpoints for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints aws list [flags]
```

### Aliases
```

atlas privateEndpoints aws list
atlas privateEndpoints aws ls
atlas privateendpoints aws list
atlas privateendpoints aws ls
atlas private-endpoints aws list
atlas private-endpoints aws ls
atlas privateEndpoint aws list
atlas privateEndpoint aws ls
atlas privateendpoint aws list
atlas privateendpoint aws ls
atlas private-endpoint aws list
atlas private-endpoint aws ls
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

### See Also


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



