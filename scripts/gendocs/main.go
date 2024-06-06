package main

import (
	"log"
	"os"
	"path/filepath"

	"github.com/mongodb/mongodb-atlas-cli/atlascli/internal/cli/root"
	"github.com/spf13/cobra/doc"
)

func run() error {
	cmd := root.Builder()

	dest, err := filepath.Abs("../../docs")
	if err != nil {
		return err
	}

	if err := os.RemoveAll(dest); err != nil {
		return err
	}

	if err := os.MkdirAll(dest, os.ModePerm); err != nil {
		return err
	}

	if err := doc.GenMarkdownTree(cmd, dest); err != nil {
		return err
	}

	return nil
}

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}
