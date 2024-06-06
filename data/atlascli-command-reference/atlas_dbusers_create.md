## atlas dbusers create

Create a database user for your project.


### Synopsis

If you set --ldapType, --x509Type, --oidcType and --awsIAMType to NONE, Atlas authenticates this user through SCRAM-SHA. To learn more, see https://www.mongodb.com/docs/manual/core/security-scram/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dbusers create <builtInRole>... [flags]
```

### Aliases
```

atlas dbusers create
atlas dbuser create
```

### Examples

```
  # Create an Atlas database admin user named myAdmin for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers create atlasAdmin --username myAdmin  --projectId 5e2211c17a3e5a48f5497de3

  # Create a database user named myUser with read/write access to any database for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers create readWriteAnyDatabase --username myUser --projectId 5e2211c17a3e5a48f5497de3

  # Create a database user named myUser with multiple roles for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers create --username myUser --role clusterMonitor,backup --projectId 5e2211c17a3e5a48f5497de3

  # Create a database user named myUser with multiple scopes for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers create --username myUser --role clusterMonitor --scope <REPLICA-SET ID>,<storeName> --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --awsIAMType string    AWS IAM method by which the provided username is authenticated. Valid values are NONE, USER, or ROLE. If you set this to USER or ROLE, the user authenticates with IAM credentials and doesn't need a password. (default "NONE")
      --deleteAfter string   Timestamp in ISO 8601 in UTC after which Atlas deletes the user.
  -h, --help                 help for create
      --ldapType string      LDAP method by which the provided username is authenticated. Valid values are NONE, USER, or GROUP. If you set this to USER or GROUP, the user authenticates with LDAP. (default "NONE")
      --oidcType string      OIDC method by which the provided database user is authenticated. Valid values are NONE, USER, or IDP_GROUP. If you set this to USER or GROUP_ID, the user authenticates with OIDC. (default "NONE")
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
  -p, --password string      Password for the database user.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings         Comma-separated list that specifies the user's roles and the databases or collections on which the roles apply.
                             The roles format is roleName[@dbName[.collection]].
                             roleName can either be a built-in role or a custom role.
                             dbName and collection are required only for built-in roles.
      --scope strings        Array of clusters and Atlas Data Lakes that this user has access to.
  -u, --username string      Username for authenticating to MongoDB.
      --x509Type string      X.509 method for authenticating the specified username. Valid values include NONE, MANAGED, and CUSTOMER. If you set this to MANAGED the user authenticates with an Atlas-managed X.509 certificate. If you set this to CUSTOMER, the user authenticates with a self-managed X.509 certificate. (default "NONE")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dbusers](atlas_dbusers.md)	- Manage database users for your project.



