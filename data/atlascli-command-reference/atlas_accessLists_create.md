## atlas accessLists create

Create an IP access list entry for your project.


### Synopsis

The access list can contain trusted IP addresses, AWS security group IDs, and entries in Classless Inter-Domain Routing (CIDR) notation. You can add only one access list entry at a time. You can create one access list per project. 
		
The command doesn't overwrite existing entries in the access list. Instead, it adds the new entries to the list of entries.

To use this command, you must authenticate with a user account or an API key with the Read Write role.



```

atlas accessLists create <entry> [flags]
atlas accesslists create <entry> [flags]
atlas access-lists create <entry> [flags]
atlas accessList create <entry> [flags]
atlas accesslist create <entry> [flags]
atlas access-list create <entry> [flags]
atlas whitelists create <entry> [flags]
atlas whitelist create <entry> [flags]
```

### Examples

```
  # Create an IP access list entry using the current IP address:
  atlas accessList create --currentIp
  
  # Create an access list entry for the IP address 192.0.2.15 in the project with ID 5e2211c17a3e5a48f5497de3:
  atlas accessList create 192.0.2.15 --type ipAddress --projectId 5e2211c17a3e5a48f5497de3 --comment "IP address for app server 2" --output json
  
  # Create an access list entry in CIDR notation for 73.231.201.205/24 in the project with ID 5e2211c17a3e5a48f5497de3:
  atlas accessList create 73.231.201.205/24 --type cidrBlock --projectId 5e2211c17a3e5a48f5497de3 --output json --comment "CIDR block for servers C - F"
  
  # Create an access list entry for the AWS security group sg-903004f8 in the project with ID 5e2211c17a3e5a48f5497de3:
  atlas accessList create sg-903004f8 --type awsSecurityGroup
  --projectId 5e2211c17a3e5a48f5497de3 --output json --comment "AWS Security Group"
```


### Flags

```
      --comment string       Optional description or comment for the entry.
      --currentIp            Flag that adds the IP address from the host that is currently executing the command to the access list. Only applicable for type ipAddress entries. You don't need the entry argument when you use the currentIp option.
      --deleteAfter string   ISO-8601-formatted UTC date after which Atlas removes the entry from the access list.
  -h, --help                 help for create
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string          Type of access list entry. Valid values are cidrBlock, ipAddress, or awsSecurityGroup. (default "ipAddress")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas accessLists](atlas_accessLists.md)	- Manage the list of IP addresses that can access your Atlas project.



