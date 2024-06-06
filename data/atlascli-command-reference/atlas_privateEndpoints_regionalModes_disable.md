## atlas privateEndpoints regionalModes disable

Disable the regionalized private endpoint setting for your project.


### Synopsis

This disables the ability to create multiple private resources per region in all cloud service providers for this project.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints regionalModes disable [flags]
atlas privateEndpoints regionalmodes disable [flags]
atlas privateEndpoints regional-modes disable [flags]
atlas privateEndpoints regionalMode disable [flags]
atlas privateEndpoints regionalmode disable [flags]
atlas privateEndpoints regional-mode disable [flags]
atlas privateendpoints regionalModes disable [flags]
atlas privateendpoints regionalmodes disable [flags]
atlas privateendpoints regional-modes disable [flags]
atlas privateendpoints regionalMode disable [flags]
atlas privateendpoints regionalmode disable [flags]
atlas privateendpoints regional-mode disable [flags]
atlas private-endpoints regionalModes disable [flags]
atlas private-endpoints regionalmodes disable [flags]
atlas private-endpoints regional-modes disable [flags]
atlas private-endpoints regionalMode disable [flags]
atlas private-endpoints regionalmode disable [flags]
atlas private-endpoints regional-mode disable [flags]
atlas privateEndpoint regionalModes disable [flags]
atlas privateEndpoint regionalmodes disable [flags]
atlas privateEndpoint regional-modes disable [flags]
atlas privateEndpoint regionalMode disable [flags]
atlas privateEndpoint regionalmode disable [flags]
atlas privateEndpoint regional-mode disable [flags]
atlas privateendpoint regionalModes disable [flags]
atlas privateendpoint regionalmodes disable [flags]
atlas privateendpoint regional-modes disable [flags]
atlas privateendpoint regionalMode disable [flags]
atlas privateendpoint regionalmode disable [flags]
atlas privateendpoint regional-mode disable [flags]
atlas private-endpoint regionalModes disable [flags]
atlas private-endpoint regionalmodes disable [flags]
atlas private-endpoint regional-modes disable [flags]
atlas private-endpoint regionalMode disable [flags]
atlas private-endpoint regionalmode disable [flags]
atlas private-endpoint regional-mode disable [flags]
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

### SEE ALSO


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



