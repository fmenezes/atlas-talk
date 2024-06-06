## atlas liveMigrations validation create

Create a new validation request for a push live migration.


### Synopsis

To migrate using scripts, use mongomirror instead of the Atlas CLI. To learn more about mongomirror, see https://www.mongodb.com/docs/atlas/reference/mongomirror/.



```

atlas liveMigrations validation create [flags]
atlas livemigrations validation create [flags]
atlas live-migrations validation create [flags]
atlas liveMigration validation create [flags]
atlas livemigration validation create [flags]
atlas live-migration validation create [flags]
atlas lm validation create [flags]
```



### Flags

```
      --clusterName string               Human-readable label that identifies the Atlas destination cluster.
      --drop                             Flag that indicates whether this process should drop existing collections from the destination (Atlas) cluster given in --destinationClusterName before starting the migration of data from the source cluster.
      --force                            Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                             help for create
      --migrationHost strings            List of hosts running the MongoDB Agent that can transfer your MongoDB data from the source (Cloud Manager or Ops Manager) to destination (Atlas) deployments. Each live migration process uses its own dedicated migration host.
  -o, --output string                    Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                 Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --sourceCACertificatePath string   Path to the CA certificate that signed TLS certificates use to authenticate to the source Cloud Manager or Ops Manager cluster. Omit this value if --sourceSSL is not passed.
      --sourceClusterName string         Human-readable label that identifies the source Cloud Manager or Ops Manager cluster.
      --sourceManagedAuthentication      Flag that indicates whether MongoDB Automation manages authentication to the source Cloud Manager or Ops Manager cluster. If you set this to true, don't provide values for --sourceUsername and --sourcePassword.
  -p, --sourcePassword string            Password that authenticates the username to the source Cloud Manager or Ops Manager cluster. Omit this value if --sourceManagedAuthentication is passed.
      --sourceProjectId string           Unique 24-hexadecimal digit string that identifies the source project.
      --sourceSsl                        Flag that indicates whether data source has TLS enabled.
  -u, --sourceUsername string            Human-readable label that identifies the SCRAM-SHA user that connects to the source Cloud Manager or Ops Manager cluster. Omit this value if --sourceManagedAuthentication is set.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas liveMigrations validation](atlas_liveMigrations_validation.md)	- Manage a Live Migration validation job for your project.



