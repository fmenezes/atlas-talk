## atlas dbusers certs list

Return all Atlas-managed, unexpired X.509 certificates for the specified database user.


### Synopsis

You can't use this command to return certificates if you are managing your own Certificate Authority (CA) in self-managed X.509 mode.
		
The user you specify must authenticate using X.509 certificates.


### Usage
```
atlas dbusers certs list <username> [flags]
```

### Aliases
```

atlas dbusers certs list
atlas dbusers certs ls
atlas dbusers cert list
atlas dbusers cert ls
atlas dbuser certs list
atlas dbuser certs ls
atlas dbuser cert list
atlas dbuser cert ls
```

### Examples

```
  # Return a JSON-formatted list of all Atlas-managed X.509 certificates for a MongoDB user named dbuser for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers certs list dbuser --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dbusers certs](atlas_dbusers_certs.md)	- Manage Atlas x509 certificates for your database users.



