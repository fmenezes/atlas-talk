## atlas customDns aws disable

Disable the custom DNS configuration of an Atlas cluster deployed to AWS in the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas customDns aws disable [flags]
atlas customDns aw disable [flags]
atlas customdns aws disable [flags]
atlas customdns aw disable [flags]
atlas custom-dns aws disable [flags]
atlas custom-dns aw disable [flags]
atlas customDn aws disable [flags]
atlas customDn aw disable [flags]
atlas customdn aws disable [flags]
atlas customdn aw disable [flags]
atlas custom-dn aws disable [flags]
atlas custom-dn aw disable [flags]
```

### Examples

```
  # Disable the custom DNS configuration deployed to AWS in the project with ID 618d48e05277a606ed2496fe:		
  atlas customDns aws disable --projectId 618d48e05277a606ed2496fe 
```


### Flags

```
  -h, --help               help for disable
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas customDns aws](atlas_customDns_aws.md)	- Manage DNS configuration of an Atlas project’s cluster deployed to AWS.



