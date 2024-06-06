## atlas privateEndpoints regionalModes describe

Return the regionalized private endpoint setting for your project.


### Synopsis

Use this command to check whether you can create multiple private resources per region.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints regionalModes describe [flags]
atlas privateEndpoints regionalModes get [flags]
atlas privateEndpoints regionalmodes describe [flags]
atlas privateEndpoints regionalmodes get [flags]
atlas privateEndpoints regional-modes describe [flags]
atlas privateEndpoints regional-modes get [flags]
atlas privateEndpoints regionalMode describe [flags]
atlas privateEndpoints regionalMode get [flags]
atlas privateEndpoints regionalmode describe [flags]
atlas privateEndpoints regionalmode get [flags]
atlas privateEndpoints regional-mode describe [flags]
atlas privateEndpoints regional-mode get [flags]
atlas privateendpoints regionalModes describe [flags]
atlas privateendpoints regionalModes get [flags]
atlas privateendpoints regionalmodes describe [flags]
atlas privateendpoints regionalmodes get [flags]
atlas privateendpoints regional-modes describe [flags]
atlas privateendpoints regional-modes get [flags]
atlas privateendpoints regionalMode describe [flags]
atlas privateendpoints regionalMode get [flags]
atlas privateendpoints regionalmode describe [flags]
atlas privateendpoints regionalmode get [flags]
atlas privateendpoints regional-mode describe [flags]
atlas privateendpoints regional-mode get [flags]
atlas private-endpoints regionalModes describe [flags]
atlas private-endpoints regionalModes get [flags]
atlas private-endpoints regionalmodes describe [flags]
atlas private-endpoints regionalmodes get [flags]
atlas private-endpoints regional-modes describe [flags]
atlas private-endpoints regional-modes get [flags]
atlas private-endpoints regionalMode describe [flags]
atlas private-endpoints regionalMode get [flags]
atlas private-endpoints regionalmode describe [flags]
atlas private-endpoints regionalmode get [flags]
atlas private-endpoints regional-mode describe [flags]
atlas private-endpoints regional-mode get [flags]
atlas privateEndpoint regionalModes describe [flags]
atlas privateEndpoint regionalModes get [flags]
atlas privateEndpoint regionalmodes describe [flags]
atlas privateEndpoint regionalmodes get [flags]
atlas privateEndpoint regional-modes describe [flags]
atlas privateEndpoint regional-modes get [flags]
atlas privateEndpoint regionalMode describe [flags]
atlas privateEndpoint regionalMode get [flags]
atlas privateEndpoint regionalmode describe [flags]
atlas privateEndpoint regionalmode get [flags]
atlas privateEndpoint regional-mode describe [flags]
atlas privateEndpoint regional-mode get [flags]
atlas privateendpoint regionalModes describe [flags]
atlas privateendpoint regionalModes get [flags]
atlas privateendpoint regionalmodes describe [flags]
atlas privateendpoint regionalmodes get [flags]
atlas privateendpoint regional-modes describe [flags]
atlas privateendpoint regional-modes get [flags]
atlas privateendpoint regionalMode describe [flags]
atlas privateendpoint regionalMode get [flags]
atlas privateendpoint regionalmode describe [flags]
atlas privateendpoint regionalmode get [flags]
atlas privateendpoint regional-mode describe [flags]
atlas privateendpoint regional-mode get [flags]
atlas private-endpoint regionalModes describe [flags]
atlas private-endpoint regionalModes get [flags]
atlas private-endpoint regionalmodes describe [flags]
atlas private-endpoint regionalmodes get [flags]
atlas private-endpoint regional-modes describe [flags]
atlas private-endpoint regional-modes get [flags]
atlas private-endpoint regionalMode describe [flags]
atlas private-endpoint regionalMode get [flags]
atlas private-endpoint regionalmode describe [flags]
atlas private-endpoint regionalmode get [flags]
atlas private-endpoint regional-mode describe [flags]
atlas private-endpoint regional-mode get [flags]
```

### Examples

```
  # Return the regionalized private endpoint setting for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints regionalModes describe --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



