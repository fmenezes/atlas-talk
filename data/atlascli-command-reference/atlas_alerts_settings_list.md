## atlas alerts settings list

Returns all alert configurations for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas alerts settings list [flags]
```

### Aliases
```

atlas alerts settings list
atlas alerts settings ls
atlas alerts config list
atlas alerts config ls
atlas alert settings list
atlas alert settings ls
atlas alert config list
atlas alert config ls
```

### Examples

```
  # Return a JSON-formatted list of all alert configurations for the project with the ID 5df90590f10fab5e33de2305:
  atlas alerts settings list --projectId 5df90590f10fab5e33de2305 --output json
```


### Flags

```
  -c, --compact            Flag that enables the compact array response structure for a json output. The --compact option returns array objects as top-level responses and allows backward compatibility for scripts based on previous CLI versions. Omitting the --compact option for a json output returns array objects within a 'results' sub-array. You must specify --output json to use this option.
  -h, --help               help for list
      --limit int          Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int           Page number that specifies a page of results. (default 1)
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas alerts settings](atlas_alerts_settings.md)	- Manages alerts configuration for your project.



