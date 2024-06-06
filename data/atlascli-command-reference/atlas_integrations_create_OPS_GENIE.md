## atlas integrations create OPS_GENIE

Create or update an Opsgenie integration for your project.


### Synopsis

The requesting API key must have the Organization Owner or Project Owner role to configure an integration with Opsgenie.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas integrations create OPS_GENIE [flags]
```

### Aliases
```

atlas integrations create OPS_GENIE
atlas integrations create ops_genie
atlas integrations create opsGenie
atlas integrations update OPS_GENIE
atlas integrations update ops_genie
atlas integrations update opsGenie
atlas integration create OPS_GENIE
atlas integration create ops_genie
atlas integration create opsGenie
atlas integration update OPS_GENIE
atlas integration update ops_genie
atlas integration update opsGenie
```

### Examples

```
  # Integrate Opsgenie with Atlas for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations create OPS_GENIE --apiKey a1a23bcdef45ghijk6789 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --apiKey string      Opsgenie API key that allows Atlas to access your Opsgenie account.
  -h, --help               help for OPS_GENIE
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string      Code that indicates which regional URL MongoDB uses to access the third-party API. Valid values are US and EU. (default "US")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas integrations create](atlas_integrations_create.md)	- Create operations.



