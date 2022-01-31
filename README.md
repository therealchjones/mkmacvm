# `mkmacvm`

Build a simple macOS virtual machine for Parallels Desktop with minimal
interaction

## Requirements

- macOS 12.2 Monterey
- Paralells Desktop Pro 17

## Usage

1. In Terminal, on the macOS host computer:

   ```shell
   sudo ./mkmacvm
   ```

2. When prompted, within the new virtual machine, choose a language, then open a terminal and run:

   ```shell
   /Volumes/Image Volume/install
   ```

3. There is no step 3.

## FAQ

- Why did I get an error that reads:

  ```shell
  Error erasing disk error number (22, 0) An error occurred erasing the disk.
  ```

  I have no idea. I don't know what it means or why it happens. However, thanks to
  [this post](https://www.blackmanticore.com/659444a81916ef87765c979e4231753d),
  I can tell you that it likely happened after a previous attempt failed, and I
  can recommend rebooting your computer as a reasonable and reliable fix (until
  it happens again).

## Acknowledgments

Though it does not share any meaningful source code with them, this project is
heavily inspired by the excellent
[macdeploystick](https://bitbucket.org/twocanoes/macdeploystick/src/master/) and
[pycreateuserpkg](https://github.com/gregneagle/pycreateuserpkg) projects.
(They're also great programs for more general solutions outside the scope of
`mkmacvm`, and they actually work.) Please see [LICENSE](LICENSE) for further
acknowledgment of their contributions.
