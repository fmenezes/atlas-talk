## atlas integrations create PAGER_DUTY

Create or update a PagerDuty integration for your project.


### Synopsis

The requesting API key must have the Organization Owner or Project Owner role to configure an integration with PagerDuty.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas integrations create PAGER_DUTY [flags]
atlas integrations create pager_duty [flags]
atlas integrations create pagerDuty [flags]
atlas integrations update PAGER_DUTY [flags]
atlas integrations update pager_duty [flags]
atlas integrations update pagerDuty [flags]
atlas integration create PAGER_DUTY [flags]
atlas integration create pager_duty [flags]
atlas integration create pagerDuty [flags]
atlas integration update PAGER_DUTY [flags]
atlas integration update pager_duty [flags]
atlas integration update pagerDuty [flags]
```

### Examples

```
  # Integrate PagerDuty with Atlas for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas integrations create PAGER_DUTY --serviceKey a1a23bcdef45ghijk6789 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help                help for PAGER_DUTY
  -o, --output string       Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --serviceKey string   Service key associated with your PagerDuty account.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas integrations create](atlas_integrations_create.md)	- Create operations.



