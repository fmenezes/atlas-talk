## atlas privateEndpoints regionalModes disable

Disable the regionalized private endpoint setting for your project.


### Synopsis

This disables the ability to create multiple private resources per region in all cloud service providers for this project.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints regionalModes disable [flags]
```

### Aliases
```

atlas privateEndpoints regionalModes disable
atlas privateEndpoints regionalmodes disable
atlas privateEndpoints regional-modes disable
atlas privateEndpoints regionalMode disable
atlas privateEndpoints regionalmode disable
atlas privateEndpoints regional-mode disable
atlas privateendpoints regionalModes disable
atlas privateendpoints regionalmodes disable
atlas privateendpoints regional-modes disable
atlas privateendpoints regionalMode disable
atlas privateendpoints regionalmode disable
atlas privateendpoints regional-mode disable
atlas private-endpoints regionalModes disable
atlas private-endpoints regionalmodes disable
atlas private-endpoints regional-modes disable
atlas private-endpoints regionalMode disable
atlas private-endpoints regionalmode disable
atlas private-endpoints regional-mode disable
atlas privateEndpoint regionalModes disable
atlas privateEndpoint regionalmodes disable
atlas privateEndpoint regional-modes disable
atlas privateEndpoint regionalMode disable
atlas privateEndpoint regionalmode disable
atlas privateEndpoint regional-mode disable
atlas privateendpoint regionalModes disable
atlas privateendpoint regionalmodes disable
atlas privateendpoint regional-modes disable
atlas privateendpoint regionalMode disable
atlas privateendpoint regionalmode disable
atlas privateendpoint regional-mode disable
atlas private-endpoint regionalModes disable
atlas private-endpoint regionalmodes disable
atlas private-endpoint regional-modes disable
atlas private-endpoint regionalMode disable
atlas private-endpoint regionalmode disable
atlas private-endpoint regional-mode disable
```

### Examples

```
  # Disable the regionalied private endpoint setting in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints regionalModes disable --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for disable
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



