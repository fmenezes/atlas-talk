## atlas dataFederation queryLimits delete

Remove the specified data federation query limit from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataFederation queryLimits delete <name> [flags]
```

### Aliases
```

atlas dataFederation queryLimits delete
atlas dataFederation querylimits delete
atlas dataFederation query-limits delete
atlas dataFederation queryLimit delete
atlas dataFederation querylimit delete
atlas dataFederation query-limit delete
atlas datafederation queryLimits delete
atlas datafederation querylimits delete
atlas datafederation query-limits delete
atlas datafederation queryLimit delete
atlas datafederation querylimit delete
atlas datafederation query-limit delete
atlas data-federation queryLimits delete
atlas data-federation querylimits delete
atlas data-federation query-limits delete
atlas data-federation queryLimit delete
atlas data-federation querylimit delete
atlas data-federation query-limit delete
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

### See Also


* [atlas dataFederation queryLimits](atlas_dataFederation_queryLimits.md)	- Data federation query limits.



