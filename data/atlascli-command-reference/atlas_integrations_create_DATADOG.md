## atlas integrations create DATADOG

Create or update a Datadog integration for your project.


### Synopsis

The requesting API key must have the Organization Owner or Project Owner role to configure an integration with Datadog.

After you integrate with Datadog, you can send metric data about your project to your Datadog dashboard. To learn more about the metrics available to Datadog, see https://www.mongodb.com/docs/atlas/tutorial/datadog-integration/.
		
Datadog integration is available only for M10+ clusters.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas integrations create DATADOG [flags]
atlas integrations create datadog [flags]
atlas integrations update DATADOG [flags]
atlas integrations update datadog [flags]
atlas integration create DATADOG [flags]
atlas integration create datadog [flags]
atlas integration update DATADOG [flags]
atlas integration update datadog [flags]
```

### Examples

```
  # Integrate Datadog with Atlas for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations create DATADOG --apiKey a1a23bcdef45ghijk6789 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --apiKey string      Datadog API key that allows Atlas to access your Datadog account.
  -h, --help               help for DATADOG
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string      Code that indicates which regional URL MongoDB uses to access the Datadog API. Valid values are US, EU, US3, US5, and AP1. (default "US")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas integrations create](atlas_integrations_create.md)	- Create operations.



