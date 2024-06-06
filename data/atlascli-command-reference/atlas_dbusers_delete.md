## atlas dbusers delete

Remove the specified database user from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dbusers delete <username> [flags]
```

### Aliases
```

atlas dbusers delete
atlas dbusers rm
atlas dbuser delete
atlas dbuser rm
```

### Examples

```
  # Delete the SCRAM SHA-authenticating database user named dylan for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers delete dylan --projectId 5e2211c17a3e5a48f5497de3

  # Delete the AWS IAM-authenticating database user with the ARN arn:aws:iam::123456789012:user/sales/enterprise/DylanBloggs for the project with ID 5e2211c17a3e5a48f5497de3. Prepend $external with \ to escape the special-use character:
  atlas dbusers delete arn:aws:iam::123456789012:user/sales/enterprise/DylanBloggs --authDB \$external --projectId 5e2211c17a3e5a48f5497de3
			
  # Delete the xLDAP-authenticating database user with the RFC 2253 Distinguished Name CN=Dylan Bloggs,OU=Enterprise,OU=Sales,DC=Example,DC=COM for the project with ID 5e2211c17a3e5a48f5497de3. Prepend $external with \ to escape the special-use character:
  atlas dbusers delete CN=Dylan Bloggs,OU=Enterprise,OU=Sales,DC=Example,DC=COM --authDB \$external --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --authDB string      Authentication database name. If the user authenticates with AWS IAM, x.509, or LDAP, this value should be $external. If the user authenticates with SCRAM-SHA, this value should be admin. (default "admin")
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dbusers](atlas_dbusers.md)	- Manage database users for your project.



