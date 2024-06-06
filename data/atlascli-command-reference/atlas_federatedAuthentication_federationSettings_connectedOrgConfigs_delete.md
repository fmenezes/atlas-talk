## atlas federatedAuthentication federationSettings connectedOrgConfigs delete

Delete a connected org config Organization.


### Usage
```
atlas federatedAuthentication federationSettings connectedOrgConfigs delete [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings connectedOrgConfigs delete
atlas federatedAuthentication federationSettings connectedorgconfigs delete
atlas federatedAuthentication federationSettings connected-org-configs delete
atlas federatedAuthentication federationSettings connectedOrgConfig delete
atlas federatedAuthentication federationSettings connectedorgconfig delete
atlas federatedAuthentication federationSettings connected-org-config delete
atlas federatedAuthentication federationsettings connectedOrgConfigs delete
atlas federatedAuthentication federationsettings connectedorgconfigs delete
atlas federatedAuthentication federationsettings connected-org-configs delete
atlas federatedAuthentication federationsettings connectedOrgConfig delete
atlas federatedAuthentication federationsettings connectedorgconfig delete
atlas federatedAuthentication federationsettings connected-org-config delete
atlas federatedAuthentication federation-settings connectedOrgConfigs delete
atlas federatedAuthentication federation-settings connectedorgconfigs delete
atlas federatedAuthentication federation-settings connected-org-configs delete
atlas federatedAuthentication federation-settings connectedOrgConfig delete
atlas federatedAuthentication federation-settings connectedorgconfig delete
atlas federatedAuthentication federation-settings connected-org-config delete
atlas federatedAuthentication federationSetting connectedOrgConfigs delete
atlas federatedAuthentication federationSetting connectedorgconfigs delete
atlas federatedAuthentication federationSetting connected-org-configs delete
atlas federatedAuthentication federationSetting connectedOrgConfig delete
atlas federatedAuthentication federationSetting connectedorgconfig delete
atlas federatedAuthentication federationSetting connected-org-config delete
atlas federatedAuthentication federationsetting connectedOrgConfigs delete
atlas federatedAuthentication federationsetting connectedorgconfigs delete
atlas federatedAuthentication federationsetting connected-org-configs delete
atlas federatedAuthentication federationsetting connectedOrgConfig delete
atlas federatedAuthentication federationsetting connectedorgconfig delete
atlas federatedAuthentication federationsetting connected-org-config delete
atlas federatedAuthentication federation-setting connectedOrgConfigs delete
atlas federatedAuthentication federation-setting connectedorgconfigs delete
atlas federatedAuthentication federation-setting connected-org-configs delete
atlas federatedAuthentication federation-setting connectedOrgConfig delete
atlas federatedAuthentication federation-setting connectedorgconfig delete
atlas federatedAuthentication federation-setting connected-org-config delete
atlas federatedauthentication federationSettings connectedOrgConfigs delete
atlas federatedauthentication federationSettings connectedorgconfigs delete
atlas federatedauthentication federationSettings connected-org-configs delete
atlas federatedauthentication federationSettings connectedOrgConfig delete
atlas federatedauthentication federationSettings connectedorgconfig delete
atlas federatedauthentication federationSettings connected-org-config delete
atlas federatedauthentication federationsettings connectedOrgConfigs delete
atlas federatedauthentication federationsettings connectedorgconfigs delete
atlas federatedauthentication federationsettings connected-org-configs delete
atlas federatedauthentication federationsettings connectedOrgConfig delete
atlas federatedauthentication federationsettings connectedorgconfig delete
atlas federatedauthentication federationsettings connected-org-config delete
atlas federatedauthentication federation-settings connectedOrgConfigs delete
atlas federatedauthentication federation-settings connectedorgconfigs delete
atlas federatedauthentication federation-settings connected-org-configs delete
atlas federatedauthentication federation-settings connectedOrgConfig delete
atlas federatedauthentication federation-settings connectedorgconfig delete
atlas federatedauthentication federation-settings connected-org-config delete
atlas federatedauthentication federationSetting connectedOrgConfigs delete
atlas federatedauthentication federationSetting connectedorgconfigs delete
atlas federatedauthentication federationSetting connected-org-configs delete
atlas federatedauthentication federationSetting connectedOrgConfig delete
atlas federatedauthentication federationSetting connectedorgconfig delete
atlas federatedauthentication federationSetting connected-org-config delete
atlas federatedauthentication federationsetting connectedOrgConfigs delete
atlas federatedauthentication federationsetting connectedorgconfigs delete
atlas federatedauthentication federationsetting connected-org-configs delete
atlas federatedauthentication federationsetting connectedOrgConfig delete
atlas federatedauthentication federationsetting connectedorgconfig delete
atlas federatedauthentication federationsetting connected-org-config delete
atlas federatedauthentication federation-setting connectedOrgConfigs delete
atlas federatedauthentication federation-setting connectedorgconfigs delete
atlas federatedauthentication federation-setting connected-org-configs delete
atlas federatedauthentication federation-setting connectedOrgConfig delete
atlas federatedauthentication federation-setting connectedorgconfig delete
atlas federatedauthentication federation-setting connected-org-config delete
atlas federated-authentication federationSettings connectedOrgConfigs delete
atlas federated-authentication federationSettings connectedorgconfigs delete
atlas federated-authentication federationSettings connected-org-configs delete
atlas federated-authentication federationSettings connectedOrgConfig delete
atlas federated-authentication federationSettings connectedorgconfig delete
atlas federated-authentication federationSettings connected-org-config delete
atlas federated-authentication federationsettings connectedOrgConfigs delete
atlas federated-authentication federationsettings connectedorgconfigs delete
atlas federated-authentication federationsettings connected-org-configs delete
atlas federated-authentication federationsettings connectedOrgConfig delete
atlas federated-authentication federationsettings connectedorgconfig delete
atlas federated-authentication federationsettings connected-org-config delete
atlas federated-authentication federation-settings connectedOrgConfigs delete
atlas federated-authentication federation-settings connectedorgconfigs delete
atlas federated-authentication federation-settings connected-org-configs delete
atlas federated-authentication federation-settings connectedOrgConfig delete
atlas federated-authentication federation-settings connectedorgconfig delete
atlas federated-authentication federation-settings connected-org-config delete
atlas federated-authentication federationSetting connectedOrgConfigs delete
atlas federated-authentication federationSetting connectedorgconfigs delete
atlas federated-authentication federationSetting connected-org-configs delete
atlas federated-authentication federationSetting connectedOrgConfig delete
atlas federated-authentication federationSetting connectedorgconfig delete
atlas federated-authentication federationSetting connected-org-config delete
atlas federated-authentication federationsetting connectedOrgConfigs delete
atlas federated-authentication federationsetting connectedorgconfigs delete
atlas federated-authentication federationsetting connected-org-configs delete
atlas federated-authentication federationsetting connectedOrgConfig delete
atlas federated-authentication federationsetting connectedorgconfig delete
atlas federated-authentication federationsetting connected-org-config delete
atlas federated-authentication federation-setting connectedOrgConfigs delete
atlas federated-authentication federation-setting connectedorgconfigs delete
atlas federated-authentication federation-setting connected-org-configs delete
atlas federated-authentication federation-setting connectedOrgConfig delete
atlas federated-authentication federation-setting connectedorgconfig delete
atlas federated-authentication federation-setting connected-org-config delete
```

### Examples

```
  # Delete a connected org config from the current profile org and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgs delete --federationSettingsId 5d1113b25a115342acc2d1aa 
			# Delete a connected org config from the org with ID 7d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgs connect --orgId 7d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa 
		
```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
      --force                         Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                          help for delete
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings connectedOrgConfigs](atlas_federatedAuthentication_federationSettings_connectedOrgConfigs.md)	- Manage Atlas Federated Authentication Connected Orgs Config



