## atlas dbusers certs create

Create a new Atlas-managed X.509 certificate for the specified database user.


### Synopsis

The user you specify must authenticate using X.509 certificates. You can't use this command to create certificates if you are managing your own Certificate Authority (CA) in self-managed X.509 mode.



```

atlas dbusers certs create [flags]
atlas dbusers cert create [flags]
atlas dbuser certs create [flags]
atlas dbuser cert create [flags]
```

### Examples

```
  # Create an Atlas-managed X.509 certificate that expires in 5 months for a MongoDB user named dbuser for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers certs create --username dbuser --monthsUntilExpiration 5 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help                        help for create
      --monthsUntilExpiration int   Number of months until the X.509 certificate expires. (default 3)
  -o, --output string               Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string            Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --username string             Username of a database user.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dbusers certs](atlas_dbusers_certs.md)	- Manage Atlas x509 certificates for your database users.



