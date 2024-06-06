## atlas privateEndpoints azure delete

Remove the specified Azure private endpoint from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints azure delete <privateEndpointId> [flags]
atlas privateEndpoints azure rm <privateEndpointId> [flags]
atlas privateendpoints azure delete <privateEndpointId> [flags]
atlas privateendpoints azure rm <privateEndpointId> [flags]
atlas private-endpoints azure delete <privateEndpointId> [flags]
atlas private-endpoints azure rm <privateEndpointId> [flags]
atlas privateEndpoint azure delete <privateEndpointId> [flags]
atlas privateEndpoint azure rm <privateEndpointId> [flags]
atlas privateendpoint azure delete <privateEndpointId> [flags]
atlas privateendpoint azure rm <privateEndpointId> [flags]
atlas private-endpoint azure delete <privateEndpointId> [flags]
atlas private-endpoint azure rm <privateEndpointId> [flags]
```

### Examples

```
  # Remove the Azure private endpoint with the ID 5f4fc14da2b47835a58c63a2 from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints azure delete 5f4fc14da2b47835a58c63a2 --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints azure](atlas_privateEndpoints_azure.md)	- Manage Azure Private Endpoints.



