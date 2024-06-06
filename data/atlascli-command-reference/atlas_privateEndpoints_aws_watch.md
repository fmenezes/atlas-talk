## atlas privateEndpoints aws watch

Watch the specified AWS private endpoint in your project until it becomes available.


### Synopsis

This command checks the endpoint's state periodically until the endpoint reaches an AVAILABLE or FAILED state. 
Once the endpoint reaches the expected state, the command prints "Private endpoint changes completed."
If you run the command in the terminal, it blocks the terminal session until the resource becomes available or fails.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas privateEndpoints aws watch <privateEndpointId> [flags]
atlas privateendpoints aws watch <privateEndpointId> [flags]
atlas private-endpoints aws watch <privateEndpointId> [flags]
atlas privateEndpoint aws watch <privateEndpointId> [flags]
atlas privateendpoint aws watch <privateEndpointId> [flags]
atlas private-endpoint aws watch <privateEndpointId> [flags]
```

### Examples

```
  # Watch for the AWS private endpoint with the ID 5f4fc14da2b47835a58c63a2 to become available in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws watch 5f4fc14da2b47835a58c63a2 --projectId 5e2211c17a3e5a48f5497de3
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

### SEE ALSO


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



