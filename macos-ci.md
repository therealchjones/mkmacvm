# Using macOS for automated testing

## SIP & TCC

Some things are easy (or at least easier) with SIP disabled, but that may not be
a realistic simulation of a user experience

## mkmacvm

- Requires parallels license
- Minimal, only includes what macOS does
- Only items in the TCC databases by default are whatever macOS puts there
- SIP is enabled (and won't be disabled)
- You can add to the user TCC database from the command line

## GitHub Actions

- Free
- Already has a decent "development" environment
- GitHub appears to regularly add "allowed" items to the system TCC database so
  you're not prompted
- You can also add to the user TCC database from the command line
- SIP is enabled (and [GitHub does not plan to disable](https://github.com/actions/runner-images/issues/650#issuecomment-610541765)), so you can't use the
  system TCC database

## Some notes & references

- https://circleci.com/developer/orbs/orb/circleci/macos - several jobs for the
  CircleCI environment to change different TCC settings, though many (perhaps all)
  require SIP to be disabled

- "_app_" wants access to control "_different app_". (AppleScript) -
  https://github.com/actions/runner-images/issues/553 - Finder timed out because
  dialog for permissions is showing when trying to run osascript at the
  terminal. Also incidentally scripting some Photos at the end.

- [A deep dive into macOS TCC.db](https://www.rainforestqa.com/blog/macos-tcc-db-deep-dive)

- https://github.com/actions/runner-images/issues/1541 - similar to the above, trying to run Java
- https://github.com/actions/runner-images/issues/1567 - GitHub will sometimes add entries to the system TCC database when rolling out new images
- https://github.com/actions/runner-images/issues/3286 - certainly some things need to be in the system database rather than the user one
