## atlas customDns aws describe

Describe the custom DNS configuration of an Atlas cluster deployed to AWS in the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas customDns aws describe [flags]
atlas customDns aws get [flags]
atlas customDns aw describe [flags]
atlas customDns aw get [flags]
atlas customdns aws describe [flags]
atlas customdns aws get [flags]
atlas customdns aw describe [flags]
atlas customdns aw get [flags]
atlas custom-dns aws describe [flags]
atlas custom-dns aws get [flags]
atlas custom-dns aw describe [flags]
atlas custom-dns aw get [flags]
atlas customDn aws describe [flags]
atlas customDn aws get [flags]
atlas customDn aw describe [flags]
atlas customDn aw get [flags]
atlas customdn aws describe [flags]
atlas customdn aws get [flags]
atlas customdn aw describe [flags]
atlas customdn aw get [flags]
atlas custom-dn aws describe [flags]
atlas custom-dn aws get [flags]
atlas custom-dn aw describe [flags]
atlas custom-dn aw get [flags]
```

### Examples

```
  # Return the details for the custom DNS configuration deployed to AWS in the project with ID 618d48e05277a606ed2496fe:		
  atlas customDns aws describe --projectId 618d48e05277a606ed2496fe 
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas customDns aws](atlas_customDns_aws.md)	- Manage DNS configuration of an Atlas project’s cluster deployed to AWS.



