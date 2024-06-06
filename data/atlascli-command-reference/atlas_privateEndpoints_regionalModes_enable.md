## atlas privateEndpoints regionalModes enable

Enable the regionalized private endpoint setting for your project.


### Synopsis

This enables the ability to create multiple private resources per region in all cloud service providers for this project.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas privateEndpoints regionalModes enable [flags]
```

### Aliases
```

atlas privateEndpoints regionalModes enable
atlas privateEndpoints regionalmodes enable
atlas privateEndpoints regional-modes enable
atlas privateEndpoints regionalMode enable
atlas privateEndpoints regionalmode enable
atlas privateEndpoints regional-mode enable
atlas privateendpoints regionalModes enable
atlas privateendpoints regionalmodes enable
atlas privateendpoints regional-modes enable
atlas privateendpoints regionalMode enable
atlas privateendpoints regionalmode enable
atlas privateendpoints regional-mode enable
atlas private-endpoints regionalModes enable
atlas private-endpoints regionalmodes enable
atlas private-endpoints regional-modes enable
atlas private-endpoints regionalMode enable
atlas private-endpoints regionalmode enable
atlas private-endpoints regional-mode enable
atlas privateEndpoint regionalModes enable
atlas privateEndpoint regionalmodes enable
atlas privateEndpoint regional-modes enable
atlas privateEndpoint regionalMode enable
atlas privateEndpoint regionalmode enable
atlas privateEndpoint regional-mode enable
atlas privateendpoint regionalModes enable
atlas privateendpoint regionalmodes enable
atlas privateendpoint regional-modes enable
atlas privateendpoint regionalMode enable
atlas privateendpoint regionalmode enable
atlas privateendpoint regional-mode enable
atlas private-endpoint regionalModes enable
atlas private-endpoint regionalmodes enable
atlas private-endpoint regional-modes enable
atlas private-endpoint regionalMode enable
atlas private-endpoint regionalmode enable
atlas private-endpoint regional-mode enable
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

### See Also


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



