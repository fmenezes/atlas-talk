## atlas dataFederation queryLimits describe

Return the details for the specified data federation query limit for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataFederation queryLimits describe <name> [flags]
```

### Aliases
```

atlas dataFederation queryLimits describe
atlas dataFederation querylimits describe
atlas dataFederation query-limits describe
atlas dataFederation queryLimit describe
atlas dataFederation querylimit describe
atlas dataFederation query-limit describe
atlas datafederation queryLimits describe
atlas datafederation querylimits describe
atlas datafederation query-limits describe
atlas datafederation queryLimit describe
atlas datafederation querylimit describe
atlas datafederation query-limit describe
atlas data-federation queryLimits describe
atlas data-federation querylimits describe
atlas data-federation query-limits describe
atlas data-federation queryLimit describe
atlas data-federation querylimit describe
atlas data-federation query-limit describe
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

### See Also


* [atlas dataFederation queryLimits](atlas_dataFederation_queryLimits.md)	- Data federation query limits.



