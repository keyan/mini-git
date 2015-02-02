# mini-git
A (re)version control system similar to git, but not really. Keeps track of file versions by implementing only a few basic git commands.

To make a new version backup:
<code>python minigit.py backup</code>

Revert to a specific backup #:
<code>python minigit.py revert #</code>

Revert to the latest backup:
<code>python minigit.py latest</code>
