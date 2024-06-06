## atlas integrations create VICTOR_OPS

Create or update a Splunk On-Call integration for your project.


### Synopsis

VictorOps is now Splunk On-Call.
		
The requesting API key must have the Organization Owner or Project Owner role to configure an integration with Splunk On-Call.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas integrations create VICTOR_OPS [flags]
```

### Aliases
```

atlas integrations create VICTOR_OPS
atlas integrations create victor_ops
atlas integrations create victorOps
atlas integrations update VICTOR_OPS
atlas integrations update victor_ops
atlas integrations update victorOps
atlas integration create VICTOR_OPS
atlas integration create victor_ops
atlas integration create victorOps
atlas integration update VICTOR_OPS
atlas integration update victor_ops
atlas integration update victorOps
```

### Examples

```
  # Integrate Splunk On-Call with Atlas using the routing key operations for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations create VICTOR_OPS --apiKey a1a23bcdef45ghijk6789 --routingKey operations --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --apiKey string       Splunk On-Call API key that allows Atlas to access your Splunk On-Call account.
  -h, --help                help for VICTOR_OPS
  -o, --output string       Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --routingKey string   Routing key associated with your Splunk On-Call account.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas integrations create](atlas_integrations_create.md)	- Create operations.



