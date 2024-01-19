# 0x0A. Configuration Management

## DevOps | SysAdmin | Scripting | CI/CD

## Background Context

During my time at SlideShare, I encountered a critical incident involving an auto-remediation tool named Skynet. This tool monitored, scaled, and fixed Cloud infrastructure using a parallel job-execution system called MCollective. An unexpected bug in the code resulted in sending nil to the filter method.

Two pieces of bad news followed:

1. When MCollective receives nil as an argument for its filter method, it interprets it as 'all servers.'
2. The action I sent was to terminate the selected servers.

The consequence was severe - 75% of all conversion infrastructure servers were shut down, affecting users' ability to convert their documents. Thanks to Puppet, we were able to restore our infrastructure within 1 hour. Imagine the manual effort required to launch servers, configure and link them, import application code, start every process, and fix all the bugs. Puppet proved invaluable in this scenario, emphasizing the long-term benefits of infrastructure as code.

[My Tweet about the incident](https://twitter.com/devopsreact/status/836971570136375296)

## Resources
Read or watch:
- [Intro to Configuration Management](#)
- [Puppet resource type: file](#) (check "Resource types" for all manifest types in the left menu)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](#)
- [Puppet lint](#)
- [Puppet emacs mode](#)

## Requirements

### General
- All your files will be interpreted on Ubuntu 20.04 LTS.
- All your files should end with a new line.
- A README.md file at the root of the folder of the project is mandatory.
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Your Puppet manifests must run without error.
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about.
- Your Puppet manifests files must end with the extension .pp.

### Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet:
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax, which is virtually identical in newer versions of Puppet.

[Puppet 5 Docs](#)

Install puppet-lint:
```bash
$ gem install puppet-lint
```
