## atlas privateEndpoints regionalModes enable

Enable the regionalized private endpoint setting for your project.


### Synopsis

This enables the ability to create multiple private resources per region in all cloud service providers for this project.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints regionalModes enable [flags]
atlas privateEndpoints regionalmodes enable [flags]
atlas privateEndpoints regional-modes enable [flags]
atlas privateEndpoints regionalMode enable [flags]
atlas privateEndpoints regionalmode enable [flags]
atlas privateEndpoints regional-mode enable [flags]
atlas privateendpoints regionalModes enable [flags]
atlas privateendpoints regionalmodes enable [flags]
atlas privateendpoints regional-modes enable [flags]
atlas privateendpoints regionalMode enable [flags]
atlas privateendpoints regionalmode enable [flags]
atlas privateendpoints regional-mode enable [flags]
atlas private-endpoints regionalModes enable [flags]
atlas private-endpoints regionalmodes enable [flags]
atlas private-endpoints regional-modes enable [flags]
atlas private-endpoints regionalMode enable [flags]
atlas private-endpoints regionalmode enable [flags]
atlas private-endpoints regional-mode enable [flags]
atlas privateEndpoint regionalModes enable [flags]
atlas privateEndpoint regionalmodes enable [flags]
atlas privateEndpoint regional-modes enable [flags]
atlas privateEndpoint regionalMode enable [flags]
atlas privateEndpoint regionalmode enable [flags]
atlas privateEndpoint regional-mode enable [flags]
atlas privateendpoint regionalModes enable [flags]
atlas privateendpoint regionalmodes enable [flags]
atlas privateendpoint regional-modes enable [flags]
atlas privateendpoint regionalMode enable [flags]
atlas privateendpoint regionalmode enable [flags]
atlas privateendpoint regional-mode enable [flags]
atlas private-endpoint regionalModes enable [flags]
atlas private-endpoint regionalmodes enable [flags]
atlas private-endpoint regional-modes enable [flags]
atlas private-endpoint regionalMode enable [flags]
atlas private-endpoint regionalmode enable [flags]
atlas private-endpoint regional-mode enable [flags]
```

### Examples

```
  # Enable the regionalied private endpoint setting in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints regionalModes enable --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for enable
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



