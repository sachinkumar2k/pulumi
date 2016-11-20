// Copyright 2016 Marapongo, Inc. All rights reserved.

package cmd

import (
	"flag"
	"strconv"

	"github.com/golang/glog"
	"github.com/spf13/cobra"
)

func NewMuCmd() *cobra.Command {
	var logToStderr bool
	var verbose int
	cmd := &cobra.Command{
		Use:   "mu",
		Short: "Mu is a framework and toolset for reusable stacks of services",
		PersistentPreRun: func(cmd *cobra.Command, args []string) {
			// Ensure the glog library has been initialized, including calling flag.Parse beforehand.  Unfortunately,
			// this is the only way to control the way glog runs.  That includes poking around at flags below.
			flag.Parse()
			glog.Info("Mu CLI is running")

			if logToStderr {
				flag.Lookup("logtostderr").Value.Set("true")
			}
			if verbose > 0 {
				flag.Lookup("v").Value.Set(strconv.Itoa(verbose))
			}
		},
		PersistentPostRun: func(cmd *cobra.Command, args []string) {
			glog.Flush()
		},
	}

	cmd.PersistentFlags().BoolVar(&logToStderr, "logtostderr", false, "Log to stderr instead of to files")
	cmd.PersistentFlags().IntVarP(
		&verbose, "verbose", "v", 0, "Enable verbose logging (e.g., v=3); anything >3 is very verbose")

	cmd.AddCommand(newBuildCmd())
	cmd.AddCommand(newVersionCmd())

	return cmd
}
