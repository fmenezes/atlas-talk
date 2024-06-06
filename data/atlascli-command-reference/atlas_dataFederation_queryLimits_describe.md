## atlas dataFederation queryLimits describe

Return the details for the specified data federation query limit for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation queryLimits describe <name> [flags]
atlas dataFederation querylimits describe <name> [flags]
atlas dataFederation query-limits describe <name> [flags]
atlas dataFederation queryLimit describe <name> [flags]
atlas dataFederation querylimit describe <name> [flags]
atlas dataFederation query-limit describe <name> [flags]
atlas datafederation queryLimits describe <name> [flags]
atlas datafederation querylimits describe <name> [flags]
atlas datafederation query-limits describe <name> [flags]
atlas datafederation queryLimit describe <name> [flags]
atlas datafederation querylimit describe <name> [flags]
atlas datafederation query-limit describe <name> [flags]
atlas data-federation queryLimits describe <name> [flags]
atlas data-federation querylimits describe <name> [flags]
atlas data-federation query-limits describe <name> [flags]
atlas data-federation queryLimit describe <name> [flags]
atlas data-federation querylimit describe <name> [flags]
atlas data-federation query-limit describe <name> [flags]
```

### Examples

```
# retrieves data federation query limits "bytesProcessed.query" for 'DataFederation1':
  atlas dataFederation queryLimits describe bytesProcessed.query --tenantName DataFederation1

```


### Flags

```
      --dataFederation string   Identifier of the Federated Database Instance.
  -h, --help                    help for describe
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation queryLimits](atlas_dataFederation_queryLimits.md)	- Data federation query limits.



