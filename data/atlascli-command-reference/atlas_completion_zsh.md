## atlas completion zsh

Generate the autocompletion script for zsh


### Synopsis

Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

	echo "autoload -U compinit; compinit" >> ~/.zshrc

To load completions in your current shell session:

	source <(atlas completion zsh)

To load completions for every new session, execute once:

#### Linux:

	atlas completion zsh > "${fpath[1]}/_atlas"

#### macOS:

	atlas completion zsh > $(brew --prefix)/share/zsh/site-functions/_atlas

You will need to start a new shell for this setup to take effect.




```

atlas completion zsh [flags]
```



### Flags

```
  -h, --help              help for zsh
      --no-descriptions   disable completion descriptions

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas completion](atlas_completion.md)	- Generate the autocompletion script for the specified shell



