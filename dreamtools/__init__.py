
# this is used in D8C1. could be simplified.
from .core.sageutils import Login
from .core import settings
import os
configuration = settings.DreamToolsConfig()
dreampath = configuration.user_config_dir


from dreamtools.core.challenge import Challenge

from dream2.D2C1.scoring import D2C1
from dream2.D2C2.scoring import D2C2
from dream2.D2C3.scoring import D2C3
from dream2.D2C4.scoring import D2C4
from dream2.D2C5.scoring import D2C5

from dream3.D3C1.scoring import D3C1
from dream3.D3C2.scoring import D3C2
from dream3.D3C3.scoring import D3C3
from dream3.D3C4.scoring import D3C4

from dream4.D4C1.scoring import D4C1
from dream4.D4C2.scoring import D4C2
from dream4.D4C3.scoring import D4C3

from dream5.D5C1.scoring import D5C1
from dream5.D5C2.scoring import D5C2
from dream5.D5C3.scoring import D5C3
from dream5.D5C4.scoring import D5C4

from dream6.D6C3.scoring import D6C3
from dream6.D6C4.scoring import D6C4

from dream7.D7C1.scoring import D7C1
from dream7.D7C4.scoring import D7C4

from dream8.D8C1.scoring import D8C1
from dream8.D8C2.scoring import D8C2
from dream8.D8C3.scoring import D8C3

from dream9.D9C1.scoring import D9C1
from dream9.D9C3.scoring import D9C3

from dream9dot5.D9dot5C1.scoring import D9dot5C1

