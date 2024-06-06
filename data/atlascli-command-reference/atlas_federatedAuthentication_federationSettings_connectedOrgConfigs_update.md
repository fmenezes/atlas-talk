## atlas federatedAuthentication federationSettings connectedOrgConfigs update

Update One Org Config Connected to One Federation Setting.


### Usage
```
atlas federatedAuthentication federationSettings connectedOrgConfigs update [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings connectedOrgConfigs update
atlas federatedAuthentication federationSettings connectedorgconfigs update
atlas federatedAuthentication federationSettings connected-org-configs update
atlas federatedAuthentication federationSettings connectedOrgConfig update
atlas federatedAuthentication federationSettings connectedorgconfig update
atlas federatedAuthentication federationSettings connected-org-config update
atlas federatedAuthentication federationsettings connectedOrgConfigs update
atlas federatedAuthentication federationsettings connectedorgconfigs update
atlas federatedAuthentication federationsettings connected-org-configs update
atlas federatedAuthentication federationsettings connectedOrgConfig update
atlas federatedAuthentication federationsettings connectedorgconfig update
atlas federatedAuthentication federationsettings connected-org-config update
atlas federatedAuthentication federation-settings connectedOrgConfigs update
atlas federatedAuthentication federation-settings connectedorgconfigs update
atlas federatedAuthentication federation-settings connected-org-configs update
atlas federatedAuthentication federation-settings connectedOrgConfig update
atlas federatedAuthentication federation-settings connectedorgconfig update
atlas federatedAuthentication federation-settings connected-org-config update
atlas federatedAuthentication federationSetting connectedOrgConfigs update
atlas federatedAuthentication federationSetting connectedorgconfigs update
atlas federatedAuthentication federationSetting connected-org-configs update
atlas federatedAuthentication federationSetting connectedOrgConfig update
atlas federatedAuthentication federationSetting connectedorgconfig update
atlas federatedAuthentication federationSetting connected-org-config update
atlas federatedAuthentication federationsetting connectedOrgConfigs update
atlas federatedAuthentication federationsetting connectedorgconfigs update
atlas federatedAuthentication federationsetting connected-org-configs update
atlas federatedAuthentication federationsetting connectedOrgConfig update
atlas federatedAuthentication federationsetting connectedorgconfig update
atlas federatedAuthentication federationsetting connected-org-config update
atlas federatedAuthentication federation-setting connectedOrgConfigs update
atlas federatedAuthentication federation-setting connectedorgconfigs update
atlas federatedAuthentication federation-setting connected-org-configs update
atlas federatedAuthentication federation-setting connectedOrgConfig update
atlas federatedAuthentication federation-setting connectedorgconfig update
atlas federatedAuthentication federation-setting connected-org-config update
atlas federatedauthentication federationSettings connectedOrgConfigs update
atlas federatedauthentication federationSettings connectedorgconfigs update
atlas federatedauthentication federationSettings connected-org-configs update
atlas federatedauthentication federationSettings connectedOrgConfig update
atlas federatedauthentication federationSettings connectedorgconfig update
atlas federatedauthentication federationSettings connected-org-config update
atlas federatedauthentication federationsettings connectedOrgConfigs update
atlas federatedauthentication federationsettings connectedorgconfigs update
atlas federatedauthentication federationsettings connected-org-configs update
atlas federatedauthentication federationsettings connectedOrgConfig update
atlas federatedauthentication federationsettings connectedorgconfig update
atlas federatedauthentication federationsettings connected-org-config update
atlas federatedauthentication federation-settings connectedOrgConfigs update
atlas federatedauthentication federation-settings connectedorgconfigs update
atlas federatedauthentication federation-settings connected-org-configs update
atlas federatedauthentication federation-settings connectedOrgConfig update
atlas federatedauthentication federation-settings connectedorgconfig update
atlas federatedauthentication federation-settings connected-org-config update
atlas federatedauthentication federationSetting connectedOrgConfigs update
atlas federatedauthentication federationSetting connectedorgconfigs update
atlas federatedauthentication federationSetting connected-org-configs update
atlas federatedauthentication federationSetting connectedOrgConfig update
atlas federatedauthentication federationSetting connectedorgconfig update
atlas federatedauthentication federationSetting connected-org-config update
atlas federatedauthentication federationsetting connectedOrgConfigs update
atlas federatedauthentication federationsetting connectedorgconfigs update
atlas federatedauthentication federationsetting connected-org-configs update
atlas federatedauthentication federationsetting connectedOrgConfig update
atlas federatedauthentication federationsetting connectedorgconfig update
atlas federatedauthentication federationsetting connected-org-config update
atlas federatedauthentication federation-setting connectedOrgConfigs update
atlas federatedauthentication federation-setting connectedorgconfigs update
atlas federatedauthentication federation-setting connected-org-configs update
atlas federatedauthentication federation-setting connectedOrgConfig update
atlas federatedauthentication federation-setting connectedorgconfig update
atlas federatedauthentication federation-setting connected-org-config update
atlas federated-authentication federationSettings connectedOrgConfigs update
atlas federated-authentication federationSettings connectedorgconfigs update
atlas federated-authentication federationSettings connected-org-configs update
atlas federated-authentication federationSettings connectedOrgConfig update
atlas federated-authentication federationSettings connectedorgconfig update
atlas federated-authentication federationSettings connected-org-config update
atlas federated-authentication federationsettings connectedOrgConfigs update
atlas federated-authentication federationsettings connectedorgconfigs update
atlas federated-authentication federationsettings connected-org-configs update
atlas federated-authentication federationsettings connectedOrgConfig update
atlas federated-authentication federationsettings connectedorgconfig update
atlas federated-authentication federationsettings connected-org-config update
atlas federated-authentication federation-settings connectedOrgConfigs update
atlas federated-authentication federation-settings connectedorgconfigs update
atlas federated-authentication federation-settings connected-org-configs update
atlas federated-authentication federation-settings connectedOrgConfig update
atlas federated-authentication federation-settings connectedorgconfig update
atlas federated-authentication federation-settings connected-org-config update
atlas federated-authentication federationSetting connectedOrgConfigs update
atlas federated-authentication federationSetting connectedorgconfigs update
atlas federated-authentication federationSetting connected-org-configs update
atlas federated-authentication federationSetting connectedOrgConfig update
atlas federated-authentication federationSetting connectedorgconfig update
atlas federated-authentication federationSetting connected-org-config update
atlas federated-authentication federationsetting connectedOrgConfigs update
atlas federated-authentication federationsetting connectedorgconfigs update
atlas federated-authentication federationsetting connected-org-configs update
atlas federated-authentication federationsetting connectedOrgConfig update
atlas federated-authentication federationsetting connectedorgconfig update
atlas federated-authentication federationsetting connected-org-config update
atlas federated-authentication federation-setting connectedOrgConfigs update
atlas federated-authentication federation-setting connectedorgconfigs update
atlas federated-authentication federation-setting connected-org-configs update
atlas federated-authentication federation-setting connectedOrgConfig update
atlas federated-authentication federation-setting connectedorgconfig update
atlas federated-authentication federation-setting connected-org-config update
```

### Examples

```
  # Update the connected orgs config the current profile org and federationSettingsId 5d1113b25a115342acc2d1aa using the JSON configuration file config.json
			atlas federatedAuthentication connectedOrgs update --federationSettingsId 5d1113b25a115342acc2d1aa --file config.json
		
```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
      --file string                   Path to a JSON configuration file that defines connected orgs configurations. To learn more about connected org configuration file format, see the request body in https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Federated-Authentication/operation/updateConnectedOrgConfig.
  -h, --help                          help for update
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings connectedOrgConfigs](atlas_federatedAuthentication_federationSettings_connectedOrgConfigs.md)	- Manage Atlas Federated Authentication Connected Orgs Config



