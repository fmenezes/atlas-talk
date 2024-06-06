## atlas federatedAuthentication federationSettings connectedOrgConfigs list

Describe a Connected Org Config.


### Usage
```
atlas federatedAuthentication federationSettings connectedOrgConfigs list [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings connectedOrgConfigs list
atlas federatedAuthentication federationSettings connectedorgconfigs list
atlas federatedAuthentication federationSettings connected-org-configs list
atlas federatedAuthentication federationSettings connectedOrgConfig list
atlas federatedAuthentication federationSettings connectedorgconfig list
atlas federatedAuthentication federationSettings connected-org-config list
atlas federatedAuthentication federationsettings connectedOrgConfigs list
atlas federatedAuthentication federationsettings connectedorgconfigs list
atlas federatedAuthentication federationsettings connected-org-configs list
atlas federatedAuthentication federationsettings connectedOrgConfig list
atlas federatedAuthentication federationsettings connectedorgconfig list
atlas federatedAuthentication federationsettings connected-org-config list
atlas federatedAuthentication federation-settings connectedOrgConfigs list
atlas federatedAuthentication federation-settings connectedorgconfigs list
atlas federatedAuthentication federation-settings connected-org-configs list
atlas federatedAuthentication federation-settings connectedOrgConfig list
atlas federatedAuthentication federation-settings connectedorgconfig list
atlas federatedAuthentication federation-settings connected-org-config list
atlas federatedAuthentication federationSetting connectedOrgConfigs list
atlas federatedAuthentication federationSetting connectedorgconfigs list
atlas federatedAuthentication federationSetting connected-org-configs list
atlas federatedAuthentication federationSetting connectedOrgConfig list
atlas federatedAuthentication federationSetting connectedorgconfig list
atlas federatedAuthentication federationSetting connected-org-config list
atlas federatedAuthentication federationsetting connectedOrgConfigs list
atlas federatedAuthentication federationsetting connectedorgconfigs list
atlas federatedAuthentication federationsetting connected-org-configs list
atlas federatedAuthentication federationsetting connectedOrgConfig list
atlas federatedAuthentication federationsetting connectedorgconfig list
atlas federatedAuthentication federationsetting connected-org-config list
atlas federatedAuthentication federation-setting connectedOrgConfigs list
atlas federatedAuthentication federation-setting connectedorgconfigs list
atlas federatedAuthentication federation-setting connected-org-configs list
atlas federatedAuthentication federation-setting connectedOrgConfig list
atlas federatedAuthentication federation-setting connectedorgconfig list
atlas federatedAuthentication federation-setting connected-org-config list
atlas federatedauthentication federationSettings connectedOrgConfigs list
atlas federatedauthentication federationSettings connectedorgconfigs list
atlas federatedauthentication federationSettings connected-org-configs list
atlas federatedauthentication federationSettings connectedOrgConfig list
atlas federatedauthentication federationSettings connectedorgconfig list
atlas federatedauthentication federationSettings connected-org-config list
atlas federatedauthentication federationsettings connectedOrgConfigs list
atlas federatedauthentication federationsettings connectedorgconfigs list
atlas federatedauthentication federationsettings connected-org-configs list
atlas federatedauthentication federationsettings connectedOrgConfig list
atlas federatedauthentication federationsettings connectedorgconfig list
atlas federatedauthentication federationsettings connected-org-config list
atlas federatedauthentication federation-settings connectedOrgConfigs list
atlas federatedauthentication federation-settings connectedorgconfigs list
atlas federatedauthentication federation-settings connected-org-configs list
atlas federatedauthentication federation-settings connectedOrgConfig list
atlas federatedauthentication federation-settings connectedorgconfig list
atlas federatedauthentication federation-settings connected-org-config list
atlas federatedauthentication federationSetting connectedOrgConfigs list
atlas federatedauthentication federationSetting connectedorgconfigs list
atlas federatedauthentication federationSetting connected-org-configs list
atlas federatedauthentication federationSetting connectedOrgConfig list
atlas federatedauthentication federationSetting connectedorgconfig list
atlas federatedauthentication federationSetting connected-org-config list
atlas federatedauthentication federationsetting connectedOrgConfigs list
atlas federatedauthentication federationsetting connectedorgconfigs list
atlas federatedauthentication federationsetting connected-org-configs list
atlas federatedauthentication federationsetting connectedOrgConfig list
atlas federatedauthentication federationsetting connectedorgconfig list
atlas federatedauthentication federationsetting connected-org-config list
atlas federatedauthentication federation-setting connectedOrgConfigs list
atlas federatedauthentication federation-setting connectedorgconfigs list
atlas federatedauthentication federation-setting connected-org-configs list
atlas federatedauthentication federation-setting connectedOrgConfig list
atlas federatedauthentication federation-setting connectedorgconfig list
atlas federatedauthentication federation-setting connected-org-config list
atlas federated-authentication federationSettings connectedOrgConfigs list
atlas federated-authentication federationSettings connectedorgconfigs list
atlas federated-authentication federationSettings connected-org-configs list
atlas federated-authentication federationSettings connectedOrgConfig list
atlas federated-authentication federationSettings connectedorgconfig list
atlas federated-authentication federationSettings connected-org-config list
atlas federated-authentication federationsettings connectedOrgConfigs list
atlas federated-authentication federationsettings connectedorgconfigs list
atlas federated-authentication federationsettings connected-org-configs list
atlas federated-authentication federationsettings connectedOrgConfig list
atlas federated-authentication federationsettings connectedorgconfig list
atlas federated-authentication federationsettings connected-org-config list
atlas federated-authentication federation-settings connectedOrgConfigs list
atlas federated-authentication federation-settings connectedorgconfigs list
atlas federated-authentication federation-settings connected-org-configs list
atlas federated-authentication federation-settings connectedOrgConfig list
atlas federated-authentication federation-settings connectedorgconfig list
atlas federated-authentication federation-settings connected-org-config list
atlas federated-authentication federationSetting connectedOrgConfigs list
atlas federated-authentication federationSetting connectedorgconfigs list
atlas federated-authentication federationSetting connected-org-configs list
atlas federated-authentication federationSetting connectedOrgConfig list
atlas federated-authentication federationSetting connectedorgconfig list
atlas federated-authentication federationSetting connected-org-config list
atlas federated-authentication federationsetting connectedOrgConfigs list
atlas federated-authentication federationsetting connectedorgconfigs list
atlas federated-authentication federationsetting connected-org-configs list
atlas federated-authentication federationsetting connectedOrgConfig list
atlas federated-authentication federationsetting connectedorgconfig list
atlas federated-authentication federationsetting connected-org-config list
atlas federated-authentication federation-setting connectedOrgConfigs list
atlas federated-authentication federation-setting connectedorgconfigs list
atlas federated-authentication federation-setting connected-org-configs list
atlas federated-authentication federation-setting connectedOrgConfig list
atlas federated-authentication federation-setting connectedorgconfig list
atlas federated-authentication federation-setting connected-org-config list
```

### Examples

```
  # List all connected org config with federationSettingsId 5d1113b25a115342acc2d1aa 
  atlas federatedAuthentication connectedOrgsConfig list --federationSettingsId 5d1113b25a115342acc2d1aa 

```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for list
      --limit int                     Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int                      Page number that specifies a page of results. (default 1)

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings connectedOrgConfigs](atlas_federatedAuthentication_federationSettings_connectedOrgConfigs.md)	- Manage Atlas Federated Authentication Connected Orgs Config



