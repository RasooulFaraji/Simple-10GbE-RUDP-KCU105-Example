#-----------------------------------------------------------------------------
# This file is part of the 'Simple-10GbE-RUDP-KCU105-Example'. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the 'Simple-10GbE-RUDP-KCU105-Example', including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import pyrogue as pr

class AppReg(pr.Device):
    def __init__( self,**kwargs):
        super().__init__(**kwargs)

        self.add(pr.RemoteVariable(
            name         = 'Write',
            description  = 'Read from the register',
            offset       = 0x000,
            bitSize      = 16,
            mode         = 'RO',
        ))

        self.add(pr.RemoteVariable(
            name         = 'Read',
            description  = 'Write into the register',
            offset       = 0x100,
            bitSize      = 16,
            mode         = 'WO',
        ))

