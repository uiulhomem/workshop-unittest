from typing import Union
import time


class Rich:
    def daily(self) -> str:
        self.talk()
        
        return self.nextchy()

    def talk(self):
        time.sleep(60)

    def nextchy(self) -> str:
        return 'Nexxxxxxxxxxxxxxtchy!'

    def rich_love(self, person: str) -> Union[str, None]:
        output = None
        if person == 'Victão':
            output = 'Fortchy!'

        return output
