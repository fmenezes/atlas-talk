## atlas integrations create WEBHOOK

Create or update a webhook integration for your project.


### Synopsis

The requesting API key must have the Organization Owner or Project Owner role to configure a webhook integration.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas integrations create WEBHOOK [flags]
atlas integrations create webhook [flags]
atlas integrations update WEBHOOK [flags]
atlas integrations update webhook [flags]
atlas integration create WEBHOOK [flags]
atlas integration create webhook [flags]
atlas integration update WEBHOOK [flags]
atlas integration update webhook [flags]
```

### Examples

```
  # Integrate a webhook with Atlas that uses the secret mySecret for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations create WEBHOOK --url http://9b4ac7aa.abc.io/payload --secret mySecret --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for WEBHOOK
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --secret string      Secret that secures your webhook.
      --url string         Endpoint web address to which Atlas sends notifications.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas integrations create](atlas_integrations_create.md)	- Create operations.



