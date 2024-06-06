## atlas networking peering create azure

Create a network peering connection between the Atlas VPC and your Azure VNet.


### Synopsis

Before you create an Azure network peering connection, complete the prerequisites listed here: https://www.mongodb.com/docs/atlas/reference/api/vpc-create-peering-connection/#prerequisites.
		
The network peering create command checks if a VNet exists in the region you specify for your Atlas project. If one exists, this command creates the peering connection between that VNet and your VPC. If an Atlas VPC does not exist, this command creates one and creates a connection between it and your VNet.
		
To learn more about network peering connections, see https://www.mongodb.com/docs/atlas/security-vpc-peering/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas networking peering create azure [flags]
```

### Aliases
```

atlas networking peering create azure
```

### Examples

```
  # Create a network peering connection between the Atlas VPC in CIDR block 192.168.0.0/24 and your Azure VNet named atlascli-test in in US_EAST_2:
  atlas networking peering create azure --atlasCidrBlock 192.168.0.0/24 --directoryId 56657fdb-ca45-40dc-fr56-77fd8b6d2b37 --subscriptionId 345654f3-77cf-4084-9e06-8943a079ed75 --resourceGroup atlascli-test --region US_EAST_2 --vnet atlascli-test
```


### Flags

```
      --atlasCidrBlock string   CIDR block that Atlas uses for all network peering connections created in the project. This option is required only if you do not already have an Atlas VPC. To learn more, see the Atlas UI tab at https://dochub.mongodb.org/core/peering-connection-atlas.
      --directoryId string      Unique identifier for an Azure AD directory.
  -h, --help                    help for azure
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string           Cloud provider region where the VPC that you peered with the Atlas VPC resides.
      --resourceGroup string    Name of your Azure resource group.
      --subscriptionId string   Unique identifier of the Azure subscription in which the VNet resides.
      --vnet string             Name of your Azure VNet.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas networking peering create](atlas_networking_peering_create.md)	- Create a connection with AWS, Azure and Google Cloud.



