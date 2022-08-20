# How to do anything from the macOS command line

No, not anything. Some. Not a lot. Commands listed here should work in a
Bourne-like shell via ssh into a new virtual machine created by the latest
version of mkmacvm. In most cases, other, easier ways exist that require user
interaction in some way, such as downloading a file using a web browser or
selecting the right option from a menu, but interactions are not allowed here.
All commands should work without depending on the installation of other
programs. If other requirements are needed, they must be explicitly noted.

## install Command Line Tools for Xcode

```shell
	CMDLINETOOLTMP="/tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress"
	touch "$CMDLINETOOLTMP"
	CMDLINETOOLS="$(softwareupdate -l 2>/dev/null \
		| sed -n \
			-e '/Command Line Tools/!d' \
			-e '/[Bb][Ee][Tt][Aa]/d' \
			-e '/^[ \*]*Label: */{s///;p;}' \
		| sort -V \
		| tail -n1)" \
	&& if [ -n "$CMDLINETOOLS" ]; then sudo softwareupdate -i "$CMDLINETOOLS"; fi
	rm "$CMDLINETOOLTMP"
```
