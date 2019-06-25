# User agent list

A list of apps, services and bots that consume podcast data.

## Contributing to the list

For now, the simplest way is to add to the file at `src/user-agents.json`. Each app, service or
bot should have its own entry.

Each entry _must_ contain:

* A `user_agents` property, which is a list of regular expressions. Backslaches (\) should be
double-escaped, so instead of `^Echo\/1\.`, the string should read `^Echo\\/1\\.`.

Each entry _can_ contain one of the following properties:

* `bot` (boolean): set to `true` or `false`. The inference is that bot downloads shouldn't be counted.
* `app` (string): set to the human-readable name of the app or service.
* `device` (string): set to a slug of the device type, usually one of
  * `pc` (meaning a desktop or laptop computer running Linux, macOS or Windows)
  * `phone`
  * `radio` (a smart radio)
  * `speaker` (smart speaker)
  * `tablet`
  * `watch`
* `os` (string): set to the slug of the operating system, usually one of
  * `android`
  * `ios`
  * `linux`
  * `macos`
  * `windows`

If `bot` is set to `true`, no other properties need to be specified.

### Slugs

A slug is a lowercase alphanumeric (ASCII) representation of a string, consisting only of numbers,
letters and, in our case, underscores. It's up to apps that implement the list to display this information
however they see fit, and using a slug is better for disambiguation.

### Unknowns

I propose that we only specify a property above when it is _known_ (not assumed). For example, it's often
difficult to _know_ whether an Android app is running on a phone or a tablet. We can _assume_ that since
Android tablets are rarer, almost all requests will be via Android phones, but we can't _know_ that.

## Future plans

To stop the list becoming unwieldy, I'll probably separate out the apps into separate files, that are then
combined together automatically. That makes it harder to make a static list available via Github, but it's
possible to run a static site and use a CI script -- a script that is called when code is committed to this
repository -- to combine the files and generate the static file.

Happy to accept advice or actual code to make this happen :)
