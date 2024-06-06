## atlas organizations apiKeys accessLists create

Create an IP access list entry for your API Key.


### Synopsis

To view possible values for the apiKey option, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Read Write role.


### Usage
```
atlas organizations apiKeys accessLists create [flags]
```

### Aliases
```

atlas organizations apiKeys accessLists create
atlas organizations apiKeys accesslists create
atlas organizations apiKeys access-lists create
atlas organizations apiKeys accessList create
atlas organizations apiKeys accesslist create
atlas organizations apiKeys access-list create
atlas organizations apiKeys whitelists create
atlas organizations apiKeys whitelist create
atlas organizations apikeys accessLists create
atlas organizations apikeys accesslists create
atlas organizations apikeys access-lists create
atlas organizations apikeys accessList create
atlas organizations apikeys accesslist create
atlas organizations apikeys access-list create
atlas organizations apikeys whitelists create
atlas organizations apikeys whitelist create
atlas organizations api-keys accessLists create
atlas organizations api-keys accesslists create
atlas organizations api-keys access-lists create
atlas organizations api-keys accessList create
atlas organizations api-keys accesslist create
atlas organizations api-keys access-list create
atlas organizations api-keys whitelists create
atlas organizations api-keys whitelist create
atlas organizations apiKey accessLists create
atlas organizations apiKey accesslists create
atlas organizations apiKey access-lists create
atlas organizations apiKey accessList create
atlas organizations apiKey accesslist create
atlas organizations apiKey access-list create
atlas organizations apiKey whitelists create
atlas organizations apiKey whitelist create
atlas organizations apikey accessLists create
atlas organizations apikey accesslists create
atlas organizations apikey access-lists create
atlas organizations apikey accessList create
atlas organizations apikey accesslist create
atlas organizations apikey access-list create
atlas organizations apikey whitelists create
atlas organizations apikey whitelist create
atlas organizations api-key accessLists create
atlas organizations api-key accesslists create
atlas organizations api-key access-lists create
atlas organizations api-key accessList create
atlas organizations api-key accesslist create
atlas organizations api-key access-list create
atlas organizations api-key whitelists create
atlas organizations api-key whitelist create
atlas organization apiKeys accessLists create
atlas organization apiKeys accesslists create
atlas organization apiKeys access-lists create
atlas organization apiKeys accessList create
atlas organization apiKeys accesslist create
atlas organization apiKeys access-list create
atlas organization apiKeys whitelists create
atlas organization apiKeys whitelist create
atlas organization apikeys accessLists create
atlas organization apikeys accesslists create
atlas organization apikeys access-lists create
atlas organization apikeys accessList create
atlas organization apikeys accesslist create
atlas organization apikeys access-list create
atlas organization apikeys whitelists create
atlas organization apikeys whitelist create
atlas organization api-keys accessLists create
atlas organization api-keys accesslists create
atlas organization api-keys access-lists create
atlas organization api-keys accessList create
atlas organization api-keys accesslist create
atlas organization api-keys access-list create
atlas organization api-keys whitelists create
atlas organization api-keys whitelist create
atlas organization apiKey accessLists create
atlas organization apiKey accesslists create
atlas organization apiKey access-lists create
atlas organization apiKey accessList create
atlas organization apiKey accesslist create
atlas organization apiKey access-list create
atlas organization apiKey whitelists create
atlas organization apiKey whitelist create
atlas organization apikey accessLists create
atlas organization apikey accesslists create
atlas organization apikey access-lists create
atlas organization apikey accessList create
atlas organization apikey accesslist create
atlas organization apikey access-list create
atlas organization apikey whitelists create
atlas organization apikey whitelist create
atlas organization api-key accessLists create
atlas organization api-key accesslists create
atlas organization api-key access-lists create
atlas organization api-key accessList create
atlas organization api-key accesslist create
atlas organization api-key access-list create
atlas organization api-key whitelists create
atlas organization api-key whitelist create
atlas orgs apiKeys accessLists create
atlas orgs apiKeys accesslists create
atlas orgs apiKeys access-lists create
atlas orgs apiKeys accessList create
atlas orgs apiKeys accesslist create
atlas orgs apiKeys access-list create
atlas orgs apiKeys whitelists create
atlas orgs apiKeys whitelist create
atlas orgs apikeys accessLists create
atlas orgs apikeys accesslists create
atlas orgs apikeys access-lists create
atlas orgs apikeys accessList create
atlas orgs apikeys accesslist create
atlas orgs apikeys access-list create
atlas orgs apikeys whitelists create
atlas orgs apikeys whitelist create
atlas orgs api-keys accessLists create
atlas orgs api-keys accesslists create
atlas orgs api-keys access-lists create
atlas orgs api-keys accessList create
atlas orgs api-keys accesslist create
atlas orgs api-keys access-list create
atlas orgs api-keys whitelists create
atlas orgs api-keys whitelist create
atlas orgs apiKey accessLists create
atlas orgs apiKey accesslists create
atlas orgs apiKey access-lists create
atlas orgs apiKey accessList create
atlas orgs apiKey accesslist create
atlas orgs apiKey access-list create
atlas orgs apiKey whitelists create
atlas orgs apiKey whitelist create
atlas orgs apikey accessLists create
atlas orgs apikey accesslists create
atlas orgs apikey access-lists create
atlas orgs apikey accessList create
atlas orgs apikey accesslist create
atlas orgs apikey access-list create
atlas orgs apikey whitelists create
atlas orgs apikey whitelist create
atlas orgs api-key accessLists create
atlas orgs api-key accesslists create
atlas orgs api-key access-lists create
atlas orgs api-key accessList create
atlas orgs api-key accesslist create
atlas orgs api-key access-list create
atlas orgs api-key whitelists create
atlas orgs api-key whitelist create
atlas org apiKeys accessLists create
atlas org apiKeys accesslists create
atlas org apiKeys access-lists create
atlas org apiKeys accessList create
atlas org apiKeys accesslist create
atlas org apiKeys access-list create
atlas org apiKeys whitelists create
atlas org apiKeys whitelist create
atlas org apikeys accessLists create
atlas org apikeys accesslists create
atlas org apikeys access-lists create
atlas org apikeys accessList create
atlas org apikeys accesslist create
atlas org apikeys access-list create
atlas org apikeys whitelists create
atlas org apikeys whitelist create
atlas org api-keys accessLists create
atlas org api-keys accesslists create
atlas org api-keys access-lists create
atlas org api-keys accessList create
atlas org api-keys accesslist create
atlas org api-keys access-list create
atlas org api-keys whitelists create
atlas org api-keys whitelist create
atlas org apiKey accessLists create
atlas org apiKey accesslists create
atlas org apiKey access-lists create
atlas org apiKey accessList create
atlas org apiKey accesslist create
atlas org apiKey access-list create
atlas org apiKey whitelists create
atlas org apiKey whitelist create
atlas org apikey accessLists create
atlas org apikey accesslists create
atlas org apikey access-lists create
atlas org apikey accessList create
atlas org apikey accesslist create
atlas org apikey access-list create
atlas org apikey whitelists create
atlas org apikey whitelist create
atlas org api-key accessLists create
atlas org api-key accesslists create
atlas org api-key access-lists create
atlas org api-key accessList create
atlas org api-key accesslist create
atlas org api-key access-list create
atlas org api-key whitelists create
atlas org api-key whitelist create
```

### Examples

```
  # Create access list entries for two IP addresses for the API key with the ID 5f24084d8dbffa3ad3f21234 in the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys accessLists create --apiKey 5f24084d8dbffa3ad3f21234 --cidr 192.0.2.0/24,198.51.100.0/24 --orgId 5a1b39eec902201990f12345 --output json
```


### Flags

```
      --apiKey string   Unique 24-digit ID that identifies your API key.
      --cidr strings    Access list entry in CIDR notation to be added for your API key. To add more than one entry, you can specify each entry with a separate cidr flag or specify all the entries as a comma-separated list using one cidr flag. You can't set both cidr and ip in the same command.
      --currentIp       Flag that adds the IP address from the host that is currently executing the command to the access list. Only applicable for type ipAddress entries. You don't need the entry argument when you use the currentIp option.
  -h, --help            help for create
      --ip strings      IP address to add to the access list for your API key. To add more than one IP address, specify each address with a separate ip flag or specify all addresses as a comma-separated list using one ip flag. You can't set both ip and cidr in the same command.
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas organizations apiKeys accessLists](atlas_organizations_apiKeys_accessLists.md)	- Manage the IP access list for your API Key.



