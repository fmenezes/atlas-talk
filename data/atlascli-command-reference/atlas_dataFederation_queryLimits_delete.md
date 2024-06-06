## atlas dataFederation queryLimits delete

Remove the specified data federation query limit from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation queryLimits delete <name> [flags]
atlas dataFederation querylimits delete <name> [flags]
atlas dataFederation query-limits delete <name> [flags]
atlas dataFederation queryLimit delete <name> [flags]
atlas dataFederation querylimit delete <name> [flags]
atlas dataFederation query-limit delete <name> [flags]
atlas datafederation queryLimits delete <name> [flags]
atlas datafederation querylimits delete <name> [flags]
atlas datafederation query-limits delete <name> [flags]
atlas datafederation queryLimit delete <name> [flags]
atlas datafederation querylimit delete <name> [flags]
atlas datafederation query-limit delete <name> [flags]
atlas data-federation queryLimits delete <name> [flags]
atlas data-federation querylimits delete <name> [flags]
atlas data-federation query-limits delete <name> [flags]
atlas data-federation queryLimit delete <name> [flags]
atlas data-federation querylimit delete <name> [flags]
atlas data-federation query-limit delete <name> [flags]
```

### Examples

```
# deletes data federation query limits "bytesProcessed.query" for 'DataFederation1':
  atlas dataFederation queryLimits delete bytesProcessed.query --tenantName DataFederation1

```


### Flags

```
      --dataFederation string   Identifier of the Federated Database Instance.
      --force                   Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                    help for delete
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation queryLimits](atlas_dataFederation_queryLimits.md)	- Data federation query limits.



