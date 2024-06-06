## atlas users invite

Create an Atlas user for your MongoDB Atlas application and invite the Atlas user to your organizations and projects.


### Synopsis

An Atlas user account grants access only to the the MongoDB Atlas application. To grant database access, create a database user with atlas dbusers create.


### Usage
```
atlas users invite [flags]
```

### Aliases
```

atlas users invite
atlas user invite
```

### Examples

```
  # Create the Atlas user with the username user@example.com and invite them to the organization with the ID 5dd56c847a3e5a1f363d424d with ORG_OWNER access:
  atlas users invite --email user@example.com --username user@example.com --orgRole 5dd56c847a3e5a1f363d424d:ORG_OWNER --firstName Example --lastName User --country US --output json
  
  # Create the Atlas user with the username user@example.com and invite them to the project with the ID 5f71e5255afec75a3d0f96dc with GROUP_READ_ONLY access:
  atlas users invite --email user@example.com --username user@example.com --projectRole 5f71e5255afec75a3d0f96dc:GROUP_READ_ONLY --firstName Example --lastName User --country US --output json
```


### Flags

```
      --country string        ISO 3166-1 alpha two-letter country code of the user's geographic location. The Atlas CLI requires this option.
      --email string          Email address for the user.
      --firstName string      First or given name for the user.
  -h, --help                  help for invite
      --lastName string       Last name, family name, or surname for the user.
      --mobile string         Mobile phone number for the user.
      --orgRole strings       Unique 24-digit string that identifies the organization, colon, and the user's role  for the organization. Specify this value as orgID:ROLE. Valid values for ROLE include ORG_OWNER, ORG_MEMBER, ORG_GROUP_CREATOR, ORG_BILLING_ADMIN, and ORG_READ_ONLY.
  -o, --output string         Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --password string       Password for the user.
      --projectRole strings   Unique 24-digit string that identifies the project, colon, and the user's role for the project. Specify this value as projectID:ROLE. Valid values for ROLE include GROUP_CLUSTER_MANAGER, GROUP_DATA_ACCESS_ADMIN, GROUP_DATA_ACCESS_READ_ONLY, GROUP_DATA_ACCESS_READ_WRITE, GROUP_OWNER, and GROUP_READ_ONLY.
      --username string       Name that identifies the user. You must specify a valid email address.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas users](atlas_users.md)	- Manage your Atlas users.



