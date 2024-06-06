## atlas metrics disks list

Return all disks or disk partitions on the specified host for your project.


### Synopsis

To return the hostname and port needed for this command, run:
$ atlas processes list

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas metrics disks list <hostname:port> [flags]
```

### Aliases
```

atlas metrics disks list
atlas metrics disks ls
atlas metrics disk list
atlas metrics disk ls
atlas metric disks list
atlas metric disks ls
atlas metric disk list
atlas metric disk ls
atlas measurements disks list
atlas measurements disks ls
atlas measurements disk list
atlas measurements disk ls
atlas measurement disks list
atlas measurement disks ls
atlas measurement disk list
atlas measurement disk ls
```

### Examples

```
  # Return a JSON-formatted list of disks and partitions for the host atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017
  atlas metrics disks list atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 --output json
```


### Flags

```
  -h, --help               help for list
      --limit int          Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount          Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int           Page number that specifies a page of results. (default 1)
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas metrics disks](atlas_metrics_disks.md)	- List available disks or disk metrics for a given host.



