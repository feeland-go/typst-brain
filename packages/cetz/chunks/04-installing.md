## Installing

To install the CeTZ package under your local typst package dir you can use the `install` script from the repository.

just install

The installed version can be imported by prefixing the package name with `@local`.

#import "@local/cetz:0.4.2"

#cetz.canvas({
  import cetz.draw: *
  // Your drawing code goes here
})

### Just

This project uses just, a handy command runner.

You can run all commands without having `just` installed, just have a look into the `justfile`.
To install `just` on your system, use your systems package manager. On Windows, Cargo (`cargo install just`), Chocolatey (`choco install just`) and some other sources can be used. You need to run it from a `sh` compatible shell on Windows (e.g git-bash).