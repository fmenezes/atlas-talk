## atlas streams instances list

List all the Atlas Stream Processing instances for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas streams instances list [flags]
```

### Aliases
```

atlas streams instances list
atlas streams instance list
atlas stream instances list
atlas stream instance list
```

### Examples

```
  # Return a JSON-formatted list of all Atlas Stream Processing instances for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas streams instance list --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
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


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



