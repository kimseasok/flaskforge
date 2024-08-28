from flaskforge.utils.exception import DoneExit
from flaskforge.writers.writer_factory import WriterFactory

from .base_cli_provider import AbstractProvider


class CreateRelationshipProvider(AbstractProvider):

    def handler(self, args: object):

        try:
            writer = WriterFactory(
                "relationship",
                args,
                strategy=args.relation,
                child_model=f"{args.child}_model",
            )

            writer.write_source()
        except DoneExit:
            ...
        except Exception as err:
            self.io.error(str(err))
