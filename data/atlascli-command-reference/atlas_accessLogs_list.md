## atlas accessLogs list

Retrieve the access logs of a cluster identified by the cluster's name or hostname.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Monitoring Admin role.


### Usage
```
atlas accessLogs list [flags]
```

### Aliases
```

atlas accessLogs list
atlas accessLogs ls
atlas accesslogs list
atlas accesslogs ls
atlas access-logs list
atlas access-logs ls
atlas accessLog list
atlas accessLog ls
atlas accesslog list
atlas accesslog ls
atlas access-log list
atlas access-log ls
```

### Examples

```
  # Return a JSON-formatted list of all authentication requests made against the cluster named Cluster0 for the project with ID 618d48e05277a606ed2496fe:		
  atlas accesslogs list --output json --projectId 618d48e05277a606ed2496fe --clusterName Cluster0
```


### Flags

```
      --authResult string    Authentication attempts that Atlas should return. When set to success, Atlas filters the log to return only successful authentication attempts. When set to fail, Atlas filters the log to return only failed authentication attempts.
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --end string           Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the last entry that Atlas returns from the database access logs.
  -h, --help                 help for list
      --hostname string      The fully qualified domain name (FQDN) of the target node that should receive the authentication attempt.
      --ip string            IP address that attempted to authenticate with the database. Atlas filters the returned logs to include documents with only this IP address.
      --nLog int             Maximum number of log lines to return.
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start string         Timestamp in the number of milliseconds that have elapsed, since the UNIX Epoch, for the first entry that Atlas returns from the database access logs.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas accessLogs](atlas_accessLogs.md)	- Return the access logs for a cluster.



