## atlas networking peering list

Return the details for all network peering connections for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas networking peering list [flags]
```

### Aliases
```

atlas networking peering list
atlas networking peering ls
```

### Examples

```
  # Return the JSON-formatted details for all network peering connections in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas networking peering list --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for list
      --limit int          Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount          Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int           Page number that specifies a page of results. (default 1)
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string    Name of your cloud service provider. Valid values are AWS, AZURE, or GCP. (default "AWS")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas networking peering](atlas_networking_peering.md)	- Manage Network Peering connections.



