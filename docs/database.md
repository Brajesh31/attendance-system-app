# Data storage

Redis is the application datastore. It stores biometric embeddings and attendance events rather than using a relational database.

## Keys

`academy:register` stores one embedding per `Name@Role` field. `attendance:logs` stores recognized events as strings. The report page derives date, in/out timestamps, durations, and status from the event list.

## Operational requirements

Use a dedicated Redis database or namespace per environment, require authentication and TLS, disable public access, configure retention/expiry, and back up only when policy permits. Treat embeddings and attendance logs as sensitive personal data. Provide deletion and correction workflows.
