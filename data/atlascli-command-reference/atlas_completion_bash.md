## atlas completion bash

Generate the autocompletion script for bash


### Synopsis

Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package.
If it is not installed already, you can install it via your OS's package manager.

To load completions in your current shell session:

	source <(atlas completion bash)

To load completions for every new session, execute once:

#### Linux:

	atlas completion bash > /etc/bash_completion.d/atlas

#### macOS:

	atlas completion bash > $(brew --prefix)/etc/bash_completion.d/atlas

You will need to start a new shell for this setup to take effect.



### Usage
```
atlas completion bash
```

### Aliases
```

atlas completion bash
```



### Flags

```
  -h, --help              help for bash
      --no-descriptions   disable completion descriptions

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas completion](atlas_completion.md)	- Generate the autocompletion script for the specified shell



