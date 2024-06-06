## atlas customDns aws describe

Describe the custom DNS configuration of an Atlas cluster deployed to AWS in the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas customDns aws describe [flags]
```

### Aliases
```

atlas customDns aws describe
atlas customDns aws get
atlas customDns aw describe
atlas customDns aw get
atlas customdns aws describe
atlas customdns aws get
atlas customdns aw describe
atlas customdns aw get
atlas custom-dns aws describe
atlas custom-dns aws get
atlas custom-dns aw describe
atlas custom-dns aw get
atlas customDn aws describe
atlas customDn aws get
atlas customDn aw describe
atlas customDn aw get
atlas customdn aws describe
atlas customdn aws get
atlas customdn aw describe
atlas customdn aw get
atlas custom-dn aws describe
atlas custom-dn aws get
atlas custom-dn aw describe
atlas custom-dn aw get
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

### See Also


* [atlas customDns aws](atlas_customDns_aws.md)	- Manage DNS configuration of an Atlas project’s cluster deployed to AWS.



