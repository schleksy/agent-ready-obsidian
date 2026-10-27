# Optional Base examples

A Base is a view over note properties, not a second store of facts. Use one only when several notes represent comparable records, share useful properties, and benefit from repeated sorting or filtering.

These examples are not installed by the initializer. First establish the user's actual schema and statuses, then adapt the filter and place the `.base` file in the relevant private vault folder. Link it from its governing Hub with the extension.

- [Projects.base](Projects.base) illustrates a scoped view of unfinished Project records.
- [Ideas.base](Ideas.base) illustrates a scoped Incubator view.

The examples use `type`, `status`, `outcome`, `next_step`, and `idea_type` from the documented note model. `completed`, `cancelled`, `promoted`, and `rejected` are example lifecycle values; they do not establish the state of any real user's work.

Test at least one expected inclusion and one exclusion in Obsidian. A syntactically valid filter can still show the wrong records. Check missing properties, archived locations, and the user's actual status capitalization before adoption. Do not create a Base merely to display these empty examples.
