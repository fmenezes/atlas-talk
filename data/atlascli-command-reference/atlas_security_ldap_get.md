## atlas security ldap get

Return the current LDAP configuration details for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security ldap get [flags]
```

### Aliases
```

atlas security ldap get
```

### Examples

```
  # Return the JSON-formatted details of the current LDAP configuration in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security ldap get --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for get
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas security ldap](atlas_security_ldap.md)	- LDAP operations.



