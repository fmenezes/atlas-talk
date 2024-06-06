## atlas dbusers update

Modify the details of a database user in your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dbusers update <username> [flags]
```

### Aliases
```

atlas dbusers update
atlas dbuser update
```

### Examples

```
  # Update roles for a database user named myUser for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas dbuser update myUser --role readWriteAnyDatabase --projectId 5e2211c17a3e5a48f5497de3

  # Update scopes for a database user named myUser for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas dbuser update myUser --scope resourceName:resourceType --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --authDB string      Authentication database name. If the user authenticates with AWS IAM, x.509, or LDAP, this value should be $external. If the user authenticates with SCRAM-SHA, this value should be admin.
  -h, --help               help for update
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
  -p, --password string    Password for the database user.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       User's roles and the databases or collections on which the roles apply. Passing this flag replaces preexisting data.
      --scope strings      Array of clusters and Atlas Data Lakes that this user has access to. Passing this flag replaces preexisting data.
  -u, --username string    Username for authenticating to MongoDB.
      --x509Type string    X.509 method for authenticating the specified username. Valid values include NONE, MANAGED, and CUSTOMER. If you set this to MANAGED the user authenticates with an Atlas-managed X.509 certificate. If you set this to CUSTOMER, the user authenticates with a self-managed X.509 certificate. (default "NONE")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dbusers](atlas_dbusers.md)	- Manage database users for your project.



