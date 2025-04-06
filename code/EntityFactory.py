#!/usr/bin/python
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_Bg = []
                for i in range(10):
                    list_Bg.append(Background(f'Level1Bg{i}', position= (0, 0)))
                    list_Bg.append(Background(f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_Bg