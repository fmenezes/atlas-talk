## atlas networking peering create gcp

Create a network peering connection between the Atlas VPC and your Google Cloud VPC.


### Synopsis

The network peering create command checks if a VPC exists in the region you specify for your Atlas project. If one exists, this command creates the peering connection between that VPC and your VPC. If an Atlas VPC doesn't exist, this command creates one and creates a connection between it and your VPC.
		
To learn more about network peering connections, see https://www.mongodb.com/docs/atlas/security-vpc-peering/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas networking peering create gcp [flags]
```

### Examples

```
  # Create a network peering connection between the Atlas VPC in CIDR block 192.168.0.0/24 and your GCP VPC with the GCP project ID grandiose-branch-256701 in the network named cli-test:
  atlas networking peering create gcp --atlasCidrBlock 192.168.0.0/24 --gcpProjectId grandiose-branch-256701 --network cli-test --output json
```


### Flags

```
      --atlasCidrBlock string   CIDR block that Atlas uses for all network peering connections created in the project. This option is required only if you do not already have an Atlas VPC. To learn more, see the Atlas UI tab at https://dochub.mongodb.org/core/peering-connection-atlas.
      --gcpProjectId string     Unique identifier of the GCP project in which the network peer resides.
  -h, --help                    help for gcp
      --network string          Unique identifier of the Network Peering connection in the Atlas project.
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region strings          List of Atlas regions where the container resides.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas networking peering create](atlas_networking_peering_create.md)	- Create a connection with AWS, Azure and Google Cloud.



