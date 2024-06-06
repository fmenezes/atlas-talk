## atlas clusters availableRegions list

List available regions that Atlas supports for new deployments.


### Usage
```
atlas clusters availableRegions list [flags]
```

### Aliases
```

atlas clusters availableRegions list
atlas clusters availableRegions ls
atlas clusters availableregions list
atlas clusters availableregions ls
atlas clusters available-regions list
atlas clusters available-regions ls
atlas clusters availableRegion list
atlas clusters availableRegion ls
atlas clusters availableregion list
atlas clusters availableregion ls
atlas clusters available-region list
atlas clusters available-region ls
atlas cluster availableRegions list
atlas cluster availableRegions ls
atlas cluster availableregions list
atlas cluster availableregions ls
atlas cluster available-regions list
atlas cluster available-regions ls
atlas cluster availableRegion list
atlas cluster availableRegion ls
atlas cluster availableregion list
atlas cluster availableregion ls
atlas cluster available-region list
atlas cluster available-region ls
```

### Examples

```
  # List available regions for a given cloud provider and tier:
  atlas cluster availableRegions list --provider AWS --tier M50

  # List available regions by tier for a given provider:
  atlas cluster availableRegions list --provider GCP
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string    Name of your cloud service provider. Valid values are AWS, AZURE, or GCP.
      --tier string        Tier for each data-bearing server in the cluster. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters availableRegions](atlas_clusters_availableRegions.md)	- Manage available regions for your project.



