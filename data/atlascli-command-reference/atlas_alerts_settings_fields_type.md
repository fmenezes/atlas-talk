## atlas alerts settings fields type

Return all available field types that the matcherFieldName option accepts when you create or update an alert configuration.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas alerts settings fields type [flags]
atlas alerts settings fields types [flags]
atlas alerts settings field type [flags]
atlas alerts settings field types [flags]
atlas alerts config fields type [flags]
atlas alerts config fields types [flags]
atlas alerts config field type [flags]
atlas alerts config field types [flags]
atlas alert settings fields type [flags]
atlas alert settings fields types [flags]
atlas alert settings field type [flags]
atlas alert settings field types [flags]
atlas alert config fields type [flags]
atlas alert config fields types [flags]
atlas alert config field type [flags]
atlas alert config field types [flags]
```

### Examples

```
  # Return a JSON-formatted list of accepted field types for the matchersFieldName option:
  atlas alerts settings fields type --output json
```


### Flags

```
  -h, --help            help for type
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas alerts settings fields](atlas_alerts_settings_fields.md)	- Manages alert configuration fields for your project.



