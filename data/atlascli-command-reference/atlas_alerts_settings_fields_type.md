## atlas alerts settings fields type

Return all available field types that the matcherFieldName option accepts when you create or update an alert configuration.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas alerts settings fields type [flags]
```

### Aliases
```

atlas alerts settings fields type
atlas alerts settings fields types
atlas alerts settings field type
atlas alerts settings field types
atlas alerts config fields type
atlas alerts config fields types
atlas alerts config field type
atlas alerts config field types
atlas alert settings fields type
atlas alert settings fields types
atlas alert settings field type
atlas alert settings field types
atlas alert config fields type
atlas alert config fields types
atlas alert config field type
atlas alert config field types
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

### See Also


* [atlas alerts settings fields](atlas_alerts_settings_fields.md)	- Manages alert configuration fields for your project.



