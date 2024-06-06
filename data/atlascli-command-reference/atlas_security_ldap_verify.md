## atlas security ldap verify

Request verification of an LDAP configuration for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas security ldap verify [flags]
```

### Examples

```
  # Request the JSON-formatted verification of the LDAP configuration for the atlas-ldaps-01.ldap.myteam.com host in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security ldap verify --hostname atlas-ldaps-01.ldap.myteam.com --bindUsername "CN=Administrator,CN=Users,DC=atlas-ldaps-01,DC=myteam,DC=com" --bindPassword changeMe --projectId 5e2211c17a3e5a48f5497de3 --output json

```


### Flags

```
      --authzQueryTemplate string   RFC 4515-formatted or RFC 4516-formatted LDAP query template that Atlas executes to obtain the LDAP authorization groups to which the authenticated user belongs. Use the {USER} placeholder in the URL to substitute the username. The query is relative to the host specified with the hostname.
      --bindPassword string         Password used to authenticate the bindUsername.
      --bindUsername string         User distinguished name (DN) that Atlas uses to connect to the LDAP server. You must format LDAP distinguished names according to RFC 2253.
      --caCertificate string        Certificate Authority (CA) used to verify the identity of the LDAP server. To delete an assigned value, pass an empty string.
  -h, --help                        help for verify
      --hostname string             Hostname or IP address of the LDAP server.
  -o, --output string               Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --port int                    Port that the LDAP server listens to for client connections. (default 636)
      --projectId string            Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas security ldap](atlas_security_ldap.md)	- LDAP operations.

* [atlas security ldap verify status](atlas_security_ldap_verify_status.md)	- Get the status of an LDAP configuration request.



