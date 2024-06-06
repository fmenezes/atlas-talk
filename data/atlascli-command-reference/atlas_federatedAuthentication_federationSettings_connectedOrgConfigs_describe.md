## atlas federatedAuthentication federationSettings connectedOrgConfigs describe

Describe a Connected Org Config.


### Usage
```
atlas federatedAuthentication federationSettings connectedOrgConfigs describe [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings connectedOrgConfigs describe
atlas federatedAuthentication federationSettings connectedorgconfigs describe
atlas federatedAuthentication federationSettings connected-org-configs describe
atlas federatedAuthentication federationSettings connectedOrgConfig describe
atlas federatedAuthentication federationSettings connectedorgconfig describe
atlas federatedAuthentication federationSettings connected-org-config describe
atlas federatedAuthentication federationsettings connectedOrgConfigs describe
atlas federatedAuthentication federationsettings connectedorgconfigs describe
atlas federatedAuthentication federationsettings connected-org-configs describe
atlas federatedAuthentication federationsettings connectedOrgConfig describe
atlas federatedAuthentication federationsettings connectedorgconfig describe
atlas federatedAuthentication federationsettings connected-org-config describe
atlas federatedAuthentication federation-settings connectedOrgConfigs describe
atlas federatedAuthentication federation-settings connectedorgconfigs describe
atlas federatedAuthentication federation-settings connected-org-configs describe
atlas federatedAuthentication federation-settings connectedOrgConfig describe
atlas federatedAuthentication federation-settings connectedorgconfig describe
atlas federatedAuthentication federation-settings connected-org-config describe
atlas federatedAuthentication federationSetting connectedOrgConfigs describe
atlas federatedAuthentication federationSetting connectedorgconfigs describe
atlas federatedAuthentication federationSetting connected-org-configs describe
atlas federatedAuthentication federationSetting connectedOrgConfig describe
atlas federatedAuthentication federationSetting connectedorgconfig describe
atlas federatedAuthentication federationSetting connected-org-config describe
atlas federatedAuthentication federationsetting connectedOrgConfigs describe
atlas federatedAuthentication federationsetting connectedorgconfigs describe
atlas federatedAuthentication federationsetting connected-org-configs describe
atlas federatedAuthentication federationsetting connectedOrgConfig describe
atlas federatedAuthentication federationsetting connectedorgconfig describe
atlas federatedAuthentication federationsetting connected-org-config describe
atlas federatedAuthentication federation-setting connectedOrgConfigs describe
atlas federatedAuthentication federation-setting connectedorgconfigs describe
atlas federatedAuthentication federation-setting connected-org-configs describe
atlas federatedAuthentication federation-setting connectedOrgConfig describe
atlas federatedAuthentication federation-setting connectedorgconfig describe
atlas federatedAuthentication federation-setting connected-org-config describe
atlas federatedauthentication federationSettings connectedOrgConfigs describe
atlas federatedauthentication federationSettings connectedorgconfigs describe
atlas federatedauthentication federationSettings connected-org-configs describe
atlas federatedauthentication federationSettings connectedOrgConfig describe
atlas federatedauthentication federationSettings connectedorgconfig describe
atlas federatedauthentication federationSettings connected-org-config describe
atlas federatedauthentication federationsettings connectedOrgConfigs describe
atlas federatedauthentication federationsettings connectedorgconfigs describe
atlas federatedauthentication federationsettings connected-org-configs describe
atlas federatedauthentication federationsettings connectedOrgConfig describe
atlas federatedauthentication federationsettings connectedorgconfig describe
atlas federatedauthentication federationsettings connected-org-config describe
atlas federatedauthentication federation-settings connectedOrgConfigs describe
atlas federatedauthentication federation-settings connectedorgconfigs describe
atlas federatedauthentication federation-settings connected-org-configs describe
atlas federatedauthentication federation-settings connectedOrgConfig describe
atlas federatedauthentication federation-settings connectedorgconfig describe
atlas federatedauthentication federation-settings connected-org-config describe
atlas federatedauthentication federationSetting connectedOrgConfigs describe
atlas federatedauthentication federationSetting connectedorgconfigs describe
atlas federatedauthentication federationSetting connected-org-configs describe
atlas federatedauthentication federationSetting connectedOrgConfig describe
atlas federatedauthentication federationSetting connectedorgconfig describe
atlas federatedauthentication federationSetting connected-org-config describe
atlas federatedauthentication federationsetting connectedOrgConfigs describe
atlas federatedauthentication federationsetting connectedorgconfigs describe
atlas federatedauthentication federationsetting connected-org-configs describe
atlas federatedauthentication federationsetting connectedOrgConfig describe
atlas federatedauthentication federationsetting connectedorgconfig describe
atlas federatedauthentication federationsetting connected-org-config describe
atlas federatedauthentication federation-setting connectedOrgConfigs describe
atlas federatedauthentication federation-setting connectedorgconfigs describe
atlas federatedauthentication federation-setting connected-org-configs describe
atlas federatedauthentication federation-setting connectedOrgConfig describe
atlas federatedauthentication federation-setting connectedorgconfig describe
atlas federatedauthentication federation-setting connected-org-config describe
atlas federated-authentication federationSettings connectedOrgConfigs describe
atlas federated-authentication federationSettings connectedorgconfigs describe
atlas federated-authentication federationSettings connected-org-configs describe
atlas federated-authentication federationSettings connectedOrgConfig describe
atlas federated-authentication federationSettings connectedorgconfig describe
atlas federated-authentication federationSettings connected-org-config describe
atlas federated-authentication federationsettings connectedOrgConfigs describe
atlas federated-authentication federationsettings connectedorgconfigs describe
atlas federated-authentication federationsettings connected-org-configs describe
atlas federated-authentication federationsettings connectedOrgConfig describe
atlas federated-authentication federationsettings connectedorgconfig describe
atlas federated-authentication federationsettings connected-org-config describe
atlas federated-authentication federation-settings connectedOrgConfigs describe
atlas federated-authentication federation-settings connectedorgconfigs describe
atlas federated-authentication federation-settings connected-org-configs describe
atlas federated-authentication federation-settings connectedOrgConfig describe
atlas federated-authentication federation-settings connectedorgconfig describe
atlas federated-authentication federation-settings connected-org-config describe
atlas federated-authentication federationSetting connectedOrgConfigs describe
atlas federated-authentication federationSetting connectedorgconfigs describe
atlas federated-authentication federationSetting connected-org-configs describe
atlas federated-authentication federationSetting connectedOrgConfig describe
atlas federated-authentication federationSetting connectedorgconfig describe
atlas federated-authentication federationSetting connected-org-config describe
atlas federated-authentication federationsetting connectedOrgConfigs describe
atlas federated-authentication federationsetting connectedorgconfigs describe
atlas federated-authentication federationsetting connected-org-configs describe
atlas federated-authentication federationsetting connectedOrgConfig describe
atlas federated-authentication federationsetting connectedorgconfig describe
atlas federated-authentication federationsetting connected-org-config describe
atlas federated-authentication federation-setting connectedOrgConfigs describe
atlas federated-authentication federation-setting connectedorgconfigs describe
atlas federated-authentication federation-setting connected-org-configs describe
atlas federated-authentication federation-setting connectedOrgConfig describe
atlas federated-authentication federation-setting connectedorgconfig describe
atlas federated-authentication federation-setting connected-org-config describe
```

### Examples

```
  # Describe a connected org config with the current profile org and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgsConfig connect --federationSettingsId 5d1113b25a115342acc2d1aa 
			# Describe a connected org config with the org with ID 7d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgs connect --orgId 7d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa 
		
```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for describe
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings connectedOrgConfigs](atlas_federatedAuthentication_federationSettings_connectedOrgConfigs.md)	- Manage Atlas Federated Authentication Connected Orgs Config



