## atlas networking peering create aws

Create a network peering connection between the Atlas VPC and your AWS VPC.


### Synopsis

The network peering create command checks if a VPC exists in the region you specify for your Atlas project. If one exists, this command creates the peering connection between that VPC and your VPC. If an Atlas VPC doesn't exist, this command creates one and creates a connection between it and your VPC.
		
To learn more about network peering connections, see https://www.mongodb.com/docs/atlas/security-vpc-peering/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas networking peering create aws [flags]
```

### Aliases
```

atlas networking peering create aws
```

### Examples

```
  # Create a network peering connection between the Atlas VPC in CIDR block 192.168.0.0/24 and your AWS VPC in CIDR block 10.0.0.0/24 for AWS account number 854333054055:
  atlas networking peering create aws --accountId 854333054055 --atlasCidrBlock 192.168.0.0/24 --region us-east-1 --routeTableCidrBlock 10.0.0.0/24 --vpcId vpc-078ac381aa90e1e63
```


### Flags

```
      --accountId string             Unique twelve-digit AWS account ID that owns the peer VPC.
      --atlasCidrBlock string        CIDR block that Atlas uses for all network peering connections created in the project. This option is required only if you do not already have an Atlas VPC. To learn more, see the Atlas UI tab at https://dochub.mongodb.org/core/peering-connection-atlas.
  -h, --help                         help for aws
  -o, --output string                Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string             Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string                Cloud provider region where the VPC that you peered with the Atlas VPC resides.
      --routeTableCidrBlock string   Peer VPC CIDR block or subnet.
      --vpcId string                 Unique identifier of the peer VPC.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas networking peering create](atlas_networking_peering_create.md)	- Create a connection with AWS, Azure and Google Cloud.



