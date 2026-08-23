---
description: One-time setup — create your private workspace and fill in your profile
---

Set up a broker-removal workspace for this user.

1. Pick the workspace location. Default to `$HOME/.broker-remove` unless the user
   names another. Tell them how to make it permanent:

   ```bash
   echo 'export BROKER_REMOVE_WORKSPACE="$HOME/.broker-remove"' >> ~/.bashrc
   ```

2. Create `$BROKER_REMOVE_WORKSPACE/data` and `$BROKER_REMOVE_WORKSPACE/outbox`,
   and copy `${CLAUDE_PLUGIN_ROOT}/data/profile.example.json` to
   `$BROKER_REMOVE_WORKSPACE/data/profile.json`.

3. Fill the profile in **with the user, one field at a time**. Do not guess and
   do not skip the tedious parts — this file determines how much gets found.

   Explain why each matters:
   - **Every email address ever used, including dead ones.** Brokers index on
     addresses abandoned years ago. A closed mailbox is still a search key.
   - **Every prior address and phone number.** A people-search index is built
     largely from details someone no longer uses. This is the single biggest
     factor in how many records get found.
   - **Name variants** — middle names, initials, maiden names, misspellings that
     appear on mail.
   - **`confirmation_email`** must be a mailbox they can read *today*. It is a
     different field from the identity list, and putting a dead address here
     silently voids requests.

4. Warn clearly: this file is the most sensitive artifact in the project. It must
   never be committed. Confirm the workspace is outside any git repository, or
   that it is gitignored.

5. Show them what happens next: `/broker-remove:status` for the picture,
   `/broker-remove:next` to start work.
