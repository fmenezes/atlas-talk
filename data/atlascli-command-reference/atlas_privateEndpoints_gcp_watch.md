## atlas privateEndpoints gcp watch

Watch the specified GCP private endpoint to detect changes in the endpoint's state.


### Synopsis

This command checks the endpoint's state periodically until the endpoint reaches an AVAILABLE or FAILED state. 
Once the endpoint reaches the expected state, the command prints "GCP Private endpoint changes completed."
If you run the command in the terminal, it blocks the terminal session until the resource becomes available or fails.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas privateEndpoints gcp watch <privateEndpointId> [flags]
```

### Aliases
```

atlas privateEndpoints gcp watch
atlas privateendpoints gcp watch
atlas private-endpoints gcp watch
atlas privateEndpoint gcp watch
atlas privateendpoint gcp watch
atlas private-endpoint gcp watch
```

### Examples

```
  atlas privateEndpoint gcp watch vpce-abcdefg0123456789
```


### Flags

```
  -h, --help               help for watch
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas privateEndpoints gcp](atlas_privateEndpoints_gcp.md)	- Manage GCP private endpoints.



