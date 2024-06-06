## atlas federatedAuthentication federationSettings connectedOrgConfigs disconnect

Connect an Identity Provider to an Organization.


### Usage
```
atlas federatedAuthentication federationSettings connectedOrgConfigs disconnect [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings connectedOrgConfigs disconnect
atlas federatedAuthentication federationSettings connectedorgconfigs disconnect
atlas federatedAuthentication federationSettings connected-org-configs disconnect
atlas federatedAuthentication federationSettings connectedOrgConfig disconnect
atlas federatedAuthentication federationSettings connectedorgconfig disconnect
atlas federatedAuthentication federationSettings connected-org-config disconnect
atlas federatedAuthentication federationsettings connectedOrgConfigs disconnect
atlas federatedAuthentication federationsettings connectedorgconfigs disconnect
atlas federatedAuthentication federationsettings connected-org-configs disconnect
atlas federatedAuthentication federationsettings connectedOrgConfig disconnect
atlas federatedAuthentication federationsettings connectedorgconfig disconnect
atlas federatedAuthentication federationsettings connected-org-config disconnect
atlas federatedAuthentication federation-settings connectedOrgConfigs disconnect
atlas federatedAuthentication federation-settings connectedorgconfigs disconnect
atlas federatedAuthentication federation-settings connected-org-configs disconnect
atlas federatedAuthentication federation-settings connectedOrgConfig disconnect
atlas federatedAuthentication federation-settings connectedorgconfig disconnect
atlas federatedAuthentication federation-settings connected-org-config disconnect
atlas federatedAuthentication federationSetting connectedOrgConfigs disconnect
atlas federatedAuthentication federationSetting connectedorgconfigs disconnect
atlas federatedAuthentication federationSetting connected-org-configs disconnect
atlas federatedAuthentication federationSetting connectedOrgConfig disconnect
atlas federatedAuthentication federationSetting connectedorgconfig disconnect
atlas federatedAuthentication federationSetting connected-org-config disconnect
atlas federatedAuthentication federationsetting connectedOrgConfigs disconnect
atlas federatedAuthentication federationsetting connectedorgconfigs disconnect
atlas federatedAuthentication federationsetting connected-org-configs disconnect
atlas federatedAuthentication federationsetting connectedOrgConfig disconnect
atlas federatedAuthentication federationsetting connectedorgconfig disconnect
atlas federatedAuthentication federationsetting connected-org-config disconnect
atlas federatedAuthentication federation-setting connectedOrgConfigs disconnect
atlas federatedAuthentication federation-setting connectedorgconfigs disconnect
atlas federatedAuthentication federation-setting connected-org-configs disconnect
atlas federatedAuthentication federation-setting connectedOrgConfig disconnect
atlas federatedAuthentication federation-setting connectedorgconfig disconnect
atlas federatedAuthentication federation-setting connected-org-config disconnect
atlas federatedauthentication federationSettings connectedOrgConfigs disconnect
atlas federatedauthentication federationSettings connectedorgconfigs disconnect
atlas federatedauthentication federationSettings connected-org-configs disconnect
atlas federatedauthentication federationSettings connectedOrgConfig disconnect
atlas federatedauthentication federationSettings connectedorgconfig disconnect
atlas federatedauthentication federationSettings connected-org-config disconnect
atlas federatedauthentication federationsettings connectedOrgConfigs disconnect
atlas federatedauthentication federationsettings connectedorgconfigs disconnect
atlas federatedauthentication federationsettings connected-org-configs disconnect
atlas federatedauthentication federationsettings connectedOrgConfig disconnect
atlas federatedauthentication federationsettings connectedorgconfig disconnect
atlas federatedauthentication federationsettings connected-org-config disconnect
atlas federatedauthentication federation-settings connectedOrgConfigs disconnect
atlas federatedauthentication federation-settings connectedorgconfigs disconnect
atlas federatedauthentication federation-settings connected-org-configs disconnect
atlas federatedauthentication federation-settings connectedOrgConfig disconnect
atlas federatedauthentication federation-settings connectedorgconfig disconnect
atlas federatedauthentication federation-settings connected-org-config disconnect
atlas federatedauthentication federationSetting connectedOrgConfigs disconnect
atlas federatedauthentication federationSetting connectedorgconfigs disconnect
atlas federatedauthentication federationSetting connected-org-configs disconnect
atlas federatedauthentication federationSetting connectedOrgConfig disconnect
atlas federatedauthentication federationSetting connectedorgconfig disconnect
atlas federatedauthentication federationSetting connected-org-config disconnect
atlas federatedauthentication federationsetting connectedOrgConfigs disconnect
atlas federatedauthentication federationsetting connectedorgconfigs disconnect
atlas federatedauthentication federationsetting connected-org-configs disconnect
atlas federatedauthentication federationsetting connectedOrgConfig disconnect
atlas federatedauthentication federationsetting connectedorgconfig disconnect
atlas federatedauthentication federationsetting connected-org-config disconnect
atlas federatedauthentication federation-setting connectedOrgConfigs disconnect
atlas federatedauthentication federation-setting connectedorgconfigs disconnect
atlas federatedauthentication federation-setting connected-org-configs disconnect
atlas federatedauthentication federation-setting connectedOrgConfig disconnect
atlas federatedauthentication federation-setting connectedorgconfig disconnect
atlas federatedauthentication federation-setting connected-org-config disconnect
atlas federated-authentication federationSettings connectedOrgConfigs disconnect
atlas federated-authentication federationSettings connectedorgconfigs disconnect
atlas federated-authentication federationSettings connected-org-configs disconnect
atlas federated-authentication federationSettings connectedOrgConfig disconnect
atlas federated-authentication federationSettings connectedorgconfig disconnect
atlas federated-authentication federationSettings connected-org-config disconnect
atlas federated-authentication federationsettings connectedOrgConfigs disconnect
atlas federated-authentication federationsettings connectedorgconfigs disconnect
atlas federated-authentication federationsettings connected-org-configs disconnect
atlas federated-authentication federationsettings connectedOrgConfig disconnect
atlas federated-authentication federationsettings connectedorgconfig disconnect
atlas federated-authentication federationsettings connected-org-config disconnect
atlas federated-authentication federation-settings connectedOrgConfigs disconnect
atlas federated-authentication federation-settings connectedorgconfigs disconnect
atlas federated-authentication federation-settings connected-org-configs disconnect
atlas federated-authentication federation-settings connectedOrgConfig disconnect
atlas federated-authentication federation-settings connectedorgconfig disconnect
atlas federated-authentication federation-settings connected-org-config disconnect
atlas federated-authentication federationSetting connectedOrgConfigs disconnect
atlas federated-authentication federationSetting connectedorgconfigs disconnect
atlas federated-authentication federationSetting connected-org-configs disconnect
atlas federated-authentication federationSetting connectedOrgConfig disconnect
atlas federated-authentication federationSetting connectedorgconfig disconnect
atlas federated-authentication federationSetting connected-org-config disconnect
atlas federated-authentication federationsetting connectedOrgConfigs disconnect
atlas federated-authentication federationsetting connectedorgconfigs disconnect
atlas federated-authentication federationsetting connected-org-configs disconnect
atlas federated-authentication federationsetting connectedOrgConfig disconnect
atlas federated-authentication federationsetting connectedorgconfig disconnect
atlas federated-authentication federationsetting connected-org-config disconnect
atlas federated-authentication federation-setting connectedOrgConfigs disconnect
atlas federated-authentication federation-setting connectedorgconfigs disconnect
atlas federated-authentication federation-setting connected-org-configs disconnect
atlas federated-authentication federation-setting connectedOrgConfig disconnect
atlas federated-authentication federation-setting connectedorgconfig disconnect
atlas federated-authentication federation-setting connected-org-config disconnect
```

### Examples

```
  # Disconnect the current profile org from identity provider with ID 5d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgs disconnect --identityProviderId 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa 
			# Connect the org with ID 7d1113b25a115342acc2d1aa to identity provider with ID 5d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa 
			atlas federatedAuthentication connectedOrgs disconnect --orgId 7d1113b25a115342acc2d1aa --identityProviderId 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa 
		
```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for disconnect
      --identityProviderId string     Unique identifier of the identity provider.
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --protocol string               Protocol used to authenticate the user. Valid value is OIDC or SAML. (default "OIDC")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings connectedOrgConfigs](atlas_federatedAuthentication_federationSettings_connectedOrgConfigs.md)	- Manage Atlas Federated Authentication Connected Orgs Config



