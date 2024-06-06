## atlas clusters indexes create

Create a rolling index for the specified cluster for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters indexes create <indexName> [flags]
```

### Aliases
```

atlas clusters indexes create
atlas clusters index create
atlas cluster indexes create
atlas cluster index create
```

### Examples

```
  # Create an index named bedrooms_1 on the listings collection of the realestate database:
  atlas clusters indexes create bedrooms_1 --clusterName Cluster0 --collection listings --db realestate --key bedrooms:1
  
  # Create a compound index named property_room_bedrooms on the
  listings collection of the realestate database:
  atlas clusters indexes create property_room_bedrooms --clusterName Cluster0 --collection listings --db realestate --key property_type:1 --key room_type:1 --key bedrooms:1

  # Create an index named my_index from a JSON configuration file named myfile.json:
  atlas clusters indexes create my_index --clusterName Cluster0 --file file.json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --collection string    Name of the collection.
      --db string            Name of the database.
  -f, --file string          Path to an optional JSON configuration file that defines index settings.
  -h, --help                 help for create
      --key strings          Field to be indexed and the type of index in the following format: field:type.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --sparse               Flag that creates a sparse index. To learn more, see https://dochub.mongodb.org/core/index-sparse-manual.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters indexes](atlas_clusters_indexes.md)	- Manage cluster rolling indexes for your project.



