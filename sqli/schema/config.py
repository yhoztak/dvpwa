import os
import trafaret as T


CONFIG_SCHEMA = T.Dict({
    T.Key('db'): T.Dict({
        'user': T.String(),
        'password': T.String(default=os.getenv('DB_PASSWORD')),
        'host': T.String(),
        'port': T.Int(),
        'database': T.String(),
    }),
    T.Key('redis'): T.Dict({
        'host': T.String(),
        'port': T.Int(),
        'db': T.Int(),
    }),
    T.Key('app'): T.Dict({
        'host': T.String(),
        'port': T.Int(),
    }),
})
