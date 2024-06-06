## atlas security ldap verify status

Get the status of an LDAP configuration request.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security ldap verify status <requestId> [flags]
```

### Aliases
```

atlas security ldap verify status
```



### Flags

```
  -h, --help               help for status
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas security ldap verify](atlas_security_ldap_verify.md)	- Request verification of an LDAP configuration for your project.

* [atlas security ldap verify status watch](atlas_security_ldap_verify_status_watch.md)	- Watch for an LDAP configuration request to complete.



