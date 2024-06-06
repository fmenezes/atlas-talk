## atlas completion powershell

Generate the autocompletion script for powershell


### Synopsis

Generate the autocompletion script for powershell.

To load completions in your current shell session:

	atlas completion powershell | Out-String | Invoke-Expression

To load completions for every new session, add the output of the above command
to your powershell profile.




```

atlas completion powershell [flags]
```



### Flags

```
  -h, --help              help for powershell
      --no-descriptions   disable completion descriptions

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas completion](atlas_completion.md)	- Generate the autocompletion script for the specified shell



