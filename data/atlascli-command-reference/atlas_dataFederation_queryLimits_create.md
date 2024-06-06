## atlas dataFederation queryLimits create

Creates a new Data Federation query limit.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation queryLimits create <name> [flags]
atlas dataFederation querylimits create <name> [flags]
atlas dataFederation query-limits create <name> [flags]
atlas dataFederation queryLimit create <name> [flags]
atlas dataFederation querylimit create <name> [flags]
atlas dataFederation query-limit create <name> [flags]
atlas datafederation queryLimits create <name> [flags]
atlas datafederation querylimits create <name> [flags]
atlas datafederation query-limits create <name> [flags]
atlas datafederation queryLimit create <name> [flags]
atlas datafederation querylimit create <name> [flags]
atlas datafederation query-limit create <name> [flags]
atlas data-federation queryLimits create <name> [flags]
atlas data-federation querylimits create <name> [flags]
atlas data-federation query-limits create <name> [flags]
atlas data-federation queryLimit create <name> [flags]
atlas data-federation querylimit create <name> [flags]
atlas data-federation query-limit create <name> [flags]
```

### Examples

```
# create data federation query limit:
  atlas dataFederation queryLimit create bytesProcessed.query --value 1000 --dataFederation DataFederation1

```


### Flags

```
      --dataFederation string   Identifier of the Federated Database Instance.
  -h, --help                    help for create
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --overrunPolicy string    Action to take when the usage limit is exceeded.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --value int               Value given to the query limit.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation queryLimits](atlas_dataFederation_queryLimits.md)	- Data federation query limits.



