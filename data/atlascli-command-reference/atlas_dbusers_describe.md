## atlas dbusers describe

Return the details for the specified database user for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas dbusers describe <username> [flags]
```

### Aliases
```

atlas dbusers describe
atlas dbusers get
atlas dbuser describe
atlas dbuser get
```

### Examples

```
  # Return the details for the SCRAM SHA-authenticating database user named myDbUser:
  atlas dbuser describe myDbUser --authDB admin --output json

  # Return the details for the AWS IAM-authenticating database user with the ARN arn:aws:iam::772401394250:user/my-test-user. Prepend $external with \ to escape the special-use character:
  atlas dbuser describe arn:aws:iam::772401394250:user/my-test-user --authDB \$external --output json

  # Return the details for the X.509-authenticating database user with the RFC 2253 Distinguished Name CN=ellen@example.com,OU=users,DC=example,DC=com. Prepend $external with \ to escape the special-use character:
  atlas dbuser describe CN=ellen@example.com,OU=users,DC=example,DC=com --authDB \$external --output json
```


### Flags

```
      --authDB string      Authentication database name. If the user authenticates with AWS IAM, x.509, or LDAP, this value should be $external. If the user authenticates with SCRAM-SHA, this value should be admin. (default "admin")
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dbusers](atlas_dbusers.md)	- Manage database users for your project.



