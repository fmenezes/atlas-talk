## atlas security ldap delete

Remove the current LDAP configuration captured in the userToDNMapping document from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security ldap delete [flags]
```

### Aliases
```

atlas security ldap delete
atlas security ldap rm
```

### Examples

```
  # Remove the current LDAP configuration in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security ldap delete --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas security ldap](atlas_security_ldap.md)	- LDAP operations.



