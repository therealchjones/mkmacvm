# `mkmacvm`

Build a simple macOS virtual machine for Parallels Desktop with minimal
interaction

## Requirements

`mkmacvm` is designed to work with:

- macOS 12.2 Monterey
- Paralells Desktop Pro 17

`mkmacvm` may work with older or alternative versions of the above software, but
each release of `mkmacvm` is only tested with its contemporary versions of macOS
and Parallels Desktop Pro.

## Usage

1. In Terminal, on the macOS host computer:

   ```shell
   sudo ./mkmacvm
   ```

2. When prompted, within the new virtual machine, choose a language, then open a
   terminal and run:

   ```shell
   /Volumes/Image Volume/install
   ```

3. There is no step 3.

## Aims

`mkmacvm` will provide a simple program that creates a macOS virtual machine on
a macOS host without user interaction beyond initiation.

To meet these aims, `mkmacvm` should:

- be a single executable (or script or bundle or similar)
- support a command-line interface (to allow easy inclusion in scripts)
- not be configurable (beyond text or display output) by the end user
- not require software other than macOS, itself, and the virtual machine
  software
- not leave remains other than the virtual machine files (such as temporary
  files, `mkmacvm` preferences, etc.) on the host machine
- by default run silently without user interaction

## FAQ

- Why did I get an error that reads:

  ```shell
  Error erasing disk error number (22, 0) An error occurred erasing the disk.
  ```

  I have no idea. I don't know what it means or why it happens. However, thanks
  to
  [this post](https://www.blackmanticore.com/659444a81916ef87765c979e4231753d),
  I can tell you that it likely happened after a previous attempt failed, and I
  can recommend rebooting your computer as a reasonable and reliable fix (until
  it happens again).

## Similar Projects

Though it does not share any meaningful source code with them, `mkmacvm` is
heavily inspired by these excellent projects:

- [macdeploystick](https://bitbucket.org/twocanoes/macdeploystick/src/master/):
  configure settings to deploy macOS with minimal interaction and multiple
  hardware and software tools

- [pycreateuserpkg](https://github.com/gregneagle/pycreateuserpkg): create macOS
  user accounts from the command line

Please see [LICENSE](LICENSE) for further acknowledgment of their contributions.
