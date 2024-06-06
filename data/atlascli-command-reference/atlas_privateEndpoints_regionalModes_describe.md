## atlas privateEndpoints regionalModes describe

Return the regionalized private endpoint setting for your project.


### Synopsis

Use this command to check whether you can create multiple private resources per region.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints regionalModes describe [flags]
```

### Aliases
```

atlas privateEndpoints regionalModes describe
atlas privateEndpoints regionalModes get
atlas privateEndpoints regionalmodes describe
atlas privateEndpoints regionalmodes get
atlas privateEndpoints regional-modes describe
atlas privateEndpoints regional-modes get
atlas privateEndpoints regionalMode describe
atlas privateEndpoints regionalMode get
atlas privateEndpoints regionalmode describe
atlas privateEndpoints regionalmode get
atlas privateEndpoints regional-mode describe
atlas privateEndpoints regional-mode get
atlas privateendpoints regionalModes describe
atlas privateendpoints regionalModes get
atlas privateendpoints regionalmodes describe
atlas privateendpoints regionalmodes get
atlas privateendpoints regional-modes describe
atlas privateendpoints regional-modes get
atlas privateendpoints regionalMode describe
atlas privateendpoints regionalMode get
atlas privateendpoints regionalmode describe
atlas privateendpoints regionalmode get
atlas privateendpoints regional-mode describe
atlas privateendpoints regional-mode get
atlas private-endpoints regionalModes describe
atlas private-endpoints regionalModes get
atlas private-endpoints regionalmodes describe
atlas private-endpoints regionalmodes get
atlas private-endpoints regional-modes describe
atlas private-endpoints regional-modes get
atlas private-endpoints regionalMode describe
atlas private-endpoints regionalMode get
atlas private-endpoints regionalmode describe
atlas private-endpoints regionalmode get
atlas private-endpoints regional-mode describe
atlas private-endpoints regional-mode get
atlas privateEndpoint regionalModes describe
atlas privateEndpoint regionalModes get
atlas privateEndpoint regionalmodes describe
atlas privateEndpoint regionalmodes get
atlas privateEndpoint regional-modes describe
atlas privateEndpoint regional-modes get
atlas privateEndpoint regionalMode describe
atlas privateEndpoint regionalMode get
atlas privateEndpoint regionalmode describe
atlas privateEndpoint regionalmode get
atlas privateEndpoint regional-mode describe
atlas privateEndpoint regional-mode get
atlas privateendpoint regionalModes describe
atlas privateendpoint regionalModes get
atlas privateendpoint regionalmodes describe
atlas privateendpoint regionalmodes get
atlas privateendpoint regional-modes describe
atlas privateendpoint regional-modes get
atlas privateendpoint regionalMode describe
atlas privateendpoint regionalMode get
atlas privateendpoint regionalmode describe
atlas privateendpoint regionalmode get
atlas privateendpoint regional-mode describe
atlas privateendpoint regional-mode get
atlas private-endpoint regionalModes describe
atlas private-endpoint regionalModes get
atlas private-endpoint regionalmodes describe
atlas private-endpoint regionalmodes get
atlas private-endpoint regional-modes describe
atlas private-endpoint regional-modes get
atlas private-endpoint regionalMode describe
atlas private-endpoint regionalMode get
atlas private-endpoint regionalmode describe
atlas private-endpoint regionalmode get
atlas private-endpoint regional-mode describe
atlas private-endpoint regional-mode get
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

### See Also


* [atlas privateEndpoints regionalModes](atlas_privateEndpoints_regionalModes.md)	- Manage regionalized private endpoint setting for your Atlas project.



