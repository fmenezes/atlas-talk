## atlas users describe

Return the details for the specified Atlas user.


### Synopsis

You can specify either the unique 24-digit ID that identifies the Atlas user or the username for the Atlas user.
		
User accounts and API keys with any role can run this command.


### Usage
```
atlas users describe [flags]
```

### Aliases
```

atlas users describe
atlas users get
atlas user describe
atlas user get
```

### Examples

```
  # Return the JSON-formatted details for the Atlas user with the ID 5dd56c847a3e5a1f363d424d:
  atlas users describe --id 5dd56c847a3e5a1f363d424d --output json
  
  # Return the JSON-formatted details for the Atlas user with the username myUser:
  atlas users describe --username myUser --output json
```


### Flags

```
  -h, --help              help for describe
      --id string         Unique 24-digit identifier of the user.
  -o, --output string     Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --username string   Name that identifies the user. You must specify a valid email address.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas users](atlas_users.md)	- Manage your Atlas users.



