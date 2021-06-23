# User agent list

A list of apps, services and bots that consume podcast **audio**. This data is used by a number of podcast hosts to assist with their analytics.

One public example is [this page at Podnews](https://podnews.net/about/podcast-stats) which uses this data alongside the RSS UA. We're aware that this data is used by a number of large podcast hosts and private podcasters too.

## Contributing to the list

The simplest way is to add to the file at `src/user-agents.json`.

Each app, service or bot should have its own entry. The user_agents should be as exclusive as possible, to avoid multiple matches.

Each entry _must_ contain the following properties:

* `user_agents` (array of strings): a list of regular expressions against which the requesting user-agent
should be validated. Backslashes ("\\") should be escaped, so instead of `^Echo\/1\.`, the string should read `^Echo\\/1\\.`.

Each entry _can_ contain one of the following properties:

* `bot` (boolean): set to `true` when the requesting agent is a bot (no need to set to `false` otherwise).
* `app` (string): set to the human-readable name of the app or service. We do not set this string if it's just a library or framework.
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
* `examples` (array of strings): a few different examples of the user-agent as seen in the wild. Caution should be taken to remove any personally identifying information
* `description` (string): intended to be a humanly readable description of the app, bot or other
* `info_url` (string): a link to the homepage of the app, bot or other, for public consumption
* `svg` (string): a name of a square SVG file, intended for use in app dashboards for identification purposes
* `developer_notes` (string): freeform notes for developers, where it is helpful to leave notes on behaviour of certain useragents or bots.

### Slugs

A slug is a lowercase alphanumeric (ASCII) representation of a string, consisting only of numbers,
letters and, in our case, underscores. It's up to apps that implement the list to display this information
however they see fit, and using a slug is better for disambiguation.

### Unknowns

It is proposed that we only specify a property above when it is _known_ (not assumed). For example, it's often
difficult to _know_ whether an Android app is running on a phone or a tablet. We can _assume_ that since
Android tablets are rarer, almost all requests will be via Android phones, but we can't _know_ that.

## Parsing order

Multiple matches should ideally not happen for anything that has an app name; so parsing order shouldn't matter. For devices and OS, you mat discover that multiple matches will give you more accurate data, but you should hopefully only see one app name.

## Testing

The ```/src``` folder contains a subfolder ```/tests``` with unit tests per programming languages. Unit tests should try to compile all the regular expressions. In case of failure, the problematic regular expressions should be fixed before pushing the changes.

### python

```bash
# Running tests with pytest
pytest
```
